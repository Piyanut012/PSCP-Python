"""RockPaperScissor"""

def main(message):
    """Input"""
    key = ""
    point_a = 0
    point_b = 0
    for i in message:
        key = key + i
        if len(key) == 2:
            if key == "RS" or key == "PR" or key == "SP":
                point_a += 1
            elif key == "SR" or key == "RP" or key == "PS":
                point_b += 1
            key = ""
    if point_a > point_b:
        print("A win %d-%d" % (point_a, point_b))
    elif point_b > point_a:
        print("B win %d-%d" % (point_b, point_a))
    else:
        print("DRAW %d" % (point_a))

main(input())
