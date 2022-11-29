"""[Recommend] Fever"""

def main():
    """Input"""
    temperature = float(input())

    if temperature >= 40:
        print("Very High Fever")
    elif temperature >= 39:
        print("High Fever")
    elif temperature >= 38:
        print("Mild Fever")
    else:
        print("No Fever")

main()
