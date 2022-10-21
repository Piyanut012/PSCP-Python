"""LastStand"""

import json
def main():
    """Input"""
    numlist = json.loads(input())
    for i in numlist:
        print(str(i)[-1])
main()
