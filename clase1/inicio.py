print (' '.center(100,'─'))
print('Desarrollador. Su Nombre')
print('Correo. Su Correo')
print('Tema. Introducción')
print('Fecha. 5 Abril 2021')
print (' '.center(100,'─'))

# variables
# dinamicamente tipado
# Sumar dos numeros cualquiera

# print-- son mensajes en pantalla
# capturar el contenido input


""" nro1 = int(input('Nro 1 '))
nro2 = int(input('Nro 2 '))
suma = nro1 + nro2
print('suma =' , suma)
 """
# variables de tipo texto y concatenar

print (' * FUNCIONES DE CADENA *'.center(100))

texto = 'Desarrollo de software'

print(texto.center(100))
print(texto.rjust(100))
print(texto.ljust(100))

print(texto.lower()) # Todo en minúscula
print(texto.upper()) # Todo en mayúscula
print(texto.capitalize()) # Inicial en mayuscula

# concatenar 

nombre = 'Gisela'
Saludo = 'como estas? '
Curso = 'Python'

print("Hola {} {} bienvendid@ al curso de {}"+nombre,Saludo,Curso) #linea incorrecta

print("Hola {} {} bienvendid@ al curso de {}".format(nombre,Saludo,Curso))# para concatenar es con el . no con el +

print(f'Hola {nombre} {Saludo} bienvendid@ al curso de {Curso}')







