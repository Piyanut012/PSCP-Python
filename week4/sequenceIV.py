"""Sequence IIII"""
def sequenceiiii():
    """print"""
    num = int(input())
    start = 1
    end = num
    for i in range(1, num+1):
        for j in range(start, end+1, 1):
            print(j, end=" ")
        start = start + num
        end = end + num
        i = i + 1
        print()

sequenceiiii()
