"""SequenceV"""
import math
def sequencev():
    """print"""
    num = int(input())
    start = num
    end = num - 7
    num2 = math.ceil(num/7)
    for i in range(1, num2+1):
        for j in range(start, end, -1):
            if j > 0:
                print(j, end=" ")
        start = start - 7
        end = end - 7
        i = i + 1
        print()


sequencev()
