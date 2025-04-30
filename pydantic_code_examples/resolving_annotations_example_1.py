 {test="skip" lint="skip"}
class Node:
    """Binary tree node."""

    # NameError: name 'Node' is not defined:
    def __init__(self, l: Node, r: Node) -> None:
        self.left = l
        self.right = r
