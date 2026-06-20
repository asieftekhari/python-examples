x = input("Enter a word: ")
u1 = 0
l1 = 0
for i in x:
    if i.isupper():
        u1 += 1
    else:
        l1 += 1

if u1 > l1:
    print(x.upper())
else:
    print(x.lower())