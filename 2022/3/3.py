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


def common_element(arr):
    # *arr -> unpacking operator
    common = set(arr[0]).intersection(*arr)
    return common.pop()


sum_priorities = 0

for index, backpack in enumerate(backpack_content_list):
    compartments = split_string(backpack)
    shared_item_type = common_element([compartments[0], compartments[1]])
    item_priority = item_types.index(shared_item_type) + 1
    sum_priorities += item_priority

print(sum_priorities)

# Part 2
groups = []
group_sum_priorities = 0

for i in range(0, len(backpack_content_list), 3):
    groups.append(backpack_content_list[i : i + 3])

for group in groups:
    shared_item_type = common_element([group[0], group[1], group[2]])
    item_priority = item_types.index(shared_item_type) + 1
    group_sum_priorities += item_priority

print(group_sum_priorities)
