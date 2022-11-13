"""Binary"""

def main():
    """Input"""
    num = int(input())
    txt_2 = ""
    i = 0
    if num == 0:
        txt_2 = "0" + txt_2
    while 2**i <= num and num != 0:
        if num%(2**(i+1)) != 0:
            num -= 2**i
            txt_2 = "1" + txt_2
        else:
            txt_2 = "0" + txt_2
        i += 1
    print(txt_2)
main()
