"""Sequence VIII"""

def sequenceviii():
    """print"""
    num = int(input())
    if num > 0 and num < 100:
        for i in range(1, num+1):
            for k in range(num, 1, -1):
                if k > i:
                    print("  ", end=' ')
            for j in range(1, num+1, 1):
                if j <= i:
                    print("%02d" % j, end=' ')
            i = i + 1
            print()
sequenceviii()
