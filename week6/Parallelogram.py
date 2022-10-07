"""Parallelogram"""


def main():
    """Input"""
    word = input()
    nword = len(word)
    #ครึ่งแรก
    for i in range(1, nword+1):
        print(" " * (nword - i), end="")
        print(word[:i])
    #ครึ่งหลัง
    for i in range(1, nword+1):
        print(word[i:])
main()
