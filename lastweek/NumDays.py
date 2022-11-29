"""NumDays"""

def main():
    """Input"""
    days_1 = int(input())
    months_1 = int(input())
    days_2 = int(input())
    months_2 = int(input())
    list_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if days_1 > list_months[months_1-1] or days_2 > list_months[months_2-1]:
        return print("Impossible")
    print(abs(sum(list_months[:months_1-1]) + days_1 - (sum(list_months[:months_2-1]) + days_2)))
main()
