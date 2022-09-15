"""FOR!F-Ball"""

def main(key):
    """Input"""
    glass_1 = 1
    glass_2 = 0
    glass_3 = 0
    for i in key:
        if i == "A":
            glass_2, glass_1 = glass_1, glass_2
        elif i == "B":
            glass_3, glass_2 = glass_2, glass_3
        else:
            glass_3, glass_1 = glass_1, glass_3
    if glass_1 == 1:
        print(1)
    elif glass_2 == 1:
        print(2)
    else:
        print(3)

main(input())
