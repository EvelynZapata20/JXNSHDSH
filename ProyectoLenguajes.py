Pronombres = ["camilo", "evelyn", "ana", "juan", "alejandro", "isabel", "marco"]
Determinantes = ["mi", "tu","el","la", "una", "un"]
Preposiciones = ["con", "en", "sobre"]
Sustantivos=["perro", "cuchillo", "gato", "loro", "casa", "carro", "manzana"]
VPresente = ["es", "esta", "pela", "come", "corre", "estudia", "duerme", "programa", "programa", "enseña", "aprende"]
VPasado = ["fue", "estuvo", "peló", "comió", "corrió", "estudió", "durmió", "programó", "enseñó" , "aprendió"]
Adjetivo = ["lento", "feo", "verde", "rapido", "grande", "rica", "peligroso", "sucia", "mucho", "poco"]


def NombrePropio(palabras:list):
    Valor=True
    if (palabras[1] not in VPresente) and (palabras [1] not in VPasado):
        Valor=False
    else:
        if (len(palabras)>2):
            if (palabras[2] not in Adjetivo) and (palabras[2] not in Determinantes):
                Valor=False
        elif (len(palabras)>3):
            if (palabras[2] in Determinantes) and (palabras[3] not in Sustantivos):
                Valor=False
        elif (len(palabras)>4):
            if (palabras[4] in Preposiciones) and (palabras[5] not in Determinantes):
                Valor=False
    return Valor


def Analizador(text: str):
    Valor = True
    palabras = text.split()

    if len(palabras) == 1:  # Caso donde tiene una única palabra
        Valor = False

    elif palabras[0] in Pronombres:  # Caso donde inicia con nombre propio
        Valor=NombrePropio(palabras)


    elif palabras[0] in Determinantes:  # Caso donde inicia con posesivo
        if palabras[1] not in Sustantivos:
            Valor = False
        else:
            palabras = palabras[1:]
            Valor=NombrePropio(palabras)

    print(Valor)

Palabra= "Ana pela una manzana con cuchillo"
Analizador(Palabra.lower())

