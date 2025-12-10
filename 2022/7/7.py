# Day 7: No Space Left On Device

from pathlib import Path

input = Path("input.txt").read_text()

terminal_output_lines = list(filter(None, input.split("\n")))


class File:
    def __init__(
        self,
        filetype: str,
        name: str,
        size: int,
        parent_directory,
    ):
        self.filetype = filetype
        self.name = name
        self.__size = size
        self.parent_directory = parent_directory
        self.__children = []

    def __repr__(self):
        return "{0}: {1}, size: {2}, {3}, contents: {4} \n".format(
            self.filetype.title(),
            self.name,
            self.get_size(),
            (
                ("parent directory: " + self.parent_directory.name)
                if self.parent_directory != None
                else "root"
            ),
            self.__children,
        )

    def get_child(self, name: str):
        match = list(filter(lambda file: file.name == name, self.__children))
        if len(match) > 0:
            return match[0]
        return None

    def add_child(self, file):
        self.__children.append(file)

    def get_size(self):
        if self.filetype == "file":
            return self.__size

        size = 0
        for file in self.__children:
            match file.filetype:
                case "file":
                    size += file.__size
                case "directory":
                    size += file.get_size()

        return size

    def get_children(self):
        return self.__children


root_dir = File(
    filetype="directory",
    name="/",
    size=0,
    parent_directory=None,
)

current_dir = root_dir
prev_dir = None

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
                    current_dir = current_dir.parent_directory
                case "/":
                    prev_dir = current_dir
                    current_dir = root_dir
                case _:
                    prev_dir = current_dir
                    current_dir = current_dir.get_child(cmd_args)

        if command == "ls":
            # nothing to do,
            continue

    if start_char.isdigit():
        file_info = line.split()
        file = File(
            filetype="file",
            name=file_info[1],
            size=int(file_info[0]),
            parent_directory=current_dir,
        )

        current_dir.add_child(file)

    if start_char == "d":
        dir_name = line[4:]
        new_dir = File(
            filetype="directory",
            name=dir_name,
            size=0,
            parent_directory=current_dir,
        )

        current_dir.add_child(new_dir)

# print(root_dir)


def sum_directories_smaller_than(files: list, size: int):
    total_size = 0

    for file in files:
        if file.filetype != "directory":
            continue

        if file.get_size() <= size:
            total_size += file.get_size()

        total_size += sum_directories_smaller_than(file.get_children(), size)

    return total_size


def get_dirs_larger_than(files: list, size: int):
    dirs = []

    for file in files:
        if file.filetype != "directory":
            continue

        if file.get_size() >= size:
            dirs.append(file)

        x = get_dirs_larger_than(file.get_children(), size)

        if len(x) > 0:
            dirs.extend(x)

    return dirs


print("Part 1:", sum_directories_smaller_than(root_dir.get_children(), 100000))

# Part 2

filesystem_size = 70000000
required_size = 30000000
free_space = filesystem_size - root_dir.get_size()

print("Free space:", free_space, "\n")

candidate_dirs = get_dirs_larger_than(
    root_dir.get_children(), required_size - free_space
)
candidate_dirs.sort(key=File.get_size)

print(candidate_dirs[0].get_size())
