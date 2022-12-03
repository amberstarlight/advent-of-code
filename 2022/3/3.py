# Day 3: Rucksack Reorganisation

from pathlib import Path
import string

input = Path("input.txt").read_text()
backpack_content_list = list(filter(None, input.split("\n")))  # filter out newlines

item_types = list(string.ascii_lowercase + string.ascii_uppercase)


def split_string(string):
    n = len(string)
    first_half = slice(0, n // 2)
    second_half = slice(n // 2, n)
    return [string[first_half], string[second_half]]


def shared_char(list_a, list_b):
    shared_char = set(list_a) & set(list_b)
    return shared_char.pop()


sum_priorities = 0

for index, backpack in enumerate(backpack_content_list):
    compartments = split_string(backpack)
    shared_item_type = shared_char(compartments[0], compartments[1])
    item_priority = item_types.index(shared_item_type) + 1

    print(shared_item_type, item_priority)
    sum_priorities += item_priority

print(sum_priorities)
