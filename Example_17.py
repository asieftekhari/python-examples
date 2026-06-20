x = int(input("Enter the ages of employees (range: 10 to 90). To stop, enter -1 :"))
list1 = [x]

while x!= -1:
    x = int(input("Enter the ages of employees (range: 10 to 90). To stop, enter -1 :"))
    list1.append(x)

print("max = ", max(list1))