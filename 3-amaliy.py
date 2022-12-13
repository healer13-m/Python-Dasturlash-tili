a=int(input("a="))
b=int(input("b="))
if a%2!=0 and b%2!=0:
    print(f"{a} , {b} kritilgan sonlar har ikkisi ham toq")
elif a%2!=0 or b%2!=0:
    print(f"{a} , {b} kritilgan sonlardan biri toq")
elif a%2==0 and b%2==0:
    print(f"{a} , {b} kritilgan sonlar har ikkisi ham juft")

