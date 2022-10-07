"""diamond"""

def main(num):
    """Input"""
    half = int(num/2)
    for i in range(half):
        if i == 0:
            print(" " * (half-i) + "*")
        else:
            print(" " * (half-i) + "*" + " " * (i*2-1) + "*")
    print("*" * num)
    for i in range(half-1, -1, -1):
        if i == 0:
            print(" " * (half-i) + "*")
        else:
            print(" " * (half-i) + "*" + " " * (i*2-1) + "*")
main(int(input()))
