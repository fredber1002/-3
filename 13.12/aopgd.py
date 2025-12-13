class Calculator:
    def __init__(self):
        self.history = []
        self.memory = 0

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            print("Ошибка: деление на ноль")
            return None
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def memory_save(self, value):
        self.memory = value

    def memory_recall(self):
        return self.memory

    def memory_clear(self):
        self.memory = 0

    def show_history(self):
        for op in self.history:
            print(op)

    def clear_history(self):
        self.history.clear()

    def get_statistics(self):
        stats = {
            "add": 0,
            "subtract": 0,
            "multiply": 0,
            "divide": 0
        }
        for op in self.history:
            if "+" in op:
                stats["add"] += 1
            elif "-" in op:
                stats["subtract"] += 1
            elif "*" in op:
                stats["multiply"] += 1
            elif "/" in op:
                stats["divide"] += 1
        return stats

    def undo_last_operation(self):
        if self.history:
            self.history.pop()

