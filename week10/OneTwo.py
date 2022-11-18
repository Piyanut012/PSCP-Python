"""OneTwo"""

def main():
    """Input"""
    num = int(input())
    if num == 1 or num == 2:
        return print(num)
    last1 = "21"
    last2 = "2"
    for _ in range(num-3):
        txt = last1 + last2
        last1, last2 = txt, last1
    print(txt)
main()
