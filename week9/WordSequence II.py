"""WordSequence II"""


def main():
    """Input"""
    first_txt = list(input())
    mutation = list(input())
    def fuc():
        """Print"""
        print(*first_txt, sep="")
        for i in range(len(first_txt)):
            if i < len(mutation):
                first_txt.pop(i)
                first_txt.insert(i, mutation[i])
            else:
                first_txt.pop(len(mutation))
            print(*first_txt, sep="")

    if len(first_txt) >= len(mutation):
        fuc()
    else:
        fuc()
        for i in range(len(first_txt), len(mutation)):
            first_txt.insert(i, mutation[i])
            print(*first_txt, sep="")
main()
