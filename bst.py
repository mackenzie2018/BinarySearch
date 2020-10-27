import math

class BNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def binarySearchTree(current, v):
    if current is None:
        return False
    elif current.value == v:
        return True
    elif current.value > v:
        return binarySearchTree(current.left, v)
    elif current.value < v:
        return binarySearchTree(current.right, v)

def binarySearchList(array, v):
    left = 0
    right = len(array) - 1

    while left <= right:
        index = left + math.floor(0.5 * (right - left))
        value = array[index]
        if value == v:
            return True
        elif value > v:
            right = index - 1
        elif value < v:
            left = index + 1

    return False

tree = BNode(
    value=10,
    right=BNode(
        value=12,
        left=BNode(
            value=11,
            left=None,
            right=None
        ),
        right=BNode(
            value=15,
            left=BNode(
                value=14,
                left=BNode(
                    value=13,
                    left=None,
                    right=None
                ),
                right=None
            ),
            right=None
        )
    ),
    left=BNode(
        value=8,
        left=BNode(
            value=3,
            left=BNode(
                value=1,
                left=None,
                right=None
            ),
            right=None
        ),
        right=BNode(
            value=9,
            left=None,
            right=None
        )
    )
)

print(binarySearchTree(tree, 1))
print(binarySearchTree(tree, 13))
print(binarySearchTree(tree, 17))

arr = [1, 5, 7, 9, 11, 15, 17]
print(binarySearchList(arr, 1))
print(binarySearchList(arr, 13))
print(binarySearchList(arr, 17))
