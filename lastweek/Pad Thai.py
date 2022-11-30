"""Pad Thai"""

def main():
    """Input"""
    all_pad_thai = "Pad Thai Sauce,Tofu,Pickle Turnip,Shrimp,Bean Sprouts,Noodle,\
Chives,Lime,Egg,Oil,Peanuts"
    all_pad_thai = all_pad_thai.split(",")
    taste = "Sweet,Sour,Salty"
    taste = taste.split(",")
    set_var = 0
    dict_1 = dict.fromkeys(all_pad_thai, set_var)
    dict_2 = dict.fromkeys(taste, set_var)
    taste_other = False
    while True:
        var = input()
        if var == "Cook":
            break
        if var in dict_1.keys() and dict_1[var] == 0:
            dict_1[var] += 1
        elif not var in dict_1.keys():
            return print("This is not Pad Thai!!!")
    while True:
        var = input()
        if var == "End":
            break
        if var in dict_2.keys() and dict_2[var] == 0:
            dict_2[var] += 1
        elif not var in dict_2.keys():
            taste_other = True
    if 0 in dict_1.values():
        print("This is bad!")
    elif not 0 in dict_1.values() and (0 in dict_2.values() or taste_other):
        print("Not Bad...")
    elif not 0 in dict_1.values() and not 0 in dict_2.values():
        print("Delicious!")
main()
