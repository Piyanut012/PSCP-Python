"""Grade III"""

def main(subject):
    """Input"""
    i = 1
    grade = 0
    while i <= subject:
        score = float(input())
        if score >= 95 and score <= 100:
            grade += 4/subject
        elif score >= 90 and score < 95:
            grade += 3.5/subject
        elif score >= 85 and score < 90:
            grade += 3/subject
        elif score >= 80 and score < 85:
            grade += 2.5/subject
        elif score >= 75 and score < 80:
            grade += 2/subject
        elif score >= 70 and score < 75:
            grade += 1.5/subject
        elif score >= 65 and score < 70:
            grade += 1/subject
        elif score >= 60 and score < 65:
            grade += 0.5/subject
        else:
            grade += 0
        i += 1
    grade = int(grade * 100) / 100
    print("%.2f" % grade)

main(int(input()))
