n = int(input("Enter the length of the list: "))

list1 = []
for i in range(n):
    x = input(f"Enter item {i+1}: ")
    list1.append(x)

print(f"After deleting duplicate elements = {list(set(list1))}")
#-------Or--------
list2 = []
for j in list1:
    if j in list2:
        continue
    else:
        list2.append(j)
print(f"After deleting duplicate elements = {list2}")