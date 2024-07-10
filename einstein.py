def formula(masse):
    energie = int(masse)*300000000*300000000
    print(f"{energie}")
def main():
    m = int(input("enter the masse of your substance m: "))
    formula(m)
main()