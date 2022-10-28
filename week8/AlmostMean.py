"""AlmostMean"""

def main():
    """Input"""
    score = []
    data = []
    average = 0
    value = 0
    num = int(input())
    for _ in range(num):
        txt = input()
        data.append(txt)
        txt = txt.split("\t")
        score.append(float(txt.pop(1)))
    average = (sum(score))/num
    student_score = sorted(score)
    student_score.reverse()
    for i in student_score:
        if i <= average:
            value = score.index(i)
            print(data[value])
            break

main()
