#!/usr/bin/env python3

import json
import random
import shutil
from pathlib import Path


def find_repo_root(path: Path) -> Path:
    for candidate in path.resolve().parents:
        if (candidate / ".git").exists():
            return candidate
    raise RuntimeError("repository root not found")


ROOT = find_repo_root(Path(__file__))
SOURCE = (
    ROOT
    / "preprints"
    / "A-Counterexample-to-Rysers-Covering-Conjecture-September-23-2026"
    / "build"
)
OUTPUT = Path(__file__).resolve().parent / "generated"
SEED = 6102028

SECTIONS = [
    "paper.tex",
    "incidence.tex",
    "linecover.tex",
    "selection.tex",
    "construction.tex",
]

ORIGINAL_PROSE = (
    "Our construction also starts from a finite plane and inserts exceptional\n"
    "edges, but keeps one part for each ambient direction."
)
CONTROL_PROSE = (
    "Our construction begins with a finite plane and adds exceptional edges,\n"
    "while retaining one part for every ambient direction."
)
ORIGINAL_PROPERTY = (
    "\\item For every finite point \\(p\\) and affine line \\(\\ell\\)\n"
    "not through \\(p\\), at most five groups \\(i\\) have a candidate\n"
    "\\(P_{i,k}\\) containing a point \\(y\\in\\ell\\) whose join to\n"
    "\\(p\\) has direction in \\(S_i\\)."
)
CORRUPTED_PROPERTY = (
    "\\item For every finite point \\(p\\), all but at most five affine lines\n"
    "\\(\\ell\\) not through \\(p\\) have the following property: at most five\n"
    "groups \\(i\\) have a candidate \\(P_{i,k}\\) containing a point\n"
    "\\(y\\in\\ell\\) whose join to \\(p\\) has direction in \\(S_i\\)."
)
ORIGINAL_UNION_BOUND = (
    "There are at most\n"
    "\\(q^2q(q+1)=O(q^4)\\) pairs \\((p,\\ell)\\).  The union bound gives\n"
    "a total failure probability \\(O_{s,K}(q^{-2})\\), proving the claim."
)
CORRUPTED_UNION_BOUND = (
    "For each fixed \\(p\\), the expected number of exceptional lines is\n"
    "\\(O_{s,K}(q^{-4})\\).  Markov's inequality shows that the probability\n"
    "of more than five exceptional lines is \\(O_{s,K}(q^{-4})\\).  A union\n"
    "bound over the \\(q^2\\) choices of \\(p\\) proves the claim."
)


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


def render_variant(kind: str) -> str:
    chunks = [
        "A counterexample to Ryser's covering conjecture\n",
        "Author: OpenAI\n",
        "Date: September 23, 2026\n\n",
    ]
    for section in SECTIONS:
        text = (SOURCE / section).read_text()
        if section == "paper.tex" and kind != "released":
            text = replace_once(text, ORIGINAL_PROSE, CONTROL_PROSE, kind)
        if section == "construction.tex" and kind == "adaptive-exception":
            text = replace_once(
                text,
                ORIGINAL_PROPERTY,
                CORRUPTED_PROPERTY,
                kind,
            )
            text = replace_once(
                text,
                ORIGINAL_UNION_BOUND,
                CORRUPTED_UNION_BOUND,
                kind,
            )
        chunks.extend(
            [
                f"\n===== BEGIN {section} =====\n\n",
                text,
                f"\n===== END {section} =====\n",
            ]
        )
    return "".join(chunks)


def main() -> None:
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)

    conditions = ["released", "prose-control", "adaptive-exception"]
    document_ids = ["doc-29", "doc-63", "doc-81"]
    random.Random(SEED).shuffle(document_ids)
    assignment = dict(zip(document_ids, conditions))

    for document_id, condition in assignment.items():
        document_dir = OUTPUT / document_id
        document_dir.mkdir()
        (document_dir / "manuscript.txt").write_text(render_variant(condition))

    manifest = {
        "seed": SEED,
        "assignment": assignment,
        "detection_criterion": (
            "Identify that the weakened pool property permits exceptional lines "
            "and cannot bound an adaptively chosen cover line."
        ),
    }
    (OUTPUT / "ground_truth.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n"
    )


if __name__ == "__main__":
    main()
