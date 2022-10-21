"""PickThemAgain"""

def main():
    """Input"""
    num = input()
    check = False
    numlist = num.split()
    numlist.reverse()
    for i in numlist:
        if int(i)%3 == 0 or int(i)%5 == 0:
            check = True
            print(i)
    if check == False:
        print("Nope")
main()
