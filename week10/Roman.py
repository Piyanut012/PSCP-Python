"""Roman"""

def main(txt):
    """Input"""
    symbolvalue = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    last = 0
    list_num = [symbolvalue.get(i) for i in txt]
    list_num.reverse()
    for num in list_num:
        if last <= num:
            total += num
        else:
            total -= num
        last = num
    print(total)
main(input())
