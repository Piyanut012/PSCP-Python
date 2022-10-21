"""Tuple's Sad life"""

def main():
    """Input"""
    num = input()
    check = input()
    box = tuple(num.split())
    count = box.count(check)
    index = box.index(check)
    for _ in range(count):
        print(("%d " % index) * count)
main()
