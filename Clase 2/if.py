#if se utiliza para realizar comparaciones con los datos.

'''
    if ():
        instrucciones
    else   
        instrucciones

anidado

    if ():
        instrucciones
    elif ():
        instrucciones
    elif ():
        instrucciones
    else
        instrucciones        

print('Digitar dos numeros DIFERENTES y decir cual es el mayor \n')

nro1 = int(input('Nro 1 '))
nro2 = int(input('Nro 2 '))

if nro1 > nro2:
    print(f'El numero {nro1} es el mayor')
else:
    print(f'El nuemro {nro2} es el mayor')
    '''
print('Digitar dos tres DIFERENTES y decir cual es el mayor \n')
nro1=int(input('Nro 1 '))
nro2=int(input('Nro 2 '))
nro3=int(input('Nro 3 '))
if nro1 > nro2 and nro1 > nro3:
    print(f'El numero {nro1} es el mayor')
elif nro2 > nro3:
    print(f'El numero {nro2} es el mayor')   
else:
    print(f'El numero {nro3} es el mayor')  



