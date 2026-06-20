age = int(input("1. Enter the ages of students (range: 10 to 90). To stop, enter -1 :"))
list1 = [age]

i=2
while age != -1:
    age = int(input(f"{i}. Enter the ages of students (range: 10 to 90). To stop, enter -1 :"))
    if age in list1:
        print("Try again")
        continue
    else:
        list1.append(age)
    i+=1

list1.sort()
print(f"The maximum = {list1[-1]}")
print(f"The second maximum = {list1[-2]}")