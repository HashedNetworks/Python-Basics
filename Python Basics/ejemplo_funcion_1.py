
def calculo_dos_datos():
    num_1 = int(input("Ingrese numero 1: " ))
    num_2 = int(input("Ingrese numero 2: " ))
    resultado = ((num_1 - num_2)**2)+1
    print("\nNumero 1 es:" , num_1)
    print("\nNumero 2 es:" , num_2)
    print("\nla operacion da:" , resultado)

def main():
    for i in range(0,3):
        calculo_dos_datos()

main()
