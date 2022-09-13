'''GraderMachine'''

def main():
    """Input"""
    start = int(input())
    end = int(input())
    total = 0
    print("pass : ", end='')
    if start < end:
        for num_even in range(start, end+1, 1):
            if num_even % 2 == 0:
                print(num_even, end=' ')
                total = total + num_even
    else:
        for num_even in range(start, end-1, -1):
            if num_even % 2 == 0 and num_even != 0:
                print(num_even, end=' ')
                total = total + num_even
    print("\nSum : %d" % total)

main()
