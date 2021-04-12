listaMercado=['Carne','Pollo','Huevo','Arepas','Leche','Arroz','Papas','Cafe','Panela','Carnes frias', 'Parva', 'Quesito']

#Longitud o tamaño de una lista LEN
print(listaMercado)
print(f'Nro de Elementos de la lista {len(listaMercado)}')

print('Lista ordenada'.center(50,'─'))
listaMercado.sort()
print(listaMercado)

#slice-- Son para imprimir rangos de posición de los elementos
print('\n\nListar los 4 primeros elementos de la lista')
print(listaMercado[0:4])

print('\n\nMostrar la lista con salto de elementos')
print(listaMercado[0::2])

print('\n Mostrar el ultimo elemento de la lista')
print('El ultimo elemento de la lista es ', listaMercado[-2])

print('\nBuscar elemento dentro de una lista')

print('licor' in listaMercado)

print(listaMercado[4:]) # desde el elemento .... hasta el final
print(listaMercado[:5])

