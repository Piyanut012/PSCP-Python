"""Kangaroo"""

def main():
    """Input"""
    kangaroo_1 = int(input())
    kangaroo_2 = int(input())
    kangaroo_3 = int(input())
    distace = max(abs(kangaroo_1 - kangaroo_2)-1, abs(kangaroo_2 - kangaroo_3)-1)
    print(distace)

main()
