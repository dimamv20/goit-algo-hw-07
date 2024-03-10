# Напишіть алгоритм (функцію), який знаходить найбільше значення у двійковому дереві пошуку
# або в AVL-дереві. Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def sum_all_value(root):
    if root is None:
        return 0
    return root.val + sum_all_value(root.left) + sum_all_value(root.right)

def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = sum_all_value(root.right)
        root.right = delete(root.right, root.val)
    return root

# tree 
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)
root = insert(root,12)

root = delete(root, 7)
sum_value = sum_all_value(root)
print(root)

# Максимальне значення в дереві
print('--'*45)
print(f'Сумма значень в дерееві: {sum_value}')

