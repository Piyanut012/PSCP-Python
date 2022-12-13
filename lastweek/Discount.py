"""Discount"""

def main():
    """Input"""
    price = input()
    list_book = []
    while price != "ENTER":
        list_book.append(int(price))
        price = input()
    list_book.sort()
    if len(list_book) < 20:
        free = min(2, len(list_book) // 6)
    else:
        free = len(list_book) // 5
    print(sum(list_book[free:]))
main()
