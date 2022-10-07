"""iPhone 13 Again"""


def main():
    """Input"""
    model = input()
    var = input()
    def mini():
        """iPhone"""
        if var == "128 GB":
            print(25900)
        elif var == "256 GB":
            print(29900)
        elif var == "512 GB":
            print(37900)
        else:
            print("Not Available")
    def normal():
        """iPhone"""
        if var == "128 GB":
            print(29900)
        elif var == "256 GB":
            print(33900)
        elif var == "512 GB":
            print(41900)
        else:
            print("Not Available")
    def pro():
        """iPhone"""
        if var == "128 GB":
            print(38900)
        elif var == "256 GB":
            print(42900)
        elif var == "512 GB":
            print(50900)
        elif var == "1 TB":
            print(58900)
        else:
            print("Not Available")
    def promax():
        """iPhone"""
        if var == "128 GB":
            print(42900)
        elif var == "256 GB":
            print(46900)
        elif var == "512 GB":
            print(54900)
        elif var == "1 TB":
            print(62900)
        else:
            print("Not Available")

    if model == "iPhone 13 mini":
        mini()
    elif model == "iPhone 13":
        normal()
    elif model == "iPhone 13 Pro":
        pro()
    elif model == "iPhone 13 Pro Max":
        promax()
    else:
        print("Not Available")
main()
