"""Sequence I"""
def sequencei():
    """print"""
    num = int(input())
    for i in range(1, num+1):
        for j in range(1, num+1, 1):
            print(j, end=" ")
        print()
        i = i + 1

sequencei()
