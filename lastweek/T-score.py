"""T-score"""

def main():
    """Input"""
    total = int(input())
    full_score = int(input())
    list_score = [int(input()) for _ in range(total)]
    sum_score = sum(list_score)
    average = sum_score/total
    sum_score2 = [i**2 for i in list_score]
    s_d_ = ((total*(sum(sum_score2)) - sum_score**2)/(total**2 - total))**0.5
    if s_d_ == 0:
        return print("50\n" * total)
    t_score = [50 + 10*(score-average)/s_d_) for score in list_score]
    
main()
