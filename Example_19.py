list1 = []

for i in range(5):
    x=input(f"Enter the name of participant number {i+1} : ")
    y=x.title()
    list1.append(y)

for j in list1:
    print(j)