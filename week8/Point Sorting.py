"""Point Sorting"""

def main():
    """Input"""
    num = int(input())
    box = []
    for _ in range(num):
        numz = int(input())
        for _ in range(numz):
            point = input()
            pointlist = point.split()
            box.append(pointlist)
        box.sort(key=lambda i: int(i[1]), reverse=True)
        box.sort(key=lambda i: int(i[0]) + int(i[1]))
        for i in box:
            print(i[0], i[1])
        box.clear()

main()
