"""ฉันจะเป็น Saitama ให้ได้เลย"""

import math
def main():
    """Input"""
    push_ups_want = int(input())
    sit_up_want = int(input())
    sit_ups_want = int(input())
    run_want = int(input())
    push_ups = int(input())
    sit_up = int(input())
    run = int(input())
    sit_ups = int(input())

    push_ups = math.ceil(push_ups_want/push_ups)
    sit_up = math.ceil(sit_up_want/sit_up)
    sit_ups = math.ceil(sit_ups_want/sit_ups)
    run = math.ceil(run_want/run)

    box = (push_ups, sit_up, sit_ups, run)
    box = sorted(box, reverse=True)
    for i in box:
        print(i)
        break


main()

