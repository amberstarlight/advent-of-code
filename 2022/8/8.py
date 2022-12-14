# Day 8: Treetop Tree House

from pathlib import Path

input = Path("test_input.txt").read_text()

tree_input = list(filter(None, input.split("\n")))

# tree_input[0] and [-1] are all visible
# as is every start and end tree of each row


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


for a in range(1, len(tree_grid) - 1):
    for b in range(1, len(tree_grid[a]) - 1):
        current_tree = tree_grid[a][b]
        print(current_tree.position, current_tree.height, current_tree.visibility)
