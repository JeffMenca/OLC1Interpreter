from TS.Tipo import TIPO
from TS.Excepcion import Excepcion

variables=[]

class TablaSimbolos:
    def __init__(self, anterior = None):
        self.tabla = {} # Diccionario Vacio
        self.anterior = anterior
        

    def setTabla(self, simbolo):      # Agregar una variable
        global variables
        if simbolo.id.lower() in self.tabla :
            return Excepcion("Semantico", "Variable " + simbolo.id + " ya existe", simbolo.fila, simbolo.columna)
        else:
            self.tabla[simbolo.id.lower()] = simbolo
            encontro=True
            if len(variables)>0:
                for variable in variables:
                    if variable.id==simbolo.id:
                        encontro=True
                        break
                    else:
                        encontro=False
                if encontro==False:
                    variables.append(simbolo)
            else:
                variables.append(simbolo)
        return None  


    def getTabla(self, id):            # obtener una variable
        tablaActual = self
        while tablaActual != None:
            if id.lower() in tablaActual.tabla :
                return tablaActual.tabla[id.lower()]           # RETORNA SIMBOLO
            else:
                tablaActual = tablaActual.anterior
        return None

    def actualizarTabla(self, simbolo):
        global variables
        tablaActual = self
        while tablaActual != None:
            if simbolo.id.lower() in tablaActual.tabla :
                if tablaActual.tabla[simbolo.id.lower()].getTipo() == simbolo.getTipo() or tablaActual.tabla[simbolo.id.lower()].getTipo()== TIPO.VAR or simbolo.getTipo()== TIPO.NULO or (tablaActual.tabla[simbolo.id.lower()].getTipo()==TIPO.DECIMAL and simbolo.getTipo()==TIPO.ENTERO) or simbolo.getTipo()== TIPO.INCREMENTO or simbolo.getTipo()== TIPO.DECREMENTO:
                    if simbolo.getTipo()== TIPO.NULO:
                        tablaActual.tabla[simbolo.id.lower()].setTipo(TIPO.VAR)
                    elif tablaActual.tabla[simbolo.id.lower()].getTipo()==TIPO.DECIMAL and simbolo.getTipo()==TIPO.ENTERO:
                        simbolo.setValor(float(simbolo.getValor()))
                    elif tablaActual.tabla[simbolo.id.lower()].getTipo()==TIPO.ENTERO and simbolo.getTipo()==TIPO.INCREMENTO:
                        simbolo.setValor(tablaActual.tabla[simbolo.id.lower()].getValor()+1)
                    elif tablaActual.tabla[simbolo.id.lower()].getTipo()==TIPO.ENTERO and simbolo.getTipo()==TIPO.DECREMENTO:
                        simbolo.setValor(tablaActual.tabla[simbolo.id.lower()].getValor()-1)
                    elif tablaActual.tabla[simbolo.id.lower()].getTipo()==TIPO.DECIMAL and simbolo.getTipo()==TIPO.INCREMENTO:
                        simbolo.setValor(tablaActual.tabla[simbolo.id.lower()].getValor()+1)
                    elif tablaActual.tabla[simbolo.id.lower()].getTipo()==TIPO.DECIMAL and simbolo.getTipo()==TIPO.DECREMENTO:
                        simbolo.setValor(tablaActual.tabla[simbolo.id.lower()].getValor()-1)
                    else:
                        if simbolo.getTipo()!=TIPO.INCREMENTO or simbolo.getTipo()!=TIPO.DECREMENTO:
                            tablaActual.tabla[simbolo.id.lower()].setTipo(simbolo.getTipo())
                        else:
                            return Excepcion("Semantico", "Tipo de dato Diferente en Asignacion", simbolo.getFila(), simbolo.getColumna())
                    tablaActual.tabla[simbolo.id.lower()].setValor(simbolo.getValor())
                    for variable in variables:
                        if variable.id==simbolo.id:
                            variable.setValor(simbolo.getValor())
                            variable.setTipo(tablaActual.tabla[simbolo.id.lower()].getTipo())
                            break    
                    return None             #VARIABLE ACTUALIZADA
                return Excepcion("Semantico", "Tipo de dato Diferente en Asignacion", simbolo.getFila(), simbolo.getColumna())
            else:
                tablaActual = tablaActual.anterior
        return Excepcion("Semantico", "Variable No encontrada en Asignacion", simbolo.getFila(), simbolo.getColumna())

    def getVariables(self):
        return variables
    def vaciarVariables(self):
        global variables
        variables=[]