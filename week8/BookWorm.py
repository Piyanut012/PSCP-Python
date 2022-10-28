"""BookWorm"""

def main():
    """Input"""
    num = int(input())
    count = 0
    box = []
    for _ in range(num):
        read_time = float(input())
        book = int(input())
        for _ in range(book):
            books = float(input())
            box.append(books)
        box.sort()
        for i in range(len(box)):
            if sum(box[:i+1]) > read_time:
                break
            count += 1
        print(count)
        count = 0
        box = []

main()
