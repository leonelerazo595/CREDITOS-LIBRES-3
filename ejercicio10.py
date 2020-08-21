aprobados=0
suspendidos=0

for alumnos in range(1,16):
    nota= int(input(f"ingresar nota del alumno {alumnos} : "))
    if nota >=3:
        aprobados+=1
    else:
        suspendidos+=1

print(f"alumnos que aprobaron {aprobados}")
print(f"alumnos suspendidos {suspendidos}")



