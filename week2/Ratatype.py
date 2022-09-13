"""Ratatype"""


def main():
    """Input"""
    one = "In Deep Learning, a Convolutional Neural Network (CNN) is a class of Deep "\
        "Neural Networks, most commonly applied to analyzing visual imagery."
    two = "\"Two things are infinite: the universe and human stupidity; "\
        "and I'm not sure about the universe\". - Albert Einstein"
    three = "Statistics is the discipline that concerns the collection, organization, "\
        "displaying, analysis, interpretation and presentation of data."
    four = "The backslash (\\) is a typographical mark used mainly in computing and is the "\
        "mirror image of the common slash (/). It is sometimes called \"escape character\"."
 
    value1 = int(input())
    if value1 == 1:
        print(one)
    elif value1 == 2:
        print(two)
    elif value1 == 3:
        print(three)
    elif value1 == 4:
        print(four)

main()
