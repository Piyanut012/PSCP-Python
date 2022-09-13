"""Sequence IX"""

def sequenceix():
    """print"""
    num = int(input())
    if num > 0 and num < 100:
        for i in range(1, num+1):
            for space in range(num, 1, -1):
                if space > i:
                    print("  ", end=' ')
            for num_front in range(1, num+1, 1):
                if num_front <= i:
                    print("%02d" % num_front, end=' ')
            for num_back in range(i-1, 0, -1):
                print("%02d" % num_back, end=' ')
            i = i + 1
            print()

sequenceix()
