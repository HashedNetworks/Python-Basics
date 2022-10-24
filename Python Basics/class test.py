

class Ficha_De_Empleado:
    def __init__(self):
        self.name = None
        self.edad = None
        self.antiguedad = None
        self.__cualificacion = None
    def __Sueldo(self):
        return(1000 + (self.antiguedad*25) + (self.__cualificacion*100))
    def SetCualificacion(self, cualif:int):
        if cualif == 1 or cualif ==2 or cualif == 3 or cualif == 4 or cualif == 5:
            self.__cualificacion =  cualif
    def GetCualificacion(self):
        return(self.__cualificacion)
    def GetSueldo(self):
        return(self.__Sueldo())


def main():

    emp_1 = Ficha_De_Empleado()
    emp_1.name = 'Andres'
    emp_1.edad = 39
    antiguedad = int(input('Introduce la antiguedad de emp_1: '))
    emp_1.antiguedad = antiguedad
    emp_1.SetCualificacion(1)


    emp_2 = Ficha_De_Empleado()
    emp_2.name = 'Ana'
    emp_2.edad = 33
    antiguedad = int(input('Introduce la antiguedad de emp_2: '))
    emp_2.antiguedad = antiguedad
    emp_2.SetCualificacion(3)

    print(f'Nombre: {emp_1.name} , edad: {emp_1.edad} , Antiguedad: {emp_1.antiguedad} , cualificacion: {emp_1.GetCualificacion()} , {emp_1.GetSueldo()}')



    print(f'Nombre: {emp_2.name} , edad: {emp_2.edad} , Antiguedad: {emp_2.antiguedad} , cualificacion: {emp_2.GetCualificacion()} , {emp_2.GetSueldo()}')
  
 


main()
