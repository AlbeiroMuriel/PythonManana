#Listas-- es un conjunto de datos, almacenados en una variable.
#para crear una lista nombre=[ele1,ele2...eleN]
#Las listas son MUTABLES-- PUEDE CAMBIAR

Estudiantes =['Yessica','Ariel','Gisela','Jesus']
notas=['Jesus',4.7, True]
#Insertar elemento en una lista APPEND, lo hace al final de lista

Estudiantes.append('Profe')
print('Nuevo elemnto de la lista'.center(50,'*'))
print(Estudiantes)

print(f'Elemento de la posición 2 {Estudiantes[2]}')
Estudiantes[0] = 'Chica Gonzalez'
print(Estudiantes)


print('\n\nLISTA ORDENADA ASCENDENTE...')
# Comando sort--- para ordenar la lista
Estudiantes.sort()
print(Estudiantes)
print('\n\nLISTA ORDENADA DESCENDIENTE...')
Estudiantes.reverse()
print(Estudiantes)

#Eliminar elemento en una lista REMOVE
print('\nEliminar elemnto de la lista'.center(50,'*'))
Estudiantes.remove('Profe')
print('Eliminando el elemento PROFE')
print(Estudiantes)





