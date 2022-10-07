"""BigFrame"""


def main(num):
    """Input""" 
    var_1 = input().strip()
    var_2 = input().strip()
    var_3 = input().strip()
    var_4 = input().strip()
    var_5 = input().strip()
    box = (var_1, var_2, var_3, var_4, var_5)
    width = max(len(var_1), len(var_2), len(var_3), len(var_4), len(var_5))
    print("*" * (width+4))
    for i in box:
        print("* " + i + (" " * (width - len(i))) + " *")
    print("*" * (width+4)) 

main(int(input()))

