"""Coke"""

def main():
    """Input"""
    original_cost = int(input())
    promotion_caps_of_coke = int(input())
    special_cost = int(input())
    amount = int(input())

    price, caps_of_coke = original_cost, 0
    pay = 0
    while amount > 0:
        caps_of_coke += 1
        pay += price
        price = original_cost
        if promotion_caps_of_coke == 0:
            pay = original_cost * amount
            break
        if caps_of_coke == promotion_caps_of_coke:
            price = special_cost
            caps_of_coke = 0
        amount -= 1
    print(pay)


main()
