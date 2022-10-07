"""Nearer"""


def main():
    """Input"""
    alicex = int(input())
    bobx = int(input())
    icex = int(input())
    if abs(icex - alicex) > abs(icex - bobx):
        print("Bob", abs(icex - bobx))
    elif abs(icex - alicex) < abs(icex - bobx):
        print("Alice", abs(icex - alicex))
    else:
        print("Sundaes", abs(icex - alicex))
main()
