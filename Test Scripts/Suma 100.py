suma = 0
while True:
    numero = int(input("Digite un numero: "))
    suma = suma + numero
    faltan = suma - 100
    if suma >= 100:
        break
    print("Te Faltan:" , faltan)
print("La suma total ha sido" , suma)