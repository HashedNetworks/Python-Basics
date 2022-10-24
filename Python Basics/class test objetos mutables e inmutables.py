class Ficha_De_Empleado:

    aumento_sueldo = 1.04
    num_de_emp = 0

    def __init__(self):
        self.name = None
        self.edad = None
        self.antiguedad = None
        self.__cualificacion = None

        Ficha_De_Empleado.num_de_emp += 1




    def __Sueldo(self):
        return(1000 + (self.antiguedad*25) + (self.__cualificacion*100))

    def SetCualificacion(self, cualif:int):
        if cualif == 1 or cualif ==2 or cualif == 3 or cualif == 4 or cualif == 5:
            self.__cualificacion =  cualif

    def GetCualificacion(self):
        return(self.__cualificacion)

    def GetSueldo(self):
        return(self.__Sueldo())

    def aumentoSueldo(self) :
        return(self.__Sueldo()*self.aumento_sueldo)


def aumentoAntiguedad(objeto, antiguedad):
    objeto.antiguedad += 1
    antiguedad += 1




    

def main():

    print(Ficha_De_Empleado.num_de_emp)

    emp_1 = Ficha_De_Empleado()
    emp_1.name = 'Andres'
    emp_1.edad = 39
    emp_1.antiguedad = 1
    emp_1.SetCualificacion(1)

   
    print(f'Nombre: {emp_1.name} , edad: {emp_1.edad} , Antiguedad: {emp_1.antiguedad} , cualificacion: {emp_1.GetCualificacion()} , {emp_1.GetSueldo()}')
    print(emp_1.aumento_sueldo)
    print(f'nuevo sueldo , {emp_1.aumentoSueldo()}')

    emp_2 = Ficha_De_Empleado()
    emp_2.name = 'Ana'
    emp_2.edad = 32
    emp_2.antiguedad = 1
    emp_2.SetCualificacion(1)
    emp_2.aumento_sueldo = 1.05
    print(emp_2.aumento_sueldo)
    print(f'nuevo sueldo , {emp_2.aumentoSueldo()}')
    

    print(Ficha_De_Empleado.num_de_emp)


    #print(emp_1.antiguedad , antiguedad)
    #print('')
    # print ('Aumento')
    #aumentoAntiguedad(emp_1, antiguedad)
    #print(f'Nombre: {emp_1.name} , edad: {emp_1.edad} , Antiguedad: {emp_1.antiguedad} , cualificacion: {emp_1.GetCualificacion()} , {emp_1.GetSueldo()}')

main()
