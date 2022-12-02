# Day 1: Calorie Counting

from pathlib import Path

input = Path("input.txt").read_text()

elf_lists = input.split("\n\n")
int_lists = []

for list in elf_lists:
    temp_var = list.split("\n")

    for i, x in enumerate(temp_var):
        if x != "":
            temp_var[i] = int(x)

    if x != "":
        int_lists.append(temp_var)

for i, list in enumerate(int_lists):
    int_lists[i] = sum(list)

top_three = []

for i in range(0, 3):
    max_value = max(int_lists)
    max_index = int_lists.index(max_value)
    top_three.append(max_value)
    int_lists.pop(max_index)

print(top_three)
top_three_total = sum(top_three)

print(top_three_total)
