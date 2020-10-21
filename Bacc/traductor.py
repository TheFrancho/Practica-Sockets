def espa_bin(pivote): #Función principal que transforma de español a binario
    pivote=pivote.upper() #Toma toda la cadena de entrada y la vuelve a mayusculas
    diccionario={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'Ñ':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26,' ':27, "\n" : 28, "," : 29, ".": 30, ":" : 31}
    mensaje="" #Inicializamos el mensaje
    cadena="" #Se inicializa la cadena que va a contener el binario de la letra
    for i in range(len(pivote)): #Se hace un for para toda la cadena
        try: #Se intenta buscar en el diccionario la letra, si no está, se salta al except
            caracter=pivote[i] #Todo este ciclo es para sacar letra a letra, pasarla a base 10 y luego a binario y concatenarla
            y=(diccionario[caracter])
            y=int(y)
            cadena=diez_binario(y)
            mensaje+=cadena
        except:
            mensaje+=""
    return mensaje

def diez_binario(n): #Función chiquita que trabsforma de base 10 a base 2
    binario=[] #Se sacan los binarios por el método de la división, por lo qeu hay que invertir la cadena
    while (n>0):
        mod=(n%2)
        binario.append(mod)
        n=(int(n/2))
    size=len(binario)
    while (size<5): #Esto es importante, si le entra una cadena con menos de 5 digitos, les pega 0 a la derecha (luego se invierte)
        binario.append(0)
        size=size+1
    cadenaInvertida = binario[::-1] #Aqui se invierte
    cadena=""
    for i in cadenaInvertida:
        cadena+=str(i) #Se para de lista a string
    return cadena #Se retorna

def binario_diez(n): #Función chiquita que traduce de binario a base 10
    size=len(n)
    contador=0
    for i in n:
        if(i=='1'):
            contador=contador+(2**(size-1))
        size=size-1
    return contador

def depurador(encriptado): #Función auxiliar para limpiar cadenas con binarios
    puro=""
    for i in encriptado:
        if i == "0" or i=="1":
            puro+=i
    return puro


def bin_espa(encriptado): #Función principal que transforma de español a binario
    diccionario={'numeros': ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ', '\n', ",", ".", ":" ]}
    decimal=0 #Variable deonde se guarda el valor decimal de cada palabra
    pivote="" #Cadena donde se van almacenando paquetes de 5 bits
    palabra="" #Cadena principal donde se va aquiriendo la palabra a retornar
    encriptado=depurador(encriptado) #Se depura la cadena (se le quita todo lo que no sea 0 o 1)
    contador=1 #El contador define cuantos por cuantos bits ha pasado hasta que junte 5
    for i in encriptado: #Se procesa
        pivote+=i #Se va concatenando binario a binario hasta que quedan 5
        if (contador%5==0): #Si están 5 concatenados (porque para nuestro diccionario son 5 bits)
            decimal=binario_diez(pivote) #Entonces se transforman los 5
            try: #Se busca ese número adquirido en el diccionario, si no está, se pasa al except
                palabra+=diccionario['numeros'][decimal]
            except: #Se ignora la palabra
                palabra+=""
            pivote=""
        contador=contador+1 
    return palabra
