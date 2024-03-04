import random


def inorder(node):
    """
    Generador para recorrer el treap de forma inorder.

    Args:
    - node (`Node`): Nodo del treap.
    """
    if node:
        yield from inorder(node.left)
        yield node.value
        yield from inorder(node.right)


class ImplicitTreap:
    """
    Treap implícito.

    Referencias:
    - https://usaco.guide/adv/treaps?lang=cpp
    """

    class Node:
        """
        Nodo del treap.
        """

        def __init__(self, value, priority, left=None, right=None):
            self.value = value
            self.priority = priority
            self.left = left
            self.right = right
            self.size = 1

        def __str__(self):
            return ' '.join(map(str, inorder(self)))

        def __repr__(self):
            return str(self)

    def __init__(self):
        self.root = None

    def _size(self, node):
        return node.size if node else 0

    def _update(self, node):
        if node:
            node.size = self._size(node.left) + 1 + self._size(node.right)

    def split(self, node, index):
        """
        Realiza la operación de split en el treap.

        Retorna una tupla con dos nodos, el primero con los primeros `index` elementos
        y el segundo con el resto de los elementos.

        Args:
        - node (`Node`): Nodo del treap.
        - index (`int`): Índice en el que se realiza el split.
        """

        if node is None:
            return None, None
        if index <= self._size(node.left):
            left, right = self.split(node.left, index)
            node.left = right
            self._update(node)
            return left, node
        else:
            left, right = self.split(
                node.right, index - self._size(node.left) - 1)
            node.right = left
            self._update(node)
            return node, right

    def merge(self, left, right):
        """
        Realiza la operación de merge en el treap.

        Retorna el nodo resultante de unir los nodos `left` y `right`.

        Args:
        - left (`Node`): Nodo izquierdo.
        - right (`Node`): Nodo derecho.
        """

        if left is None:
            return right
        if right is None:
            return left
        if left.priority > right.priority:
            left.right = self.merge(left.right, right)
            self._update(left)
            return left
        else:
            right.left = self.merge(left, right.left)
            self._update(right)
            return right

    def insert(self, index, value):
        """
        Inserta un valor en el treap en la posición `index`.

        Args:
        - index (`int`): Índice en el que se inserta el valor.
        - value: Valor a insertar.
        """

        new_node = self.Node(value, random.random())
        left, right = self.split(self.root, index)
        self.root = self.merge(self.merge(left, new_node), right)

    def __str__(self):
        return str(self.root)

    def __repr__(self):
        return str(self)
