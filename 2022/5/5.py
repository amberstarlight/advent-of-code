# Day 5: Supply Stacks

from pathlib import Path

input = Path("test_input.txt").read_text()

crate_input = input.split("\n\n")[0]
rearrangement_procedure = list(filter(None, input.split("\n\n")[1].split("\n")))

#     [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3

# a 'crate' is 3 chars: "[", "A-Z", "]"
# crates are separated by a space,
# thus: a crate's identifier (it's letter) appears every (1 + (n*4)) chars

crate_layers = crate_input.split("\n")[:-1]
num_stacks = len(crate_input.split("\n").pop(-1).split())

for n, layer in enumerate(crate_layers):
    print(n, layer)
