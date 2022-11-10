"""All_Primes"""

def main():
    """Input"""
    num = int(input())
    count = 0
    countz = 0
    for i in range(2, num+1):
        for j in range(2, i+1):
            if i%j == 0:
                count += 1
            if count >= 2:
                break
        if count < 2 and count != 0:
            countz += 1
        count = 0
    print(countz)
main()
