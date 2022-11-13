"""CaesarV1"""

def main():
    """Input"""
    num = int(input())
    message = input()
    txt_print = ""
    for i in message:
        if not i.isalpha():
            txt_print += i
            continue
        if num < 0:
            txt = ord(i) + num%(-26)
        else:
            txt = ord(i) + num%26
        if i.isupper():
            if txt < 65:
                txt = 26 + txt
            elif txt > 90:
                txt = txt - 26
        else:
            if txt < 97:
                txt = 26 + txt
            elif txt > 122:
                txt = txt - 26
        txt_print += chr(txt)
    print(txt_print)
main()
