class Primes:
    def __init__(self):
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            current = self.current
            square_root = int(current ** 0.5)
            is_prime = True
            if square_root >= 2:
                for i in range(2, square_root + 1):
                    if current % i == 0:
                        is_prime = False
                        break
            self.current += 1
            if is_prime:
                return current

import cProfile
import itertools
cProfile.run('[p for p in itertools.takewhile(lambda x: x<10000, Primes())]')