print (' '.center(100,'─'))
print('Desarrollador. Su Nombre')
print('Correo. Su Correo')
print('Tema. Calcular Salario')
print('Fecha. 5 Abril 2021')
print ('CALCULAR NOMINA'.center(100,'─'))

#Nombre, salario, nroTrabajadas, calcular el pago
''' Dato Entrada
        nombre, salario, nroTrabajadas
    Datos Proceso
        vlrHora = salario/240
        totalPago = vlrHora * nroTrabajadas
    Datos salida
        Nombre, salario, nroTrabajadas, totalPago
'''
# Datos de entrada
nombre = input('Nombre ----------> ')
salario = int(input('Salario ----->'))
nroHorTrab = int(input('Horas trabajadas -->'))

#Datos de proceso
vlrHora= salario /240
totalPago = vlrHora * nroHorTrab

#Datos de Salida
print(f'{nombre}'.center(50,'─'))
print(f'Salario -----------> {salario}')
print(f'Valor Hora --------> {vlrHora}')
print(f'Horas Trabajadas --> {nroHorTrab}')
print(f'Total a Pagar -----> {totalPago}')

