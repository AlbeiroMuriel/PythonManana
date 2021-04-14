'''
Diccionarios
* son elementos no ordenados
* se pueden indexar
* SON MUTUBLES.... se pueden modificar
* NO PERMITEN CLAVES REPETIDAS
* Dentro de un diccionario pueden existir otros diccionarios

CONCEPTOS
llave -- que este me identifica el elemnto, hace las veces de indice
valor -- contenido de llave

llave : valor
key : valor

Cedula     nombre     celular
123        Gisela      300-300-30-30

'''

Estudiante = {123: 'Gisela 300-300-30-30', 124:['Ariel, 301-301-31-31, 320-320-2020'], 125:'Jesus 321-321-2121'}

print(Estudiante)
print()

print(Estudiante[123])
print(Estudiante[124])
print(Estudiante[125])

#Agregar un nuevo elemento, siempre lo hace al final 

Estudiante[126]='Yessica 318-318-1818'
print('\n\n')
print(Estudiante)

#modificar un elemento, debo hacerlo por la key
Estudiante[125]='Jesus 321-321-2020'
print('\n\n')
print(Estudiante[125])
print('\n')
#buscar un key dentro del diccionario... GET

print(1234 in Estudiante)

print(Estudiante.get(1234, 'El Dato no existe o esta mal digitado'))

#mostrar todas las llaves o los key
print(Estudiante.keys())
#mostrar todas los valores
print(Estudiante.values())

