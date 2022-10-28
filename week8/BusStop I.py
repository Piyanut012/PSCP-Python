"""BusStop I"""

def main():
    """Input"""
    amount = int(input())
    count = int(input())
    list_str = []
    lsit_int = []
    yay = 0
    for _ in range(count):
        bus = input().split()
        list_str.append(bus)
    list_str.sort(key=lambda i: int(i[0]))
    for i in list_str:
        busstop = int(i[0])
        if len(lsit_int) != 0:
            lsit_int2 = lsit_int.copy()
            for arrive in lsit_int:
                if arrive == busstop:
                    lsit_int2.remove(arrive)
                    yay += 1
            lsit_int = lsit_int2
        for j in range(1, len(i)):
            if len(lsit_int) == amount:
                break
            if busstop < int(i[j]):
                lsit_int.append(int(i[j]))
    print(yay)

main()
