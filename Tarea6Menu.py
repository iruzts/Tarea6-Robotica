def menu():
    print("********************************")
    print("*             MENU             *")
    print("*1. División entre dos números *")
    print("*2. Area del cuadrado          *")
    print("*3. Area del triángulo         *")
    print("*4.      Salir                 *")
    print("********************************")
    opcion = int(input("Escoja la opcion: "))
    return opcion
opcion = menu()
while opcion != 4:
    if opcion == 1:
        print("Division entre dos numeros")
        n1 = int(input("ingrese la primera cantidad: " ) )
        n2 = int(input("ingrese la primera cantidad: " ) )
        cal = n1/n2
        print("Respuesta: " + str(cal) + "\n")
    elif opcion == 2:
        print("Calculo del area de un Cuadrado")
        lado = int(input("ingrese uno de los Lados: " ) )
        CalculoC = lado*lado
        print("Area del Cuadrado es: " + str(CalculoC) + "\n")
    elif opcion == 3:
        print("Calculo del area de un Triangulo")
        base = int(input("ingrese la base: " ) )
        altura = int(input("ingrese la altura: "))
        calculo = base*altura/2
        print("Area del triangulo: " + str(calculo) + "\n")
    else:
        print("Opcion no valida\n")
    opcion = menu()