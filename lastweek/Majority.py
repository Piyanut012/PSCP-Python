"""Majority"""


def main():
    """Input"""
    leader = int(input())
    select_people = int(input())
    dict_leader = {}
    for i in range(1, leader+1):
        dict_leader[i] = 0
    print(dict_leader)
    for _ in range(select_people):
        select = int(input())
        dict_leader[select] += 1
    if max(dict_leader.values()) >= int(select_people/2) + 1:
        print(*max(dict_leader, key=dict_leader.get), max(dict_leader.values()))
    else:
        print(0, max(dict_leader.values()))
main()
