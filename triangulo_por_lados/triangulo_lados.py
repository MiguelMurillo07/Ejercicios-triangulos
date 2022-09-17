# Ejercicio No. 3: Determinar si un triángulo es equilátero, isósceles o escaleno.


print("------------------------------------------")
print("----Determinar triángulo por sus lados----")
print("------------------------------------------")

# input

a = int(input("Ingrese el valor que quiera darle a A: "))
b = int(input("Ingrese el valor que quiera darle a B: "))
c = int(input("Ingrese el valor que quiera darle a C: "))

# processing and output

if (a<= 0 and b<=0 and c<=0):
    print("No es posible determinar un triángulo con los valores digitados. Por favor intente nuevamente.")
elif(a==b and a==c and b==c): 
    print("Las medidas dadas forman un triángulo Equilátero.")
elif(a != b and a !=c):
    print("Las medidas dadas forman un triángulo Escaleno.")
else:
    print("Las medidas dadas forman un triángulo Isósceles.")
