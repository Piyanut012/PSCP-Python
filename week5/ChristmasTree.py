"""ChristmasTree"""

def main(size, size_body):
    """Input"""
    for i in range(1, size+1, 1):
        print(" " * (size - i), end="")
        print("*" * (i * 2 - 1))
    for i in range(1, size_body+1, 1):
        print(" " * (size - 2) + "---")

main(int(input()), int(input()))
