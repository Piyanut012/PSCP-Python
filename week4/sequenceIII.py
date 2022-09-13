"""Sequence III"""
def sequenceiii():
    """print"""
    num = int(input())
    jjj = 1
    num1 = num + 1
    for i in range(1, num+1):
        num1 += 1
        jjj += 1
        for j in range(jjj, num1):
            print(j, end=" ")
        i = i + 1
        print()

sequenceiii()
