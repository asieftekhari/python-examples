x = input("Enter a name : ")
y = x.lower()
if y == y[::-1]:
    print(f"'{x}' is Palindrome")
else:
    print(f"'{x}' isn't palindrome")