"""Filter"""

import json
def main():
    """Input"""
    message = json.loads(input())
    box = message.copy()
    score = float(input())
    for key, value in message.items():
        if value < score:
            box.pop(key)
    if box == {}:
        print("Nope")
    box = dict(sorted(box.items()))
    for key, value in box.items():
        print(key + "	%.2f" % value)

main()
