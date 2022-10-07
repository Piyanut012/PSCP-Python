"""Restaurant"""


def main():
    """Input"""
    pay = float(input())
    promotion = float(input())
    discount = 1 - (float(input())/100)
    add_food = float(input())

    if pay + add_food >= promotion:
        pay_promotion = (pay + add_food) * discount
    else:
        pay_promotion = pay + add_food

    if pay >= promotion:
        pay = pay * discount

    diff = abs(pay_promotion - pay)
    if pay > pay_promotion:
        print("Yes %.3f" % diff)
    elif pay < pay_promotion:
        print("No %.3f" % diff)
    else:
        print("Yes")

main()
#pay 1
#promotion 1
#discount 1 or 0
#add_food 0
