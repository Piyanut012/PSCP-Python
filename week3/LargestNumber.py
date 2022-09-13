"""LargestNumber"""


def main():
    """Inputt"""
    num_1 = input()
    num_2 = input()
    num_3 = input()
    set_1 = int(num_1 + num_2 + num_3)
    set_2 = int(num_1 + num_3 + num_2)
    set_3 = int(num_2 + num_1 + num_3)
    set_4 = int(num_2 + num_3 + num_1)
    set_5 = int(num_3 + num_2 + num_1)
    set_6 = int(num_3 + num_1 + num_2)
    def sor(set1, set2, set3):
        """Sort"""
        if set1 > set2:
            set2, set1 = set1, set2
        if set2 > set3:
            set3, set2 = set2, set3
        if set1 > set2:
            set2, set1 = set1, set2
        if set2 > set3:
            set3, set2 = set2, set3
        high = set3
        return high

    info1 = sor(set_1, set_2, set_3)
    info2 = sor(set_4, set_5, set_6)
    if info1 > info2:
        print(info1)
    else:
        print(info2)

main()
