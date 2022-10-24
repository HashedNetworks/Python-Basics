def calculo_dos_datos(num_1,num_2):
    res= ((num_1 - num_2)**2) + 1
    return(res)

def main():
    for i in range(0,3):
        inum_1 = int(input("Ingrese numero 1: " ))
        inum_2 = int(input("Ingrese numero 2: " ))
        resultado = calculo_dos_datos(inum_1,inum_2)
        print("\nNumero 1 es:" , inum_1)
        print("\nNumero 2 es:" , inum_2)
        print("\nla operacion da:" , resultado)


main()