def cm_to_ft():
    cm = float(input("Enter value in cm: "))
    return cm * 0.0328084


def km_to_miles():
    km = float(input("Enter value in km: "))
    return km * 0.621371


def usd_to_bdt():
    usd = float(input("Enter value in USD: "))
    return usd * 122.28


def main():
    state = True
    print("""
        Menu:
            1. cm to ft
            2. km to miles
            3. USD to BDT
            4. exit
         """)
    while state:
        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            print(f"Value In CM: {cm_to_ft():.3f}")
        elif choice == 2:
            print(f"Value in miles: {km_to_miles():.3f}")
        elif choice == 3:
            print(f"Value in BDT: {usd_to_bdt():.3f}")
        elif choice == 4:
            state = False
        else:
            print("Invalid choice")


main()
