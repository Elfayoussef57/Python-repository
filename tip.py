def main():
    dollars = float(input("How much was the meal? ").replace("$",""))
    percent = percent_to_float(input("What percentage would you like to tip? ").replace("%",""))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def percent_to_float(p):
    percent = float(p)/100
    return percent
main()