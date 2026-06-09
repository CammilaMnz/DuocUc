print("CALCULADORA")
print("___"*20)

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese un segundo numero: "))
numero3 = int(input("Ingrese un tercer numero: "))

while True:

    print("Menu de opciones")
    print("**"*20)
    print("1.-Sumar")
    print("2.-Restar")
    print("3.-Dividir")
    print("4.-Multiplicar")
    print("**"*20)

    opc = int(input("Ingrese una opcion: "))

    if opc == 1:
        print("La suma es:", numero1 + numero2 + numero3)
        break
    elif opc == 2:
        print("La resta es:", numero1 - numero2 - numero3)
        break
    elif opc == 3:
        print("La division es:", numero1 / numero2 / numero3)
        break
    elif opc == 4:
        print("La multiplicacion es:", numero1 * numero2 * numero3)
        break
    else:
        print("Opción no válida")

