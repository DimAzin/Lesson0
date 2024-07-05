class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start if start % 2 == 0 else start + 1  
        self.end = end
        self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            current_even = self.current
            self.current += 2
            return current_even



en = EvenNumbers(10, 25)
for i in en:
    print(i)
