"""TheFunctionWithin"""


def main():
    """Input"""
    var_a = float(input())
    var_b = float(input())
    var_c = float(input())
    var_d = float(input())
 
    def ft1(variable):
        """TheFunctionWithin f(x)"""
 
        variable = variable*2
        return variable
 
    def ft2(variable):
        """TheFunctionWithin g(x)"""
 
        variable = (3*variable**4)-(variable**3)+(2*variable**2)+10
        return variable
 
    def ft3(variable1, variable2, variable3):
        """TheFunctionWithin h(x)"""
 
        variable = (variable3 + variable1)**2 - (variable1 * variable2) + variable2**2
        return variable
 
    def ft4(variable1, variable2, variable3, variable4):
        """TheFunctionWithin i(x)"""
        var_back = (variable4**2-2*variable1*variable4+2*variable1)
        variable = (variable1**2+variable2**2-variable3**2)/var_back
        return  variable
 
    print(ft1(ft1(var_a)))
    print(ft2(ft1(var_a-var_b)))
    aaa = ft2(ft1(var_d**2))
    print(ft3(ft1(var_a+var_b), ft1(var_a+var_c), aaa))
    bbb = ft3((ft1(var_a+var_b)), ft1(var_a-var_c), ft2(ft1(var_d**2)))
    ccc = ft1(ft1(ft1(ft1(ft1(var_c)))))
    print(ft4(bbb, ft2(ft1(var_a-var_b)), ccc, var_d**8))

main()
