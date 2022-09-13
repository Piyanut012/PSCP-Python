"""Stepper II"""
def stepper():
    """output"""
    numa = int(input())
    numb = int(input())
    if numa <= numb:
        for i in range(numa, numb+1, 1):
            print(i)
    elif numa > numb:
        for i in range(numa, numb-1, -1):
            print(i)

stepper()
