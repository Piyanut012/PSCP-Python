"""Olympic"""

def main():
    """Input"""
    num = int(input())
    box = []
    before = 0
    pos = 0
    for _ in range(num):
        txt = input()
        txt = txt.split()
        box.append(txt)
    box.sort(key=lambda i: int(i[1]) + int(i[2]) +int(i[3]), reverse=True)
    box.sort(key=lambda i: i[0])
    box.sort(key=lambda i: (int(i[1]), int(i[2]), int(i[3])), reverse=True)

    def pirnt(var, var_num):
        """Print"""
        print(var, end=" ")
        for j in box[var_num]:
            print(j, end=" ")
        print(total)

    for i in range(num):
        total = int(box[i][1]) + int(box[i][2]) +int(box[i][3])
        check = int(box[i][1] + box[i][2] + box[i][3])
        if before == check:
            pirnt(pos, i)
        else:
            pirnt(i+1, i)
            pos = i+1
        before = check
main()
