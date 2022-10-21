"""MissingNumber"""

def main():
    """Input"""
    num = int(input())
    box1 = []
    while True:
        numz = int(input())
        if numz == 0:
            break
        box1.append(numz)
    box1.sort()
    for i in range(1, num+1):
        if box1.count(i) == 0:
            print(i)

main()
