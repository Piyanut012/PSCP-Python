"""Median"""


def main():
    """Input"""
    num = int(input())
    numlist = []
    for _ in range(num):
        numz = int(input())
        numlist.append(numz)
    numlist.sort()
    if num%2 == 0:
        mid = ((numlist[int(num/2 - 1)])+(numlist[int(num/2)]))/2
        print("%.1f" % mid)
    else:
        print("%.1f" % (numlist[int(num//2)]))
main()
