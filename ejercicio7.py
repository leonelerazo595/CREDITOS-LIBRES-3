numero1= int(input("ingresar el primer numero "))
numero2= int(input("ingresar el segundo numero "))


for n in range(numero1,numero2):  
    if n%2==0:
        print("")

    else:
         print(f"este numero es primo {n}")