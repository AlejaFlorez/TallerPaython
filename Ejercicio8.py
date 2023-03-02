numeros = []

numerosenteros = int(input("ingrese la cantidad de numeros enteros que desea colocar: "))

for n in range(0, numerosenteros):
    nenteros = int(input(f"Ingrese los numeros  {n}:  "))
    numeros.append(nenteros)

numeros.sort(reverse=True)
print("descendientes: ", numeros)
numeros.sort()
print("ascendientes: ",numeros)


