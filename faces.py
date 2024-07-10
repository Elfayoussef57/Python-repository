def convert(enter):
    enter = enter.replace(":)","🙂").replace(":(","☹️")
    print(enter)
def main():
    name = input("enter a sentance that finish with ':)' or ':(' : ")
    convert(name)
main()