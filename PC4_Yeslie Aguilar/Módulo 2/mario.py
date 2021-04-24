intentos = 0
while intentos < 1000:
    entrada= input('Ingrese un dato, por favor: ')
    intentos+= 1 
    if entrada in ('1','2','8'):
        for i in range(1,int(entrada)+1):
            print(" " * (int(entrada) - i)  + '#' * int(i))
        break
    else: 
        print('Dato inválido, inténtalo de nuevo')
        



