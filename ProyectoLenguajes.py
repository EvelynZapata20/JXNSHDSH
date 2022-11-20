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
        if (len(palabras)>2 and len(palabras)<4):
            if (palabras[2] not in Adjetivo) and (palabras[2] not in Determinantes) and (palabras[2] not in Preposiciones):
                Valor=False

        if (len(palabras)>3):
            if (palabras[2] in Preposiciones) and (palabras[3] not in Determinantes):
                Valor=False
            elif (palabras[2] in Determinantes) and (palabras[3] not in Sustantivos):
                Valor=False
            if (palabras[3] in Sustantivos) and ((palabras[4] not in Preposiciones) and (palabras[4] not in Adjetivo)):
                Valor=False
            elif (palabras[3] in Determinantes) and ((palabras[4] not in Sustantivos)):
                Valor=False

        if (palabras[len(palabras)-1] in Determinantes) or (palabras[len(palabras)-1] in Preposiciones):
            Valor=False

    return Valor


def Analizador(text: str):
    Valor = True
    Verbos= 0
    palabras = text.split()

    for i in palabras:
        if (i in VPasado) or (i in VPresente):
            Verbos=Verbos+1

    if Verbos==0:
        Valor=False

    if len(palabras) == 1:  # Caso donde tiene una única palabra
        Valor = False

    elif Verbos>1:
        Valor=False

    elif palabras[0] in Pronombres:  # Caso donde inicia con nombre propio
        Valor=NombrePropio(palabras)


    elif palabras[0] in Determinantes:  # Caso donde inicia con posesivo
        if palabras[1] not in Sustantivos:
            Valor = False
        else:
            palabras = palabras[1:]
            Valor=NombrePropio(palabras)

    print(Valor)

if __name__ == '__main__':
        print ("°|----------------------------------------------------------------------------------|°")
        print ("°|                        BIENVENIDO AL ANALIZADOR SINTÁCTICO                       |°")
        print ("°|----------------------------------------------------------------------------------|°")
        print ("°|         Puede realizar sus oraciones simples con las siguientes palabras         |°") 
        print ("°|----------------------------------------------------------------------------------|°")
        print ("°| PRONOMBRES | DETERMINANTES | PREPOSICIONES | SUSTANTIVOS |  VERBOS   | ADJETIVOS |°")
        print ("°|----------------------------------------------------------------------------------|°")
        print ("°| Camilo     | Mi            | Con           | Perro       | Ser       | Lento     |°")
        print ("°| Evelyn     | Tu            | En            | Cuchillo    | Estar     | Feo       |°")
        print ("°| Ana        | El            |               | Gato        | Pelar     | Verde     |°")
        print ("°| Juan       | La            |               | Loro        | Comer     | Rapido    |°")
        print ("°| Alejandro  | Una           |               | Casa        | Correr    | Grande    |°")
        print ("°| Isabel     | Un            |               | Manzana     | Estudiar  | Rica      |°")
        print ("°|            |               |               |             | Dormir    | Peligroso |°")
        print ("°|            |               |               |             | Programar | Sucia     |°")
        print ("°|            |               |               |             | Enseñar   |           |°")
        print ("°|            |               |               |             | Aprender  |           |°")
        print ("°|----------------------------------------------------------------------------------|°")
        print ("°|                                     RECUERDE                                     |°")
        print ("°|----------------------------------------------------------------------------------|°")
        print ("°| *La oración debe tener exactamente un verbo                                      |°")
        print ("°| *La oración debe tener como mínimo dos palabras y como máximo seis               |°") 
        print ("°| *Los verbos solo pueden conjugarse en presente o en pasado                       |°") 
        print ("°| *Si el verbo se conjuga en pasado, debe llevar su respectiva tilde               |°") 
        print ("°|----------------------------------------------------------------------------------|°")
        print ("°|----------------------------------------------------------------------------------|°")
        print ("°|                                     EJEMPLOS                                     |°")
        print ("°|----------------------------------------------------------------------------------|°")
        print ("°| *Camilo estudió en una casa verde                                                |°")
        print ("°| *Evelyn programa rapido en la casa                                               |°") 
        print ("°| *El perro comió con el gato                                                      |°") 
        print ("°| *La manzana verde es rica                                                        |°") 
        print ("°|----------------------------------------------------------------------------------|°\n")
        Flag = True
        while Flag:
           Opcion= input("¿Desea ingresar una nueva oración? (Si/No): ").lower()
           if (Opcion=="si"):
                Palabra=input("Ingrese su oración: ")
                Analizador(Palabra.lower())
           else:
            Flag=False
            print ("\n°|----------------------------------------------------------------------------------|°")
            print ("°|                    GRACIAS POR USAR EL ANALIZADOR SINTÁCTICO                     |°")
            print ("°|----------------------------------------------------------------------------------|°")
