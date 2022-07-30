"""
Given the following definition of a Node ,
please implement preorder traversal right inside Node.
The sequence returned should be the sequence of values,
not their containing nodes.
"""

from unittest import TestCase


PRE_ORDER = 1
IN_ORDER = 2
POS_ORDER = 3


class Node:

    def __init__(self, value, left: "Node" = None, right: "Node" = None):
        self.right = right
        self.left = left
        self.value = value

        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def traverse(self, order):
        # General traverse given an order: PRE, IN, POS
        def walk(node: Node):
            if not node:
                return
            if order == PRE_ORDER:
                yield node
            yield from walk(node.left)
            if order == IN_ORDER:
                yield node
            yield from walk(node.right)
            if order == POS_ORDER:
                yield node

        for node in walk(self):
            yield node.value

    # NOTE: Statefull iterators cannnot be recursive
    # That's why you need yield "from"
    def traverse_preorder(self):
        def walk(node: Node):
            if not node:
                return
            yield node
            yield from walk(node.left)
            yield from walk(node.right)

        for node in walk(self):
            yield node.value


class Evaluate(TestCase):
    def test_exercise(self):
        node = Node('a',
                    Node('b',
                        Node('c'),
                        Node('d')),
                    Node('e'))
        self.assertEqual(
        'abcde',
        ''.join([x for x in node.traverse_preorder()])
        )
      
# ---------------
tree = Node(
            'd',
            Node(
                'b',
                Node('a'),
                Node('c')
            ),
            Node(
                'g',
                Node('e'),
                Node('f')
            )
        )


print (''.join([x for x in tree.traverse(IN_ORDER)]))
