
print("Ingrese 10 números:")

numeros = []
for numerosalm in range(10):
    ingresonumero = float(input(f"Ingrese el número {numerosalm+1}: "))
    numeros.append(ingresonumero)


total = sum(numeros)
promedio = total / len(numeros)


print(f"El promedio de los números ingresados es: {promedio}")
