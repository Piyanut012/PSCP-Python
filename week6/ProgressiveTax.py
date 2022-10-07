"""ProgressiveTax"""


def main(income):
    """Input"""
    range_1 = 7500
    range_2 = 20000
    range_3 = 37500
    range_4 = 50000
    range_5 = 250000
    range_6 = 600000
    total = 0

    if income <= 150000:
        total = 0
    elif income > 150000 and income <= 300000:
        total += (income - 150000) * 0.05
    elif income > 300000 and income <= 500000:
        total += (income - 300000) * 0.1 + range_1
    elif income > 500000 and income <= 750000:
        total += (income - 500000) * 0.15 + range_1 + range_2
    elif income > 750000 and income <= 1000000:
        total += (income - 750000) * 0.2 + range_1 + range_2 + range_3
    elif income > 1000000 and income <= 2000000:
        total += (income - 1000000) * 0.25 + range_1 + range_2 + range_3 + range_4
    elif income > 2000000 and income <= 4000000:
        total += (income - 2000000) * 0.3 + range_1 + range_2 + range_3 + range_4 + range_5
    else:
        total += (income - 4000000) * 0.35 + range_1+range_2+range_3+range_4+range_5+range_6
    print(int(total))

main(float(input()))

