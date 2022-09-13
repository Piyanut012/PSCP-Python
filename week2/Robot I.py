'''Robot I'''
 
 
def main():
    """Input"""
    name = str(input())
    old = float(input())
 
    if old < 18:
        print(name + ", you can pass.")
    else:
        print(name + ", you shall not pass.")

main()
