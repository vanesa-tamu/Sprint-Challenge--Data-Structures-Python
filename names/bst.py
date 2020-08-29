class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left: BSTNode = None
        self.right: BSTNode = None

    def __str__(self):
        return f'value: {self.value}'

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            # Go R
            # check if there is already a node in R
            if self.right is None:
                # insert new node with value & insert in R spot
                self.right = BSTNode(value)
            else:
                # call insert function on new root at R
                self.right.insert(value)
        if value < self.value:
            # Go L
            # check if there is already a node in L
            if self.left is None:
                # insert new node with value in L spot
                self.left = BSTNode(value)
            else:
                # call insert function on new root at L
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if target == self.value:
            return True
        elif target >= self.value:
            # Go R
            # if R is None:
            if self.right is None:
                return False  # we have traversed tree already
            # if R has value
            else:
                return self.right.contains(target)  # recurse on R node
        elif target < self.value:
            # Go L
            # check if L is None:
            if self.left is None:
                return False
            # if L has value
            else:
                return self.left.contains(target)  # recurse on L node
