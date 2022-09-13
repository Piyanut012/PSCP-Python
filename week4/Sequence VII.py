"""Sequence VII"""

def sequencevii():
    """print"""
    num = int(input())
    endz = 0
    for i in range(1, num*2):
        if i <= num:
            endz += 1
            for j in range(1, endz+1, 1):
                print(j, end=" ")
        elif i > num:
            endz -= 1
            for j in range(1, endz+1, 1):
                print(j, end=" ")
        i = i + 1
        print()

sequencevii()
