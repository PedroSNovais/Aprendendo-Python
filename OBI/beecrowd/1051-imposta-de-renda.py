n = float(input())
imposto = 0
if n <= 2000:
    imposto = 0
if n > 4500:
    i = (n - 4500)
    imposto += i * 0.28
    n -= i
if n > 3000:
    i = (n - 3000)
    imposto += i * 0.18
    n -= i
if n > 2000:
    i = (n - 2000)
    imposto += i * 0.08
    n -= i

if imposto == 0:
    print("Isento")
else:  
    print(f"R$ {imposto:.2f}")
