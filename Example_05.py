a=input("Enter an operator : ")
b=float(input("Enter the first number: "))
c=float(input("Enter the second number: "))

if a == "+" :
    d=b+c
elif a == "-" :
    d=b-c
elif a == "*" :
    d=b*c
elif a == "/" :
    d=b/c
elif a == "%" :
    d=b%c
elif a == "**" :
    d=b**c
elif a == "//" :
    d=b//c

print(f"{b} {a} {c} = {d}")
