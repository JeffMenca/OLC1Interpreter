from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO, OperadorLogico

class Casteo(Instruccion):
    def __init__(self, tipo, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        self.tipo = tipo

    
    def interpretar(self, tree, table):
        val = self.expresion.interpretar(tree, table)

        if self.tipo == TIPO.DECIMAL:
            try:
                if self.expresion.tipo == TIPO.ENTERO or self.expresion.tipo == TIPO.CADENA or self.expresion.tipo == TIPO.CHARACTER:
                    return float(self.obtenerVal(self.expresion.tipo, val))
            except:
                return Excepcion("Semantico", "No se puede castear para Double.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de casteo para Double.", self.fila, self.columna)
        
        if self.tipo == TIPO.ENTERO:
            try:
                if self.expresion.tipo == TIPO.DECIMAL or self.expresion.tipo == TIPO.CADENA or self.expresion.tipo == TIPO.CHARACTER:
                    return int(self.obtenerVal(self.expresion.tipo, val))
            except:
                    return Excepcion("Semantico", "No se puede castear para Int.", self.fila, self.columna)   
            return Excepcion("Semantico", "Tipo Erroneo de casteo para Int.", self.fila, self.columna)
        
        if self.tipo == TIPO.CHARACTER:
            try:
                if self.expresion.tipo == TIPO.ENTERO:
                    return chr(self.obtenerVal(self.expresion.tipo, val))
            except:
                return Excepcion("Semantico", "No se puede castear para Char.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de casteo para Char.", self.fila, self.columna)
        
        if self.tipo == TIPO.CADENA:
            try:
                if self.expresion.tipo == TIPO.DECIMAL or self.expresion.tipo == TIPO.ENTERO:
                    return str(self.obtenerVal(self.expresion.tipo, val))
            except:
                    return Excepcion("Semantico", "No se puede castear para String.", self.fila, self.columna)   
            return Excepcion("Semantico", "Tipo Erroneo de casteo para String.", self.fila, self.columna)
        
        if self.tipo == TIPO.BOOLEANO:
            try:
                if self.expresion.tipo == TIPO.CADENA:
                    if val.lower()=="true":
                        return True
                    elif val.lower()=="false":
                        return False
                    else:
                        return Excepcion("Semantico", "Tipo Erroneo de casteo para Booleano.", self.fila, self.columna)
            except:
                    return Excepcion("Semantico", "No se puede castear para Booleano.", self.fila, self.columna)   
            return Excepcion("Semantico", "Tipo Erroneo de casteo para Booleano.", self.fila, self.columna)
        
    def getNodo(self):
        nodo = NodoAST("CASTEO")
        nodo.agregarHijo(str(self.tipo))
        nodo.agregarHijoNodo(self.expresion.getNodo())
        return nodo

    def obtenerVal(self, tipo, val):
        if tipo == TIPO.ENTERO:
            return int(val)
        elif tipo == TIPO.DECIMAL:
            return float(val)
        elif tipo == TIPO.BOOLEANO:
            return bool(val)
        elif tipo == TIPO.CHARACTER:
            return ord(val)
        return str(val)