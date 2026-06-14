n = int(input("Enter the number of key-value pairs in the dictionary: "))
dec1 = {}
for i in range(n):
    key1 = input(f"key ({i+1}) = ")
    value1 = input(f"value ({i+1}) = ")
    dec1[key1]=value1

key2=input("Enter the key you want to find: ")
if key2 in dec1:
    print(f"Yes, {key2} is in keys.")
else:
    print(f"No, {key2} isn't in keys.")