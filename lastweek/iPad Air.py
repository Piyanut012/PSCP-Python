"""iPad Air"""

def main():
    """Input"""
    color = input()
    capacity = input()
    wifi = input()

    colors = "Space Gray, Silver, Green, Rose Gold, Sky Blue "
    capacitys = "64, 256"
    wifis = "Wi-Fi, Wi-Fi + Cellular"
    if not color in colors or not capacity in capacitys or not wifi in wifis:
        return print("Not Available")
    if capacity == "64" and wifi == "Wi-Fi":
        print(19900)
    elif capacity == "64" and wifi == "Wi-Fi + Cellular":
        print(24400)
    elif capacity == "256" and wifi == "Wi-Fi":
        print(24900)
    elif capacity == "256" and wifi == "Wi-Fi + Cellular":
        print(29400)

main()
