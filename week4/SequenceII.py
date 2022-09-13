"""Sequence II"""
def sequenceii():
    """print"""
    num = int(input())
    for i in range(1, num+1):
        print(i**2, end=" ")
        i = i + 1

sequenceii()
