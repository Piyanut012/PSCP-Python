'''SurprisingVote'''

def main():
    """Input"""
    totalpoint = float(input())
    highpoint = float(input())
   #distance = (totalpoint-highpoint)/2
    xxx = 0
    if highpoint * 2 < totalpoint:
        xxx = totalpoint - highpoint*2
    if highpoint - xxx > 2:
        print("Surprising")
    else:
        print("Not surprising")

main()
