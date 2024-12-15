from threading import Lock
class ZeroEvenOdd:
    """"
    This is a good practice of using lock to synchronize threads.
    """
    def __init__(self, n):
        self.n = n
        self.zeroLock = Lock()
        self.oddLock = Lock()
        self.evenLock = Lock()
        self.oddLock.acquire()
        self.evenLock.acquire()
        self.number = 1

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.zeroLock.acquire()
            printNumber(0)
            if self.number % 2 == 1:
                self.oddLock.release()
            else:
                self.evenLock.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.evenLock.acquire()
            printNumber(i)
            self.number += 1
            self.zeroLock.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.oddLock.acquire()
            printNumber(i)
            self.number += 1
            self.zeroLock.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.oddLock.acquire()
            printNumber(i)
            self.number += 1
            self.zeroLock.release()
