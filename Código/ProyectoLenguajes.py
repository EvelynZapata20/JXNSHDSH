"""Pronombres = ["camilo", "evelyn", "ana", "juan", "alejandro", "isabel"]
DFemeninos = ["la", "una","tu","mi"]
DMasculinos = ["el","un","mi", "tu"]
SMasculinos = ["perro", "cuchillo", "gato", "loro"]
SFemeninos = ["casa","manzana"]
Preposiciones = ["con", "en", "sobre"]
VPresente = ["es", "está", "pela", "come", "corre", "estudia", "duerme", "programa", "enseña", "aprende"]
VPasado = ["fue", "estuvo", "peló", "comió", "corrió", "estudió", "durmió", "programó", "enseñó", "aprendió"]
Adjetivos = ["lento", "feo", "verde", "rapido", "grande", "rica", "peligroso", "sucia",]


def MPronombres(palabras: list):
    print ("Entra método")
    Valor = True
    if (palabras[1] not in VPresente) and (palabras[1] not in VPasado):
        Valor = False
    else:
        palabras=palabras[1:]
        Valor=MVerbos(palabras)
        print ("Cumple")
    return Valor

def MDFemeninos(palabras: list):
    Valor = True
    if (palabras[1] not in SFemeninos):
        Valor = False
    else:
        palabras=palabras[1:]
        Valor=MPronombres(palabras)
    return Valor

def MDMasculinos(palabras: list):
    Valor = True
    if (palabras[1] not in SMasculinos):
        Valor = False
    else:
        palabras=palabras[1:]
        Valor=MPronombres(palabras)
    return Valor

def MPreposiciones (palabras: list):
    Valor = True
    if (palabras[1] not in DFemeninos) and (palabras[1] not in DMasculinos) and (palabras[1] not in Pronombres):
        Valor = False
    else:
        if(len(palabras))==2:
            if (palabras[len(palabras)-1]) not in Pronombres:
                Valor = False
        if(len(palabras>2)):
            palabras=palabras[1:]
            if palabras[0] in DFemeninos:
                Valor=MDFemeninos(palabras)
            elif palabras[0] in DMasculinos:
                Valor=MDMasculinos(palabras)
            elif palabras[0] in Pronombres:
                Valor=MPronombres(palabras)
    return Valor

def MAdjetivos (palabras: list):
    Valor= True
    if(len(palabras))==2:
            if (palabras[len(palabras)-1]) not in Preposiciones:
                Valor = False
    return Valor

def MVerbos (palabras: list):
    Valor= True
    if (palabras[1] not in Preposiciones) and (palabras[1] not in DFemeninos) and (palabras[1] not in DMasculinos) and (palabras[1] not in Adjetivos):
        Valor = False
    else:
        if(len(palabras))==2:
            if (palabras[len(palabras)-1]) not in Adjetivos:
                Valor = False
        if(len(palabras>2)):
            palabras=palabras[1:]
            if palabras[0] in Preposiciones:
                Valor=MPreposiciones(palabras)
            elif palabras[0] in DFemeninos:
                Valor=MDFemeninos(palabras)
            elif palabras[0] in DMasculinos:
                Valor=MDMasculinos(palabras)
            elif palabras[0] in Adjetivos:
                Valor=MAdjetivos(palabras)
    return Valor


def Analizador(text: str):
    Valor = True
    Verbos = 0
    palabras = text.split()

    for i in palabras: 
        if (i in VPasado) or (i in VPresente):
            Verbos = Verbos + 1

    if Verbos != 1:
        Valor = False

    if palabras[0] in (Pronombres):  # Caso donde inicia con nombre propio
        MPronombres(palabras)

    print (Valor)

Palabra= "Camilo lento corre"
Analizador(Palabra)"""

Pronombres = ["camilo", "evelyn", "ana", "juan", "alejandro", "isabel", "marco"]
Determinantes = ["mi", "tu", "el", "la", "una", "un"]
DeterminantesFemeninos=["la", "una","tu","mi"]
DeterminantesMasculinos=["el","un","mi", "tu"]
Preposiciones = ["con", "en", "sobre"]
Sustantivos = ["perro", "cuchillo", "gato", "loro", "casa", "carro", "manzana"]
SustantivosMasculinos=["perro", "cuchillo", "gato", "loro"]
SustantivosFemenino=["casa","manzana"]
VPresente = ["es", "está", "pela", "come", "corre", "estudia", "duerme", "programa", "enseña", "aprende"]
VPasado = ["fue", "estuvo", "peló", "comió", "corrió", "estudió", "durmió", "programó", "enseñó", "aprendió"]
Adjetivo = ["lento", "feo", "verde", "rapido", "grande", "rica", "peligroso", "sucia",]

def FDeterminantes(palabras:list): #Si inicia con algún determinante
    Valor=True
    if (palabras[0] in DeterminantesMasculinos) and (palabras[1] not in SustantivosMasculinos):
        Valor=False
    if(palabras[0] in DeterminantesFemeninos) and (palabras[1] not in SustantivosFemenino):
        valor=False
    return Valor

def FSustantivos(palabras:list):
    Valor=True
    if (palabras[0] in SustantivosFemenino)and (palabras[1] not in (Preposiciones and Adjetivo and VPresente and VPasado)):
        Valor=False
    elif (palabras[0] in SustantivosMasculinos) and (palabras[1] not in (Preposiciones and Adjetivo and VPresente and VPasado)):
        Valor=False
    return Valor

def FAdjetivos(palabra:list):
    Valor=True
    if (palabra[0]in Adjetivo)and (palabra[1] not in Preposiciones):
        Valor=False
    return Valor

def FNombrePropio(palabras: list):
    Valor = True
    if (palabras[1] not in VPresente) and (palabras[1] not in VPasado):
        Valor = False
    return Valor

def FPreposiciones(palabras:list):
    Valor=True
    if (palabras[0] in Preposiciones) and (palabras[1] not in Determinantes):
        Valor=False
    return Valor

def Fverbos(palabras:list):
    Valor=True
    if ((palabras[0] in VPasado) or (palabras[0] in VPresente)):
        if (palabras[1] not in (Preposiciones and Determinantes and Adjetivo)):
            Valor=False
    return Valor

def SubAnalizador(palabras:list):
    Valor=True
    while len(palabras) > 1:
        print(Valor)
        print(palabras)
        if palabras[0] in Pronombres:
            Valor = FNombrePropio(palabras)
            palabras = palabras[1:]
            if Valor == False:
                break
        elif (palabras[0] in VPasado) or (palabras[0] in VPresente):
            Valor = Fverbos(palabras)
            palabras = palabras[1:]
            if Valor == False:
                break

        elif palabras[0] in Preposiciones:
            Valor = FPreposiciones(palabras)
            palabras = palabras[1:]
            if Valor == False:
                break

        elif palabras[0] in Determinantes:
            Valor = FDeterminantes(palabras)
            palabras = palabras[1:]
            if Valor == False:
                break

        elif palabras[0] in SustantivosFemenino or SustantivosMasculinos:
            Valor = FSustantivos(palabras)
            palabras = palabras[1:]
            if Valor == False:
                break
    return Valor

def Analizador(text: str):
    text.lower()
    print(text)
    Valor = True
    Verbos = 0
    palabras = text.split()
    for i in palabras: #caso con mas de un verbo
        if (i in VPasado) or (i in VPresente):
            Verbos = Verbos + 1
    if Verbos == 0:
        Valor = False
    if len(palabras) == 1:  # Caso donde tiene una única palabra
        Valor = False
    elif Verbos > 1:
        Valor = False
    elif palabras[0] in Pronombres:  # Caso donde inicia con nombre propio
        Valor=SubAnalizador(palabras)
    elif palabras[0] in Determinantes:  # Caso donde inicia con posesivo
       Valor=SubAnalizador(palabras)
    return Valor


Palabra = "Camilo programa rapido casa"

print(Analizador(Palabra))

