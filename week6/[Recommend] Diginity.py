"""Diginity"""


def main():
    """Input"""
    while True:
        num = input()
        total_num = 0
        if num == "0":
            break
        n_num = len(num)
        if n_num > 1:
            while True:
                for i in num:
                    total_num += int(i)
                if len(str(total_num)) <= 1:
                    print(total_num)
                    break
                else:
                    num = str(total_num)
                    total_num = 0
        else:
            print(num)

main()

