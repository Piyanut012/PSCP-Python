"""Inverter"""

def main():
    """Input"""
    print("".join(['0' if i == "1" else '1' for i in list(input())]).lstrip("0"))
main()
