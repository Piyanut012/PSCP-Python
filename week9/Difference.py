"""Difference"""

def main():
    """Input"""
    set1 = int(input())
    set2 = int(input())

    setnum1 = set()
    setnum2 = set()
    for _ in range(set1):
        setnum1.add(int(input()))
    for _ in range(set2):
        setnum2.add(int(input()))
    setdiff = setnum1.difference(setnum2)

    for i in sorted(setdiff):
        print(i, end=" ")

main()
