"""AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""

def main():
    """Input"""
    message = input().replace(".", "")
    message_list = message.split()
    vowels = "AaEeIiOoUu"
    box = []
    count = 0
    for i in message_list:
        for txt in i:
            if txt in vowels:
                count += 1
        if count >= 2:
            box.append(i)
        count = 0
    box.sort()
    if box == []:
        print("Nope")
    else:
        for i in box:
            print(i)
main()
