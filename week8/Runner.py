"""Runner"""

def main():
    """Input"""
    distance = float(input())
    num = int(input())
    box = []
    for _ in range(num):
        txt = input()
        txt = txt.split()
        box.append(txt)
    runnerlist = box[:]
    box.sort(key=lambda i: int(i[0]), reverse=True)
    box.sort(key=lambda i: float(distance-int(i[1]))/int(i[0]))
    print(runnerlist.index(box[0]) + 1)

main()
