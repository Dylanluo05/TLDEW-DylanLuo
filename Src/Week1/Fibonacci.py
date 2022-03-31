# Factorial of a number using recursion
def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)

def Tester():
    num = int(input("Enter a number for fibonacci terms: "))
    A1, A2 = 0, 1
    count = 0
  
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num ==1:
        print("Fibonacci sequence upto",num,":")
        print(A1)
    else:
       print("Fibonacci sequence:")
    while count < num:
       print(A1)
       nth = A1 + A2
       A1 = A2
       A2 = nth
       count += 1
