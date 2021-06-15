

from TS.Tipo import TIPO
from TS.Excepcion import Excepcion


class TablaSimbolos:
    def __init__(self, anterior = None):
        self.tabla = {} # Diccionario Vacio
        self.anterior = anterior

    def setTabla(self, simbolo):      # Agregar una variable
        if simbolo.id.lower() in self.tabla :
            return Excepcion("Semantico", "Variable " + simbolo.id + " ya existe", simbolo.fila, simbolo.columna)
        else:
            self.tabla[simbolo.id.lower()] = simbolo
            return None

    def getTabla(self, id):            # obtener una variable
        tablaActual = self
        while tablaActual.tabla != None:
            if id in tablaActual.tabla :
                return tablaActual.tabla[id]           # RETORNA SIMBOLO
            else:
                tablaActual = tablaActual.anterior
        return None

    def actualizarTabla(self, simbolo):
        tablaActual = self
        while tablaActual != None:
            if simbolo.id in tablaActual.tabla :
                if tablaActual.tabla[simbolo.id].getTipo() == simbolo.getTipo() or tablaActual.tabla[simbolo.id].getTipo()== TIPO.VAR or simbolo.getTipo()== TIPO.NULO or (tablaActual.tabla[simbolo.id].getTipo()==TIPO.DECIMAL and simbolo.getTipo()==TIPO.ENTERO) or simbolo.getTipo()== TIPO.INCREMENTO or simbolo.getTipo()== TIPO.DECREMENTO:
                    if simbolo.getTipo()== TIPO.NULO:
                        tablaActual.tabla[simbolo.id].setTipo(TIPO.VAR)
                    elif tablaActual.tabla[simbolo.id].getTipo()==TIPO.DECIMAL and simbolo.getTipo()==TIPO.ENTERO:
                        simbolo.setValor(float(simbolo.getValor()))
                    elif tablaActual.tabla[simbolo.id].getTipo()==TIPO.ENTERO and simbolo.getTipo()==TIPO.INCREMENTO:
                        simbolo.setValor(tablaActual.tabla[simbolo.id].getValor()+1)
                    elif tablaActual.tabla[simbolo.id].getTipo()==TIPO.ENTERO and simbolo.getTipo()==TIPO.DECREMENTO:
                        simbolo.setValor(tablaActual.tabla[simbolo.id].getValor()-1)
                    elif tablaActual.tabla[simbolo.id].getTipo()==TIPO.DECIMAL and simbolo.getTipo()==TIPO.INCREMENTO:
                        simbolo.setValor(tablaActual.tabla[simbolo.id].getValor()+1)
                    elif tablaActual.tabla[simbolo.id].getTipo()==TIPO.DECIMAL and simbolo.getTipo()==TIPO.DECREMENTO:
                        simbolo.setValor(tablaActual.tabla[simbolo.id].getValor()-1)
                    else:
                        if simbolo.getTipo()!=TIPO.INCREMENTO or simbolo.getTipo()!=TIPO.DECREMENTO:
                            tablaActual.tabla[simbolo.id].setTipo(simbolo.getTipo())
                        else:
                            return Excepcion("Semantico", "Tipo de dato Diferente en Asignacion", simbolo.getFila(), simbolo.getColumna())
                    tablaActual.tabla[simbolo.id].setValor(simbolo.getValor())         
                    return None             #VARIABLE ACTUALIZADA
                return Excepcion("Semantico", "Tipo de dato Diferente en Asignacion", simbolo.getFila(), simbolo.getColumna())
            else:
                tablaActual = tablaActual.anterior
        return Excepcion("Semantico", "Variable No encontrada en Asignacion", simbolo.getFila(), simbolo.getColumna())
        
    
