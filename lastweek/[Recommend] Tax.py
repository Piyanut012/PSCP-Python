"""[Recommend] Tax"""

def main():
    """Input"""
    years = int(input())
    var_cc = int(input())
    tax = 0
    if var_cc > 1800:
        tax += (var_cc - 1800)*4 + 1200*1.5 + 600*0.5
    elif var_cc > 600:
        tax += (var_cc - 600)*1.5 + 600*0.5
    else:
        tax += var_cc*0.5

    if years >= 10:
        tax = tax*0.5
    elif years == 9:
        tax = tax*0.6
    elif years == 8:
        tax = tax*0.7
    elif years == 7:
        tax = tax*0.8
    elif years == 6:
        tax = tax*0.9

    print("%.2f" % tax)
main()
