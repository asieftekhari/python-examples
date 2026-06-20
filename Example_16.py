set1 = {1, 59, "Yes", 35, " ", "No", 1, 85, "true"}
set2 = {"Yes", "False", 59, "h", 85}
copyset1=set1.copy()

set1.add("delete")
print(f"set1 + {{delete}} = {set1}")

set1.remove("No")
print(f"set1 - {{No}} = {set1}")

print(f"Union of set1 and set2 = {set1.union(set2)}")
print(f"Intersection of set1 and set2 = {copyset1.intersection(set2)}")