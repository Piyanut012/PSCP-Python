"""Heron of Alexandria"""


def main(var_a, var_b, var_c):
    """Input"""
    var_s = (var_a + var_b + var_c)/2
    area = (var_s*(var_s-var_a)*(var_s-var_b)*(var_s-var_c))**0.5
    print("%.3f" % area)

main(float(input()), float(input()), float(input()))
