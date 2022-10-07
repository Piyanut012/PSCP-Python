"""Ball"""


def main(meter):
    """Input"""
    cmeter = meter*100
    check = True
    count = 0
    while check:
        cmeter = cmeter*3/5
        if cmeter < 1:
            break
        else:
            count += 1
    print(count)

main(float(input()))
