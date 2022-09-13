"""Triangle I"""

def main():
    """Input"""
    stick1 = float(input())
    stick2 = float(input())
    stick3 = float(input())
 
    while_check = True
    while while_check:
        while_check = False
        if stick1 > stick2:
            while_check = True
            stick1, stick2 = stick2, stick1
        if stick2 > stick3:
            while_check = True
            stick2, stick3 = stick3, stick2
 
    if stick1**2 + stick2**2 == stick3**2:
        print("Yes")
    elif stick1**2 + stick2**2 <= stick3**2+0.01 and stick1**2 + stick2**2 >= stick3**2-0.01:
        print("Yes")
    else:
        print("No")

main()
