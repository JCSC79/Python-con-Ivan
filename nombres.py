#Ejercicio 1:
#Crea dos arrays que tengan el mismo tamaño (lo pedirá por teclado), en uno de ellos almacenarás nombres de personas como cadenas, en el otro array irá almacenando la longitud de los nombres

print("\tEjercicio de nombres y tamaños")
print("\t==============================")

print("Introduce ¿cuántos nombres vas a meter en la lista: ")
tamaño = input()
z = int(tamaño)

# print(f"El numero es: {tamaño}")
# print(f"El si le sumo 3 es: {z+3}")
print(f"Muy bien, vamos a introducir {tamaño} nombres.\n")
print("-"*45)

#Creo 2 arrays vacios por ahora
nombres = []
longitudes = []
mayor= 0
menor = 100000000000000000000000
posicion_menor = -1 
posicion_mayor = -1


#Ciclo para pedir nombre e ir guardando en el las longitudes de cada uno
for i in range(z):
    #nombre = input(f"Ingresa nombre numero {i+1}: ") #Aqui se lista e ingresa cada nombre nuevo
    nombre = input(f"Ingresa el nombre #{i+1}: ").title()  # Capitaliza automáticamente
    nombres.append(nombre)  #Con el método append agregamos al array nombres que estaba vacio un nuevo nombre
    #longitudes.append(len(nombre)) #Aqui agregamos al array longitudes los tamaños de los nombres que se calvulan con el len
    longitudes.append(len(nombre.replace(" ", "")))
    
    if longitudes[i]>mayor:
        mayor = longitudes[i]
        posicion_mayor = i
    
    if longitudes[i]<menor:
        menor = longitudes[i]
        posicion_menor = i
    
#SALIDAS POR PANTALLA
print("\nNombres y longitudes:")
print("-"*25)

#Este for puede recorrer simultaneamente los dos arrays y mostrar fácilmente ambas informaciones con una sola linea de código
for i in range(z):
    print(f"{i+1}) {nombres[i]} tiene {longitudes[i]} caracteres")
    
print(f"El nombre: {nombres[posicion_mayor]} es el mas largo con: {mayor} caracteres")
print(f"El nombre: {nombres[posicion_menor]} es el mas corto con: {menor} caracteres")