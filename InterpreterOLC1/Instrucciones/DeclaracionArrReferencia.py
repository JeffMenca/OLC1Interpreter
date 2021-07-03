from re import A
from TS.Tipo import TIPO
from Abstract.NodoAST import NodoAST
from TS.Excepcion import Excepcion
from Abstract.Instruccion import Instruccion
from TS.Simbolo import Simbolo
import copy


class DeclaracionArrReferencia(Instruccion):
    def __init__(self, tipo1, dimensiones, identificador, identificador2, fila, columna):
        self.identificador = identificador
        self.tipo = tipo1
        self.dimensiones = dimensiones
        self.identificador2=identificador2
        self.fila = fila
        self.columna = columna
        self.arreglo = True
        self.dimensiones2 = 1


    def interpretar(self, tree, table):
        
        try:
            arreglo2 = table.getTabla(self.identificador2.lower())
            if arreglo2 == None:
                return Excepcion("Semantico", "Variable " + self.identificador + " no encontrada.", self.fila, self.columna)
            if not arreglo2.getArreglo(): 
                return Excepcion("Semantico", "Variable " + self.identificador + " no es un arreglo.", self.fila, self.columna)\
            
            if self.tipo != arreglo2.getTipo():                     #VERIFICACION DE TIPOS
                return Excepcion("Semantico", "Tipo de dato diferente en Arreglo.", self.fila, self.columna)
            
            expresiones2 = arreglo2.getValor()
            self.obtenerDimension(expresiones2)
            if self.dimensiones != self.dimensiones2:   #VERIFICACION DE DIMENSIONES
                return Excepcion("Semantico", "Dimensiones diferentes en Arreglo.", self.fila, self.columna)
        
            # CREACION DEL ARREGLO
            simbolo = Simbolo(str(self.identificador), self.tipo, self.arreglo, self.fila, self.columna, arreglo2.getValor())
            result = table.setTabla(simbolo)
            if isinstance(result, Excepcion): return result
            return None  
        except:
            return Excepcion("Semantico", "Tipo de dato no valido o negativo.", self.fila, self.columna)
        

    def getNodo(self):
        nodo = NodoAST("DECLARACION ARREGLO")
        nodo.agregarHijo(str(self.tipo))
        nodo.agregarHijo(str(self.dimensiones))
        nodo.agregarHijo(str(self.identificador))
        exp = NodoAST("EXPRESIONES DE LAS DIMENSIONES")
        return nodo

    def crearDimensiones(self, tree, table, expresiones):
        arr = []
        if len(expresiones) == 0:
            return None
        dimension = expresiones.pop(0)
        num = dimension.interpretar(tree, table)
        if isinstance(num, Excepcion): return num
        if dimension.tipo != TIPO.ENTERO:
            return Excepcion("Semantico", "Expresion diferente a ENTERO en Arreglo.", self.fila, self.columna)
        contador = 0
        while contador < num:
            arr.append(self.crearDimensiones(tree, table, copy.copy(expresiones)))
            contador += 1
        return arr
    
    def obtenerDimension(self, expresiones):
        for expresion in expresiones:
            if(isinstance(expresion,list)):
                self.dimensiones2 += 1 
                self.obtenerDimension(expresion)
            return None



            

