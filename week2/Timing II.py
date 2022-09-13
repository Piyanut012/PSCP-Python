"""Timing II"""


def main():
    """Input"""
    second = int(input())
    day = second//86400
    second = second%86400
    hrs = second//3600
    second = second%3600
    minute = second//60
    second = second%60
 
    if day < 10000:
        print("{x:04d}:{y:02d}:{z:02d}:{w:02d}".format(x=day, y=hrs, z=minute, w=second))
    else:
        print("ERR_:__:__:__")

main()
