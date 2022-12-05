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


def parse_crates(crate_string: str):
    crate_layers = crate_input.split("\n")[:-1]
    num_stacks = len(crate_input.split("\n").pop(-1).split())

    stacks = []
    for n in range(0, num_stacks):
        stacks.append([])

    for layer in crate_layers:
        x = 0
        while x < num_stacks:  # while there are still crates to parse in this layer
            crate = layer[1 + (x * 4)]
            if crate != " ":  # if there is actually a crate at this location
                stacks[x].append(crate)
            x += 1  # increment the stack counter

    return stacks


crates = parse_crates(crate_input)

for n, stack in enumerate(crates):
    print(n, stack)
