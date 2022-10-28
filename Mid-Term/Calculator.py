"""Calculator"""

def main(num):
    """Input"""
    numz = ""
    for i in range(1, num+1):
        numz += str(i)
    if num == 1:
        print(1)
    else:
        print(len(numz) + num)

main(int(input()))
