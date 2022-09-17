# Ejercicio No.3: Determinar si un triángulo es obtuso, recto o agudo.


print("--------------------------------------")
print("---Determinar triángulo por ángulos---")
print("--------------------------------------")

# input

a = int(input("Digite el valor que quiera darle a A: "))
b = int(input("Digite el valor que quiera darle a B: "))
c = int(input("Digite el valor que quiera darle a C:"))

# processing

if (a and b and c <90):
    print("Las medidas forman un triángulo Agudo.")
elif(a == 90 and  b and c <90):
    print("Las medidas dadas forman un triángulo Recto.")
elif(b == 90 and a and c <90):
    print("Las medidas dadas forman un triángulo Recto.")
elif(c == 90 and a and b <90):
    print("Las medidas dadas forman un triángulo Recto.")
elif(a >90 and b and c <90):
    print("Las medidas dadas forman un triángulo Obtuso.")
elif(b >90 and a and c <90):
    print("Las medidas dadas forman un triángulo Obtuso.")
elif(c >90 and a and b <90):
    print("Las medidas dadas forman un triángulo Obtuso.")
else:
    print("No es posible determinar el tipo de triángulo. Por favor vuelva a intentarlo.")