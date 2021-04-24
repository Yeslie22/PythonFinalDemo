#Los intentos están en el archivo .ipynb

Letras= ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

entrada = input('Ingrese el texto a desencriptar, por favor: ')
miabc= 'VCHPRZGJNTLSKFBDQWAXEUYMOI'
action= input('Mode: ')

if action == 'encriptar':
    traducido= cifrar_textito(miabc, entrada)
elif action== 'desencriptar':
    traducido= descifrar_textito(miabc, entrada)
print(traducido)

def cifrar_textito (llave, ola):
    return traductor_texto(llave, ola, 'encriptar')
def descifrar_textito (llave, ola):
    return traductor_texto(llave, ola, 'desencriptar')

def traductor_texto (llave, ola, action):
    traducido=[]
    indice= 0
    llave= llave.upper()

    for simbolo in ola: 
        contador= miabc.find(simbolo.upper())
        if contador!=-1:
            if action== 'encriptar':
                contador+= miabc.find(llave[indice])
            elif action=='desencriptar':
                contador-= miabc.find(llave[indice])
            contador%= len(miabc)
            if simbolo.isupper():
                traducido.append(miabc[contador])
            elif simbolo.islower():
                traducido.append(miabc[contador].lower())
            indice+=1
            if indice == len(llave):
                indice= 0
        else: 
            traducido.append(simbolo)
    return ('').join(traducido)

