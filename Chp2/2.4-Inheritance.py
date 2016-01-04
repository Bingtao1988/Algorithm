class Progression:
    """Base class for any progression class"""
    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current == None:
            raise StopIteration
        else:
            answer = self._current
            self._advance()
            return answer
    def __iter__(self):
        return self
    def print_progression(self, n):
        print(" ".join(str(next(self)) for j in range(n)))

class ArithmeticProgression(Progression):
    def __init__(self, step = 1, start = 0):
        super().__init__(start)
        self._step = step

    def _advance(self):
        self._current += self._step

class GeometricProgression(Progression):
    def __init__(self, base = 2, start = 1):
        super().__init__(start)
        self._base = base

    def _advance(self):
        self._current *= self._base

class FibonacciProgression(Progression):
    def __init__(self, first = 0, second = 1):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current
        
if __name__ == "__main__":
    instance = Progression()
    instance.print_progression(100)
    instance2 = ArithmeticProgression(4, 1)
    instance2.print_progression(5)
    instance3 = GeometricProgression(4)
    instance3.print_progression(5)
    instance4 = FibonacciProgression(0, 1)
    instance4.print_progression(10)
