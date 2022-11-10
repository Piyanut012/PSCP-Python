"""Olympic"""

def main():
    """Input"""
    num = int(input())
    box = []
    for _ in range(num):
        txt = input()
        txt = txt.split()
        box.append(txt)
    box.sort(key=lambda i: i[1], reverse=True)
    print(box)
main()
