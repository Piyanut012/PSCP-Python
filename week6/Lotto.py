"""Lotto"""


def main():
    """Input"""
    reward1 = input()
    reward2_back = input()
    reward3_front_1 = input()
    reward3_front_2 = input()
    reward3_back_1 = input()
    reward3_back_2 = input()
    lottery = input()

    if reward1 == "999999":
        rewardnear1_fornt = "000000"
        rewardnear1_back = "999998"
    elif reward1 == "000000":
        rewardnear1_fornt = "000001"
        rewardnear1_back = "999999"
    else:
        rewardnear1_fornt = "%06d" % (int(reward1) + 1)
        rewardnear1_back = "%06d" % (int(reward1) - 1)
    total = 0
    if lottery == reward1:
        total += 6000000
    if lottery[-2:] == reward2_back:
        total += 2000
    if lottery[:3] == reward3_front_1 or lottery[:3] == reward3_front_2:
        if reward3_front_1 == reward3_front_2:
            total += 8000
        else:
            total += 4000
    if lottery[-3:] == reward3_back_1 or lottery[-3:] == reward3_back_2:
        if reward3_back_1 == reward3_back_2:
            total += 8000
        else:
            total += 4000
    if lottery == rewardnear1_fornt or lottery == rewardnear1_back:
        total += 100000
    print(total)
main()
