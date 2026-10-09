#!/usr/bin/env python3

POINT = "p"
LINES = [f"ell-{i}" for i in range(8)]
GROUPS = [f"group-{i}" for i in range(6)]

groups_met = {line: set() for line in LINES}
groups_met["ell-0"] = set(GROUPS)
for index, line in enumerate(LINES[1:], 1):
    groups_met[line] = set(GROUPS[: min(index, 5)])

exceptional = [line for line, groups in groups_met.items() if len(groups) > 5]

assert len(exceptional) == 1
assert len(exceptional) <= 5
assert all(len(groups_met[line]) <= 5 for line in LINES if line not in exceptional)

adaptive_cover_line = exceptional[0]
covered_selected_edges = len(groups_met[adaptive_cover_line])

assert covered_selected_edges == 6
assert covered_selected_edges > 5

print("Point:", POINT)
print("Exceptional lines allowed by weakened lemma:", exceptional)
print("Adaptively chosen cover line:", adaptive_cover_line)
print("Selected edges covered:", covered_selected_edges)
print("The final per-line bound of five does not follow.")
