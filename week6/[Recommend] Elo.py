"""Elo"""


def main():
    """Input"""
    var_ra = int(input())
    var_rb = int(input())
    var_e = input()
    def elo(first_r, second_r):
        """Elo"""
        elo_e = 1/(1+(10**((first_r-second_r)/400)))
        print("%.2f"%elo_e)

    if var_e == "A":
        elo(var_rb, var_ra)
    else:
        elo(var_ra, var_rb)

main()
