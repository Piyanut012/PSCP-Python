"""Flatten"""

import json
def main(num_list: list):
    """Input"""
    ans_list = []
    for i in num_list:
        if isinstance(i, list):
            ans_list += main(i)
        else:
            ans_list.append(i)
    ans_list.sort(reverse=True)
    return ans_list
print(main(json.loads(input())))
