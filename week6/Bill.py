"""Bill"""


def main():
    """Input"""
    price = int(input())
    service = 0.1*price
    if service < 50:
        service = 50
    elif service > 1000:
        service = 1000
    withtax = (price + service)*1.07
    print("%.2f"%(withtax))
main()
