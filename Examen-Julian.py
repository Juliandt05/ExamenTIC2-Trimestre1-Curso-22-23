
salida=1


def imprimir():
    print("     ")
    print("Menu")
    print("1-Sumar")
    print("2-Salir")

def sumanum(num1,num2):
    suma=num1+num2
    return(suma)

while salida!=2:
    try:
        imprimir()
        salida=int(input("Dime la opcion que has elegido: "))
        if salida==1:
            num1=int(input("Dime el primer número de la suma: "))
            num2=int(input("Dime el segundo número de la suma: "))
            print("La suma es",sumanum(num1,num2))
    except:
        print("Tienes que introducir un número")

print("Has terminado")

    