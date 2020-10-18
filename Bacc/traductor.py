def espa_bin(pivote):
    pivote=pivote.upper()
    diccionario={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'Ñ':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26,' ':27}
    mensaje=""
    cadena=""
    for i in range(len(pivote)):
        caracter=pivote[i]
        y=(diccionario[caracter])
        y=int(y)
        cadena=diez_binario(y)
        mensaje+=cadena
    return mensaje

def diez_binario(n):
    binario=[]
    while (n>0):
        mod=(n%2)
        binario.append(mod)
        n=(int(n/2))
    size=len(binario)
    while (size<5):
        binario.append(0)
        size=size+1
    cadenaInvertida = binario[::-1]
    cadena=""
    for i in cadenaInvertida:
        cadena+=str(i)
    return cadena

def binario_diez(n):
    size=len(n)
    contador=0
    for i in n:
        if(i=='1'):
            contador=contador+(2**(size-1))
        size=size-1
    return contador

def bin_espa(encriptado):
    diccionario={'numeros': ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']}
    decimal=0
    pivote=""
    palabra=""
    contador=1
    for i in encriptado:
        pivote+=i
        if (contador%5==0):
            decimal=binario_diez(pivote)
            palabra+=diccionario['numeros'][decimal]
            pivote=""
        contador=contador+1
    print (palabra)