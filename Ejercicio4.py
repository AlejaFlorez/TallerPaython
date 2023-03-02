departamentos_colombia = []

depa_colombia = int(input("cantidad de departamentos a ingresar: "))

for dep in range(0, depa_colombia):
    nombresdep = input(f"Ingrese el nomre del departamento {dep}:  ")
    departamentos_colombia.append(nombresdep)


print("los 2 últimos departamentos ingresados son : ", {departamentos_colombia[-2]}, {departamentos_colombia[-1]})
departamentos_colombia.sort(reverse=True)
print(departamentos_colombia)











