"""BMI"""


def main(name, weight, tall):
    """Input"""
    bmi = weight/(tall/100)**2
    print(name + "\'s  BMI = %.2f" %bmi)


main(str(input()), float(input()), float(input()))
main(str(input()), float(input()), float(input()))
main(str(input()), float(input()), float(input()))
main(str(input()), float(input()), float(input()))
main(str(input()), float(input()), float(input()))
