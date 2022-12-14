import time

class FiboIter():
    
    def __init__(self, limit):
        self.limite = limit

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        elif self.counter == self.limite:
            raise StopIteration
        else:
            self.n1, self.n2 = self.n2, (self.n1 + self.n2)
            self.counter += 1
            return self.n2

if __name__ == '__main__':
    limit = round(float(input("Ingrese un numero: ")))
    fibonacci = FiboIter(limit)
    
    for element in fibonacci:
        print(element)
        time.sleep(0.05)