n = int(input("Enter the number of numbers: "))
list1 = []

for i in range(n):
    a = float(input(f"{i+1}. Enter a number: "))
    list1.append(a)

print("Sum = ", sum(list1))
print("Average = ", sum(list1) / len(list1))
print("Min = ", min(list1))
print("Max = ", max(list1))
