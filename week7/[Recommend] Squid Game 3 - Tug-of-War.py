"""Squid Game 3 - Tug-of-War"""

def main():
    """Input"""
    total_a = 0
    total_b = 0
    for i in range(1, 21):
        if i <= 10:
            force_a = int(input())
            total_a += force_a
        else:
            force_b = int(input())
            total_b += force_b
    if total_a > total_b:
        print("B")
    elif total_b > total_a:
        print("A")
    else:
        print("AB")
main()
