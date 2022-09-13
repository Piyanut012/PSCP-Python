'''Quadrant'''
 
 
def main():
    """Input"""
    value1 = int(input())
    value2 = int(input())
 
    if value1 == 0 and value2 == 0:
        print("O")
    elif value1 > 0 and value2 > 0:
        print("Q1")
    elif value1 < 0 and value2 > 0:
        print("Q2")
    elif value1 < 0 and value2 < 0:
        print("Q3")
    elif value1 > 0 and value2 < 0:
        print("Q4")
    elif value2 == 0:
        print("X")
    elif value1 == 0:
        print("Y")

main()
