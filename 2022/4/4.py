# Day 4: Camp Cleanup

from pathlib import Path
import string

input = Path("input.txt").read_text()
assignment_pairs = list(filter(None, input.split("\n")))  # filter out newlines

# in what circumstances can one range fully contain another
# if a1 >= a2 & b1 <= b2
# OR
# if a2 >= a1 & b2 <= b1

overlap_count = 0

for pair in assignment_pairs:
    assignments = pair.split(",")

    elf1 = assignments[0].split("-")
    elf2 = assignments[1].split("-")

    a1 = int(elf1[0])
    b1 = int(elf1[1])
    a2 = int(elf2[0])
    b2 = int(elf2[1])

    if (a1 >= a2 and b1 <= b2) or (a2 >= a1 and b2 <= b1):
        overlap_count += 1

print(overlap_count)
