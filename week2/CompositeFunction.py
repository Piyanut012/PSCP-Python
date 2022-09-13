"""CompositeFunction"""


def main():
    """Input"""
    variable = int(input())

    def function1(variable):
        """CompositeFunction g(x)"""

        variable = variable/2 + 1
        return variable

    def function2(variable):
        """CompositeFunction f(x)"""

        variable = variable * 2
        return variable

    print("%.2f" %function2(function1(variable)))
    print("%.2f" %function1(function2(variable)))

main()
