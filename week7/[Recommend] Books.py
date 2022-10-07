"""Book"""

import math


def main(book, page, page_up, page_down):
    """Input"""
    day = 0
    page_read = 0
    while book != 0:
        page_read += math.ceil((page_up + day)/(page_down + day) * page)
        if page_read > page:
            page_read = 0
            book -= 1
        elif page_read == page:
            day = day + book
            break
        day += 1
    print(day)

main(int(input()), int(input()), int(input()), int(input()))

