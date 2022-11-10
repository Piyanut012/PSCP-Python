"""LetterFrequency"""

def main():
    """Input"""
    message = input().lower()
    txt = ""
    box = {}
    for i in message:
        if i.isalpha() and i != " ":
            txt += i
    for i in txt:
        if i in box:
            continue
        count = txt.count(i)
        box[i] = count
        count = 0
    box = sorted(box, key=lambda i: box[i])
    print(box[-1])
main()
