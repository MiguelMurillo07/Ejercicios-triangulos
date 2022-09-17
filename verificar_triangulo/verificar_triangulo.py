# Ejercicio 1: Dados 3 numeros a,b,c verificar si se puede formar los lados de un triángulo-


print("-----------------------------------")
print("-------Verificar Triángulo---------")
print("-----------------------------------")

# input

a = int(input("Digite el valor que quiera para a:"))
b = int(input("Digite el valor que quiera para b:"))
c = int(input("Digite el valor que quiera para c:"))

# processing and output

if(a>0 and b>0 and c>0):
    if(a+b > c  and a+c > b and b+c > a):
        print("Si se puede formar un triángulo con los digitos ingresados.")
    else:print("Los valores digitados no cumplen con el teorema. Por favor vuelva a intentarlo.")

   