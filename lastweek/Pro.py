"""Pro"""

def main():
    """Input"""
    pro_person = int(input())
    price_person = int(input())
    price = int(input())
    person = int(input())

    check_pro = int(person/pro_person)
    if check_pro >= 1:
        person -= (pro_person-price_person)*check_pro
    print(price*person)
main()
