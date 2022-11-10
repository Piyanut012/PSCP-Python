"""Duplicate I"""

def main():
    """Input"""
    num1 = int(input())
    num2 = int(input())
    group1 = set()
    group2 = set()
    for _ in range(num1):
        group1.add(int(input()))
    for _ in range(num2):
        group2.add(int(input()))
    same = group1.intersection(group2)
    if same == set():
        print("Nope")
    else:
        same = sorted(same, reverse=True)
        print(*same, sep="\n")
main()
