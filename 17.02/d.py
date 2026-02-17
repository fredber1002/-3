1. Массив
arr = [10, 20, 30, 40]  # создаю массив

print(arr[2])  # доступ по индексу 

arr.append(50)  # добавление в конец
print(arr)     # вывод массива

2. Стек (Stack)
stack = []
stack.append(1)  # push
stack.append(2)
stack.append(3)
print(stack.pop())  # pop → 3
print(stack)        # [1, 2]

3. Хеш-таблица
d = {}
d["apple"] = 5
d["banana"] = 3

print(d["apple"])  # 5

4. Древо
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)

5. граф

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
}
print(graph["A"])  # ['B', 'C']

6. множество
s = {1, 2, 3}
s.add(4)
print(2 in s)  # True
