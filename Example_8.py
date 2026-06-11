a =input("Enter the first positive integer: ")
while True:
    if a.isdigit():
        break
    else:
        print("Try again!")
        a = input("please enter the first positive integer: ")
print(("--------------------------------------"))
b = input("Enter the second positive integer: ")
while True:
    if b.isdigit():
        break
    else:
        print("Try again!")
        b = input("please enter the second positive integer: ")
print(("--------------------------------------"))
if int(a) >= int(b) :
    print(f"The maximum is {int(a)}")
else:
    print(f"The maximum is {int(b)}")