Pronombres = ["Camilo", "Evelyn", "Ana", "Juan", "Alejandro", "Isabel"]
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

def FDeterminantes(palabras:list):
    Valor=True
    if (palabras[0] in DeterminantesMasculinos)and (palabras[1] not in SustantivosMasculinos):
        Valor=False
    if(palabras[0] in DeterminantesFemeninos)and (palabras[1] not in SustantivosFemenino):
        valor=False
    return Valor
def FSustantivos(palabras:list):
    Valor=True
    if palabras[0] in SustantivosFemenino:
        if palabras[1] not in Preposiciones:
            if palabras[1] not in Adjetivo:
                if palabras[1] not in VPresente:
                    if palabras[1] not in  VPasado:
                        Valor=False
    if palabras[0] in SustantivosMasculinos:
        if palabras[1] not in Preposiciones:
            if palabras[1] not in Adjetivo:
                if palabras[1] not in VPresente:
                    if palabras[1] not in  VPasado:
                        Valor=False
    return Valor
def FAdjetivos(palabra:list):
    Valor=True
    if (palabra[0]in Adjetivo)and (palabra[1]not in Preposiciones):
        if palabra[1] not in VPasado:
            if palabra[1] not in VPresente:
                Valor=False
    return Valor

def FNombrePropio(palabras: list):
    Valor = True
    if (palabras[1] not in VPresente) and (palabras[1] not in VPasado):
        Valor = False
    return Valor
def FPreposiciones(palabras:list):
    Valor=True
    if (palabras[0] in Preposiciones)and (palabras[1] not in Determinantes):
        Valor=False
    return Valor
def Fverbos(palabras:list):
    Valor=True
    if ((palabras[0] in VPasado) or (palabras[0] in VPresente)):
            if palabras[1] not in DeterminantesMasculinos:
                if palabras[1] not in DeterminantesFemeninos:
                    if palabras[1] not in Preposiciones:
                        if palabras[1] not in Adjetivo:
                            Valor=False
    return Valor
def SubAnalizador(palabras:list):
    Valor=True
    while len(palabras) > 1:
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
        elif palabras[0] in Adjetivo:
            Valor = FAdjetivos(palabras)
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
