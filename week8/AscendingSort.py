"""AscendingSort"""

def main():
    """Input"""
    box = []
    for _ in range(5):
        box.append(int(input()))
    box.sort()
    for i in box:
        print(i)

main()
