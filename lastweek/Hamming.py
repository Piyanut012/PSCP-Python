"""Hamming"""

def main():
    """Input"""
    txt_1 = input()
    txt_2 = input()
    count = 0
    for i in range(len(txt_1)):
        if txt_1[i] != txt_2[i]:
            count += 1
    print(count)
main()
