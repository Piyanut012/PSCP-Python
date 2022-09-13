"""SumOfNumber"""

def main():
    """output"""
    total = int(input())
    total_num = 0
    input_while = True
    while input_while:
        if total_num == total:
            break
        num = int(input())
        if total_num != total and num != -1:
            total_num = total_num + num
        else:
            input_while = False

    print(total_num)

main()
