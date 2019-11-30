a = int(input("Masukan bilangan A: "))
b = int(input("Masukan bilangan B: "))
c = int(input("Masukan bilangan c: "))

if a > b and a > c:
        terbesar = a
else:
    if b > c and b > a:
         terbesar = b
    if c > a and c > b:
        terbesar = c

print("Jadi Bilangan yang Terbesar Adalah :",terbesar)