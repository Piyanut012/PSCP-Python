"""PhoneNumber"""


def main():
    """Input"""
    num_phone = input()
    country = input()
    if country == "International":
        num_phone = "+66" + num_phone[1:]
    print(num_phone[:-8], num_phone[-8:-4], num_phone[-4:])

main()

