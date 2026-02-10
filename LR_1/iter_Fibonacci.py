from typing import Generator

class FibonacciSequence:
    """Последовательность чисел Фибоначчи с доступом по индексу."""

    # максимально допустимый индекс. нужен, чтобы понять когда выбрасывать IndexError
    def __init__(self, limit: int) -> None:
        self.limit = limit

    def __getitem__(self, index: int) -> int:
        if index < 0:
            raise IndexError

        if index >= self.limit:
            raise IndexError

        a, b = 0, 1
        for _ in range(index):
            a, b = b, a + b

        return a

class Fibonacci:
    """Последовательность чисел Фибоначчи."""

    def __init__(self, limit: int) -> None:
        self.limit = limit

    def __iter__(self) -> "FibonacciIterator":
        return FibonacciIterator(self.limit)


class FibonacciIterator:
    """Итератор чисел Фибоначчи."""

    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.count = 0
        self.a = 0
        self.b = 1

    def __iter__(self) -> "FibonacciIterator":
        return self
    
    def __next__(self) -> int:
        if self.count >= self.limit:
            raise StopIteration
        
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return value
    
def fib_coroutine() -> Generator[int, None, None]:
    """Сопрограмма, возвращающая числа Фибоначчи."""

    a,b = 0,1
    yield

    while True:
        yield a
        a,b = b, a+b

coro = fib_coroutine()
next(coro) # запуск
coro.send(None)  # 0
coro.send(None)  # 1
