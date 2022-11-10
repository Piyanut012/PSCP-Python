"""WordSequence I"""

def main():
    """Input"""
    message = input()
    for i in range(1, len(message)+1):
        print(message[:i])
main()
