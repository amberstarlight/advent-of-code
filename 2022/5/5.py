# Day 5: Supply Stacks

from pathlib import Path
import re

input = Path("input.txt").read_text()

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


def rearrange_crates(crates: list, instructions: list):
    rearranged_crates = crates.copy()

    for instruction in instructions:
        matches = re.findall(r".... (\d{1,}) .... (\d{1,}) .. (\d{1,})", instruction)
        instruction_items = list(matches[0])

        crates_to_move = int(instruction_items[0])
        from_stack = int(instruction_items[1]) - 1  # because crates is zero-indexed
        to_stack = int(instruction_items[2]) - 1  # because crates is zero-indexed

        for i in range(0, crates_to_move):
            moving_crate = crates[from_stack].pop(0)
            crates[to_stack].insert(0, moving_crate)

    return rearranged_crates


crates = parse_crates(crate_input)
print("Starting crates:", crates)

rearranged_crates = rearrange_crates(crates, rearrangement_procedure)
print("Rearranged crates:", crates)

message = []

for stack in rearranged_crates:
    top_crate = stack.pop(0)
    message.append(top_crate)

print("Message:", "".join(message))
