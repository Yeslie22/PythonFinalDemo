#American Express -> 15 dígitos
    #COMIENZAN CON 34 O 37

#MasterCard -> 16 dígitos
    #COMIENZAN CON 51, 52, 53, 54 o 55

#Visa -> 13 y 16 dígitos
    #COMIENZAN CON 4

#Número decimales (0 a 9) no binariarios
#Suma de verificación
entrada= input('Ingrese el número de su tarjeta, por favor: ')
def validacion(entrada): 
    digit = len(entrada)
    value = 0
    total = 0
    while  digit > 0: 
        if ((len(entrada)+1-digit) % 2 == 0):
            value = ( int( entrada[digit - 1]) * 2 )
        if (value > 9 ):
            double = str( value )
            value = int( double[:1]) + int(double[-1])
            total = total + value
            digit = digit - 1
        elif ((len(entrada)+1-digit) % 2 != 0): 
            value=int(entrada[digit - 1])
            total = total + int(entrada[digit - 1])
            digit = digit - 1
        else:
            total = total + value
            digit-=  1
    return total

def tarjeta(entrada):
    if (len(entrada)==15):
        if ((entrada[0]=='3' and entrada[1]=='4') or (entrada[0]=='3' and entrada[1]=='7')):
            salida= 'AMEX'
        else: 
            salida= 'INVALID'
            
    elif (len(entrada)==16):
        if ((entrada[0]=='5' and entrada[1]=='1') or (entrada[0]=='5' and entrada[1]=='2') or (entrada[0]=='5' and entrada[1]=='3') or (entrada[0]=='5' and entrada[1]=='4') or (entrada[0]=='5' and entrada[1]=='5')):
            salida= 'MASTERCARD'
        elif (entrada[0]=='4' ):
            salida= 'VISA'
        else: 
            salida= 'INVALID'

    elif (len(entrada)==13):
        salida= 'VISA'

    else: 
        salida= 'INVALID'

    return salida

estadito= validacion(entrada)
totalito= str(estadito)
m=0
while m < len(totalito):
    a=0
    for i in totalito:  
        if i == '0':
            a+=1
    m+=1

if a > 0:
    x= tarjeta(entrada)
else: 
    x= 'INVALID'

print(x)



  