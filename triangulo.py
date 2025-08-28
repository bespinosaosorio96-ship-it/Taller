import os
os.system("clear")


isActive=True
while isActive:
        os.system("clear")
        print("Bienvenido al generador de triangulos")
        try:
            n=int(input("Ingresa el tamamño de la base del triangulo \nPresiones 0 para salir:"))
            if n == 0:
                isActive=False
                print("Gracias por usar el programa")
            elif n>1:
                for i in range(1, n+1):
                    print("*"*i)
                input("Presiones Enter para continuar")
            else:
                    print("No existe un triangulo con base 1")
                    input("Presione Enter para continuar")
                    
        except ValueError:
            print("Debe ingresar un numero entero")
            input("Presione enter para salir")
        

          


        
        
        
        
       



















    