x=int(input("Enter your age : "))

if x>0 and x<6:
    print("Child")
elif x>=6 and x<10:
    print("Young Child")
elif x>=10 and x<14:
    print("Pre-teen")
elif x>=14 and x<24:
    print("Youth")
elif x>=24 and x<40:
    print("Adult")
elif x>=40:
    print("Middle-aged")