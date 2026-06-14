num = int(input("Enter the number of students in the class: "))

list1=[]
for i in range(num):
    age = int(input(f"Enter the age of student {i+1}: "))
    list1.append(age)

avg = sum(list1)/len(list1)
print(f"Average of ages = {avg}")

count=0
for j in list1:
    if j>avg:
        count+=1
print(f"The number of students older than the class average: {count}")