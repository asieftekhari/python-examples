a=input("Enter a three-digit number (from 100 to 999): ")
a1=int(a)

while a1<100 or a1>999:
    a = input("Errore!\nPlease enter a three-digit number (from 100 to 999): ")
    a1 = int(a)

print(2*int(a[::-1]))