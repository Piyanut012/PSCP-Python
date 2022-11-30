"""ISBN"""

def main():
    """Input"""
    message = input().replace("-", "")
    div = 10
    total = 0
    for i in range(len(message)-1):
        if message[i] == "X":
            var_i = 10
        else:
            var_i = int(message[i])
        total += div*var_i
        div -= 1
    var = (-total)%11
    if message[-1] == "X":
        last_num = 10
    else:
        last_num = int(message[-1])
    if var == last_num:
        print("Yes")
    elif var == 10:
        var = "X"
        print("No", var)
    else:
        print("No", var)
main()
