"""Cha Cha Cha"""

import math
def main():
    """Input"""
    num = int(input())
    total = 0
    for _ in range(0, num):
        hrs = math.ceil(float(input()))
        total += hrs * 8720
    print(total)
main()
