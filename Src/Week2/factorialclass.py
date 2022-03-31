class Factorial:

    def algorithm(self, FactorialNumber):
        w = 1
        for i in range(1, FactorialNumber + 1):
            w = w * i
        return w


def solve():
  FactorialNumber = int(input("Enter a number:"))
  
  obj = Factorial()
  w = obj.algorithm(FactorialNumber)
  print("Factorial is:", w)
  
# def __init__(self):
#      self.Number = [0, 1]
# def __call__(self, w):