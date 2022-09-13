"""Donut"""

import math
def main():
    """Input"""
    price_donut = int(input())
    if_buy = int(input())
    giveaway = int(input())
    want_donut = int(input())
    get_donut = if_buy + giveaway

    price_promotion = math.ceil(want_donut/get_donut) * price_donut * if_buy
    price_normal = (want_donut//get_donut) * price_donut * if_buy + (want_donut%get_donut) \
         * price_donut

    if price_normal >= price_promotion:
        #Promotion
        price = price_promotion
        donut = math.ceil(want_donut/get_donut) * get_donut
    else:
        #Normal
        price = price_normal
        donut = (want_donut//get_donut) * get_donut + (want_donut%get_donut)

    print(price, donut)

main()
