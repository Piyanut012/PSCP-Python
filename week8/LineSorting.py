"""LineSorting"""

def main():
    """Input"""
    num = int(input())
    box = []
    for _ in range(num):
        box.append(input())
    box.sort(key=len)
    for i in box:
        print(i)
main()
