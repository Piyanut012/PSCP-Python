"""Diamond I"""

def main():
    """Input"""
    high = int(input())
    long = int(input())
    box = []
    for _ in range(high):
        num = input()
        num = num.split()
        box.extend(num)
    sumz = 0
    pos = 0
    box_total = []
    for i in range(long):
        for j in range(high):
            pos = j * long + i
            sumz += int(box[pos])
        box_total.append(sumz)
        sumz = 0
        pos = 0
    print(max(box_total))
main()
