"""FibonacciRecursionV1"""

def fibonacci(var):
    """Fibonacci"""
    if var == 0:
        return 0
    elif var == 1:
        return 1
    return fibonacci(var-1) + fibonacci(var-2)

def main():
    """Main"""
    num = int(input())
    print(fibonacci(num))
main()
