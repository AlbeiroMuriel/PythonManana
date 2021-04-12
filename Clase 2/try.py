#try.. es capturar los errores y poder contralarlos

try:     
    nro1=int(input('Digite nro '))
    nro2=int(input('Digite nro '))
    suma = nro1 + nro2
    print(f'La suma es {suma}')
except:
    print('\n*********** Eror esto no es un numero ***********')
    