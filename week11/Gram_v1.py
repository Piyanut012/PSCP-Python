"""Gram_v1"""

def main():
    """Input"""
    message = input()
    txt = {}
    for i in range(len(message)):
        if i != len(message)-1:
            gram = message[i] + message[i+1]
            if gram not in txt:
                txt[gram] = 0
            txt[gram] += 1
    txt_list = list(txt.keys())
    var_list = list(txt.values())
    print(txt_list[var_list.index(max(var_list))])
    print(max(var_list))
main()
