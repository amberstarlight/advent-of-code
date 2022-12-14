# Day 8: Treetop Tree House

from pathlib import Path

input = Path("input.txt").read_text()
tree_input = list(filter(None, input.split("\n")))


class Tree:
    def __init__(self, x_pos, y_pos, height, visibility=None):
        self.position = [int(x_pos), int(y_pos)]
        self.height = int(height)

        if visibility == None:
            self.visibility = {
                "top": None,
                "left": None,
                "right": None,
                "bottom": None,
            }
        else:
            self.visibility = visibility

    def __repr__(self) -> str:
        return "Tree: {position}, height: {height}, {visibility}\n".format(
            position=self.position,
            height=self.height,
            visibility="visible" if self.is_visible() else "invisible",
        )

    def set_visibility(self, direction, visibility):
        self.visibility[direction] = visibility

    def is_visible(self) -> bool:
        if any(self.visibility.values()):
            return True

        return False


tree_grid = []

for y, row in enumerate(tree_input):
    tree_grid.append([])
    for x, col in enumerate(row):
        tree = Tree(
            x_pos=x,
            y_pos=y,
            height=col,
            visibility={
                "top": True if y == 0 else None,
                "left": True if x == 0 else None,
                "right": True if x == (len(row) - 1) else None,
                "bottom": True if y == (len(tree_input) - 1) else None,
            },
        )
        tree_grid[y].append(tree)


def check_visibility(tree: Tree, new_tree: Tree, direction: str):
    if tree.height <= new_tree.height:
        tree.set_visibility(direction=direction, visibility=False)
    else:
        tree.set_visibility(direction=direction, visibility=True)


# tree_input[0] and [-1] are all visible
# as is every start and end tree of each row
for y_position in range(1, len(tree_grid) - 1):
    for x_position in range(1, len(tree_grid[y_position]) - 1):
        current_tree = tree_grid[y_position][x_position]

        for _1 in range(y_position, 0, -1):
            check_visibility(
                current_tree, tree_grid[y_position - _1][x_position], direction="top"
            )
            if current_tree.visibility["top"] == False:
                break

        for _2 in range(x_position, 0, -1):
            check_visibility(
                current_tree, tree_grid[y_position][x_position - _2], direction="left"
            )
            if current_tree.visibility["left"] == False:
                break

        for _3 in range(x_position + 1, len(tree_grid[y_position])):
            check_visibility(current_tree, tree_grid[y_position][_3], direction="right")

            if current_tree.visibility["right"] == False:
                break

        for _4 in range(y_position + 1, len(tree_grid)):
            check_visibility(
                current_tree, tree_grid[_4][x_position], direction="bottom"
            )
            if current_tree.visibility["bottom"] == False:
                break

        print(
            current_tree.position,
            current_tree.height,
            current_tree.visibility,
            current_tree.is_visible(),
        )


visible_trees = 0

for row in tree_grid:
    for tree in row:
        if tree.is_visible():
            visible_trees += 1

print(visible_trees)
