"""Classify"""

def main():
    """Input"""
    dica = {}
    lsta = []
    ans = 0
    while True:
        txt = input()
        if txt == 'END':
            break
        dica[int(txt[:4])] = 0
        lsta.append(int(txt[:4]))
    for i in lsta:
        if i in dica.keys():
            dica[i] += 1
    dicaa = dict(sorted(dica.items()))
    for i, j in dicaa.items():
        if str(i)[:2] == ans:
            print('--', int(str(i)[2:]), j)
        else:
            print(str(i)[:2], int(str(i)[2:]), j)
        ans = str(i)[:2]

main()
