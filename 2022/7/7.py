# Day 7: No Space Left On Device

from pathlib import Path

input = Path("test_input.txt").read_text()

terminal_output_lines = list(filter(None, input.split("\n")))


class Directory:
    def __init__(self, name: str, contents: list = []):
        self.name = name
        self.contents = contents

    def __repr__(self):
        return "Directory: {0}, {1}".format(self.name, self.contents)


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __repr__(self):
        return "File: {0}, {1}".format(self.name, self.size)


filesystem = [Directory("/", [])]
root = filesystem[0].contents
dir_depth = 0
current_dir = ""
prev_dir = ""

for line in terminal_output_lines:
    start_char = line[0]

    # we have 4 possible cases
    # $ cd <dir>
    # $ ls
    # dir <x>
    # <filesize> <filename>

    if start_char == "$":
        # command cases
        command = line[2:4]
        cmd_args = line[5:]

        if command == "cd":
            match cmd_args:
                case "..":
                    dir_depth -= 1
                    current_dir = prev_dir
                case "/":
                    dir_depth = 0
                    current_dir = cmd_args
                case _:
                    dir_depth += 1
                    current_dir = cmd_args

        if command == "ls":
            # nothing to do,
            continue

    if start_char.isdigit():  # file
        file_info = line.split()
        file = File(file_info[1], file_info[0])
        print(file)

    if start_char == "d":
        dir_name = line[4]
        new_dir = Directory(dir_name, [])
        print(new_dir)
        print(filesystem)

print(filesystem)
