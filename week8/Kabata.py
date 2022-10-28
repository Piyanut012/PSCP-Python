"""Kabata"""

def main():
    """Input"""
    num = int(input())
    box = []
    for _ in range(num):
        kabata = input()
        kabata = kabata.replace("baka", "e")
        kabata = kabata.replace("bakka", "")
        kabata = kabata.replace("ta", "")
        kabata = kabata.replace("ka", "")
        kabata = kabata.replace("ba", "")
        if kabata == "":
            box.append("yes")
        else:
            box.append("no")
    for i in box:
        print(i)
main()
