"""RemoveTag"""

def main():
    """Input"""
    box = []
    txt = input()
    txt = txt.split("<")
    for i in txt:
        var = i.find(">")
        if var == -1:
            var_list = i.split()
            box.extend(var_list)
        else:
            var_list = i[var+1:]
            var_list = var_list.split()
            box.extend(var_list)
    print(box)
main()
