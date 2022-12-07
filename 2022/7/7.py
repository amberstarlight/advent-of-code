# Day 7: No Space Left On Device

from pathlib import Path

input = Path("test_input.txt").read_text()

terminal_output_lines = list(filter(None, input.split("\n")))


class File:
    def __init__(
        self,
        filetype: str,
        name: str,
        size: int,
        parent_directory: str = "",
        children: list = [],
    ):
        self.filetype = filetype
        self.name = name
        self.size = size
        self.parent_directory = parent_directory
        self.children = children

    def __repr__(self):
        return "{0}: {1}, size: {2}, {3}, {4}".format(
            self.filetype.title(),
            self.name,
            self.size,
            ("parent directory: " + self.parent_directory)
            if self.parent_directory != ""
            else "root",
            self.children,
        )


filesystem = [
    File(
        filetype="directory",
        name="/",
        size=0,
        parent_directory="",
        children=[],
    )
]

root = filesystem[0].children
dir_depth = 0
current_dir = ""
prev_dir = ""

for line in terminal_output_lines:
    start_char = line[0]

    print("pwd =", current_dir)

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
                    prev_dir = current_dir
                    current_dir = cmd_args
                case _:
                    dir_depth += 1
                    prev_dir = current_dir
                    current_dir = cmd_args

        if command == "ls":
            # nothing to do,
            continue

    if start_char.isdigit():
        file_info = line.split()
        file = File(
            filetype="file",
            name=file_info[1],
            size=file_info[0],
            parent_directory=current_dir,
        )
        print(file)

    if start_char == "d":
        dir_name = line[4]
        new_dir = File(
            filetype="directory",
            name=dir_name,
            size=0,
            parent_directory=current_dir,
        )
        print(new_dir)

        if current_dir == "/":
            root.append(new_dir)
        else:
            root.children.append()

print(filesystem)
