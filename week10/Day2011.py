"""Day2011"""

def main():
    """Input"""
    day = int(input())
    month = int(input())
    days_list = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    months = []
    for i in range(1, 13): #create months
        if i == 4 or i == 6 or i == 9 or i == 11:
            months.append(30)
        elif i == 2:
            months.append(28)
        else:
            months.append(31)
    day_all = sum(months[:month-1]) + day
    print(days_list[day_all%7 - 1])
main()
