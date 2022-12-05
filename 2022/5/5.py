# Day 5: Supply Stacks

from pathlib import Path
import re
import copy

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
    crate_layers = crate_string.split("\n")[:-1]
    num_stacks = len(crate_string.split("\n").pop(-1).split())

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


def rearrange_crates(crates: list, instructions: list, crane_type: str):
    arrangement = copy.deepcopy(crates)

    for instruction in instructions:
        matches = re.findall(r".... (\d{1,}) .... (\d{1,}) .. (\d{1,})", instruction)
        instruction_items = list(matches[0])

        crates_to_move = int(instruction_items[0])
        from_stack = int(instruction_items[1]) - 1  # because crates is zero-indexed
        to_stack = int(instruction_items[2]) - 1  # because crates is zero-indexed

        for i in range(0, crates_to_move):
            moving_crate = arrangement[from_stack].pop(0)
            arrangement[to_stack].insert(
                0 if crane_type == "CrateMover 9000" else i, moving_crate
            )

    return arrangement


def get_crate_message(crates: list):
    top_crates = []

    for stack in crates:
        crate = stack.pop(0)
        top_crates.append(crate)

    return "".join(top_crates)


crates = parse_crates(crate_input)
print("\nStarting crates:\n", crates)

simulated_rearranged_crates = rearrange_crates(
    crates, rearrangement_procedure, crane_type="CrateMover 9000"
)
print("Simulated rearranged crates:\n", simulated_rearranged_crates)

simulated_message = get_crate_message(simulated_rearranged_crates)
print("Theoretical message:\n", simulated_message)

# Part 2
print("\nStarting crates:\n", crates)

rearranged_crates = rearrange_crates(
    crates, rearrangement_procedure, crane_type="CrateMover 9001"
)
print("Rearranged crates:\n", rearranged_crates)

message = get_crate_message(rearranged_crates)
print("Message:\n", message)
