"""Colors"""

def main():
    """Input"""
    color_1 = input()
    color_2 = input()
    colors = "Red Yellow Blue"

    if not color_1 in colors or not color_2 in colors:
        return print("Error")
    elif color_1 == color_2:
        return print(color_1)

    if (color_1 == "Red" and color_2 == "Yellow") or (color_1 == "Yellow" and color_2 == "Red"):
        print("Orange")
    elif (color_1 == "Red" and color_2 == "Blue") or (color_1 == "Blue" and color_2 == "Red"):
        print("Violet")
    else:
        print("Green")
main()
