"""EuclideanDistance2D"""


def main():
    """Input"""
    value_q1 = float(input())
    value_q2 = float(input())
    value_p1 = float(input())
    value_p2 = float(input())
 
    print(((value_q1-value_p1)**2 + (value_q2-value_p2)**2)**0.5)

main()
