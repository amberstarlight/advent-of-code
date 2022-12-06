# Day 6: Tuning Trouble

from pathlib import Path

input = Path("input.txt").read_text()

queue = []

for n, c in enumerate(input):
    queue.append(c)

    if len(queue) > 4:
        queue.pop(0)

        if len(set(queue)) == 4:
            # set() returns no duplicate elements. if it returns 4 characters,
            # we have found the marker at n+1 (zero indexing, remember?)
            print("Marker found:", queue[-1], "\ncharacters processed:", n + 1)
            break
