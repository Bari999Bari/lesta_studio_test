# Ниже два варианта реализации очереди с помощью кольцевого буфера.
# Второй вариант менее эффективен потому, что
# операция извлечения элемента из очереди
# выполняется за O(n), в то время как в первой реализации все операции
# выполняются за O(1). Незначительным плюсом второго варианта
# является относительная простота реализации

# эффективная
class Queue:
    """Реализация очереди методом кольцевого буфера."""

    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.len = 0

    def push(self, item):
        """Добавление элемента в очередь."""
        if self.queue[self.tail] is None:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_n
            self.len += 1
        else:
            return 'error'

    def pop(self):
        """Извлечение элемента из очереди."""
        if self.len == 0:
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.len -= 1
        return x

    def peek(self):
        """Получение значения первого элемента в очереди."""
        return self.queue[self.head]

    def size(self):
        """Возвращает размер очереди."""
        return self.len

# неэфективная
class Queue_2:
    """Неэффективная реализация очереди методом кольцевого буфера."""

    def __init__(self, n):
        self.queue = []
        self.max_n = n
        self.len = 0

    def push(self, item):
        """Добавление элемента в очередь."""
        if self.len < self.max_n:
            self.queue.append(item)
            self.len += 1
        else:
            return 'error'

    def pop(self):
        """Извлечение элемента из очереди."""
        if self.len == 0:
            return None

        x = self.queue[0]
        del self.queue[0]
        self.len -= 1
        return x

    def peek(self):
        """Получение значения первого элемента в очереди."""
        return self.queue[0]

    def size(self):
        """Возвращает размер очереди."""
        return self.len
