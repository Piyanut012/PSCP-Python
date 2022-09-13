"""WeightStation"""

def main():
    """Input"""
    average = float(input())
    weight1 = float(input())
    weight2 = float(input())
    weight3 = float(input())
    weight4 = average*4-weight1-weight2-weight3
    average_down = average/2
    average_up = average/2 + average
 
    if weight1+weight2+weight3+weight4 >= 15000:
        print("Overweight")
    elif weight1 <= average_down or weight1 >= average_up:
        print("Unbalance")
    elif weight2 <= average_down or weight2 >= average_up:
        print("Unbalance")
    elif weight3 <= average_down or weight3 >= average_up:
        print("Unbalance")
    elif weight4 <= average_down or weight4 >= average_up:
        print("Unbalance")
    else:
        print("Pass %.2f" % weight4)

main()
