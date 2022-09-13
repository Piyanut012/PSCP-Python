"""BootSequence"""

def main():
    """output"""
    num = int(input())
    for i in range(1, num+1):
        if i == num:
            print(i)
        else:
            print(i, "", sep="_", end="")

main()
