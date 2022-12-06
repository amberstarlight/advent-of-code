# Day 6: Tuning Trouble

from pathlib import Path

input = Path("input.txt").read_text()


def find_marker(input: str, index: int):
    queue = []
    marker = ""
    marker_index = 0

    for n, c in enumerate(input):
        queue.append(c)

        if len(queue) > index:
            queue.pop(0)

            if len(set(queue)) == index:
                # set() returns no duplicate elements.
                # if it returns len(index) characters,
                # we have found the marker at n+1
                # (zero indexing, remember?)
                marker = queue[-1]
                marker_index = n + 1
                break

    return marker, marker_index


part_one_answer = find_marker(input, 4)
part_two_answer = find_marker(input, 14)

print(part_one_answer, part_two_answer)
