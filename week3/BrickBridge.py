"""BrickBridge"""

def main():
    """Input"""
    small = int(input())
    big = int(input())
    goal = int(input())
    big_5 = big * 5
 
    if small + big_5 < goal:
        print(-1)
    else:
        if goal/big_5 >= 1:
            small_use = goal - big_5
            print(small_use)
        else:
            small_use = goal % 5
            if small_use > small:
                print(-1)
            else:
                print(small_use)

main()
