"""Sequence VI"""
 
def sequencevi():
    """print"""
    num = int(input())
    end = 0
    for i in range(1, num+1):
        end += 1
        for j in range(1, end+1, 1):
            print(j, end=" ")
        i = i + 1
        print()

sequencevi()
