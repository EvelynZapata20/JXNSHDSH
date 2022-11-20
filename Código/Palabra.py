from FuncionesDeComparacion import Analizador
class OracionSimple:
    def __init__(self,frase):
        self.Frase=frase
    def Validar(self):
        analizar=self.Frase
        valor=Analizador(analizar)
        if valor==True:
            print("Frase Valida")
        else:
            print("Frase Invalida")
