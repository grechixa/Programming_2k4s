import pytest
from iter_Fibonacci import *

def test_getitem_fibonacci():
    fib = FibonacciSequence(5)
    assert list(fib) == [0,1,1,2,3]

def test_iterator_fibonacci():
    fib = Fibonacci(7)
    assert list(fib) == [0,1,1,2,3,5,8]

def test_coroutine_fibonacci():
    coro = fib_coroutine()
    next(coro)

    res = [coro.send(None) for _ in range(5)]
    assert res == [0,1,1,2,3]