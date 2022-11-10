"""Impostor"""

import json
def main():
    """Input"""
    people = {}
    dead = []
    count = 0
    while True:
        txt = input()
        if txt == "Start":
            break
        color = json.loads(txt)
        people.update(color)
    while True:
        txt = input()
        if txt == "End":
            break
        dead_list = [txt, people[txt]]
        people.pop(txt)
        dead.append(dead_list)
    people = dict(sorted(people.items()))
    dead.sort(key=lambda i: i[0])
    for key in people:
        if people[key] == "Impostor":
            count += 1
    print(count, "Impostor Remains")
    print("***Alive***")
    for key in people:
        print(key, ":", people[key])
    print("***Dead***")
    for i in dead:
        print(i[0], ":", i[1])
main()
