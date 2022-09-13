"""DataSpike"""


def main():
    """Input"""
    total = 0
    def funcn_data(begift):
        """Data"""
        gift = int(input())
        if gift > begift:
            begift = gift
        return begift

    total = funcn_data(total)
    total = funcn_data(total)
    total = funcn_data(total)
    total = funcn_data(total)
    total = funcn_data(total)
    total = funcn_data(total)
    total = funcn_data(total)
    total = funcn_data(total)
    print(total)

main()
