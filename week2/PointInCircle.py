"""PointInCircle"""


def main():
    """Input"""
    valuex = float(input())
    valuey = float(input())
    valuer = float(input())
    valuexn = float(input())
    valueyn = float(input())
 
    distance = ((valuex-valuexn)**2 + (valuey-valueyn)**2)**0.5
 
    if distance > valuer:
        print("False")
    else:
        print("True")

main()
