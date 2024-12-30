def area_rectangle(l, L):
    return l*L

def bmi(weight, height):
    return weight/(height**(1/2))

def main():
    L = float(input("Enter the length of the rectangle: "))
    l = float(input("enter the larger of the rectangle: "))
    
    weight = float(input("Enter the weight of the Body Mass Index: "))
    height = float(input("Enter the height of the Body Mass Index: "))
    print(f"the area of this rectangle is {area_rectangle(l,L)}",
          f"the Body Mass Index is {round(bmi(weight, height),2)}", sep="\n")

if __name__ == "__main__":
    main()