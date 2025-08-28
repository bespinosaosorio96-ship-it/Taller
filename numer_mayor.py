import os

os.system

print("numeros mayores")

a=int (input("ingrese el primer numero:"))
b=int (input("ingrese el segundo numero:"))
c= int (input("ingrese el tercer numero:"))

if a>b and b>c:
  print (f"numero mayor es : {a}")
elif b>a and a>c:
  print (f"numero mayor es: {b}")
elif a==b and b==c:
    print("Los numeros son iguales")
else:
   print(f"El numero mayor es : {c}")

