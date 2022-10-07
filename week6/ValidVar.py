"""ValidVar"""


def main(num):
    """Input"""
    for _ in range(num):
        word = input()

        punctuation = True
        for i in word:
            if i.isalnum():
                continue
            elif i != "_":
                punctuation = False
                break
        dontspace = (word.strip()).find(" ") == -1
        dont_num_frist = word[0].isnumeric() == False
        reserved_word = ("if", "else", "elif", "while", "for", "True", "False", "continue",\
             "break", "return", "is", "in", "and", "or", "from", "as", "pass", "not", "def", "None")
        reserved = True
        for i in reserved_word:
            if i == word:
                reserved = False
                break
        if punctuation and dontspace and dont_num_frist and reserved:
            print("Valid")
        else:
            print("Invalid")

main(int(input()))

