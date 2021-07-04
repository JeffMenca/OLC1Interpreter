from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from Abstract.NodoAST import NodoAST
from Instrucciones.Return import Return
from Instrucciones.Continue import Continue

class Switch(Instruccion):
    def __init__(self, expresion, cases,default, fila, columna):
        self.expresion= expresion
        self.cases= cases
        self.default= default
        self.fila= fila
        self.columna = columna

    def interpretar(self, tree, table):
        if self.cases == None:
            if self.default != None:
                self.default.interpretar(tree,table)
        else:
            result = False
            for case in self.cases:
                value = case.expresion.interpretar(tree,table)
                if isinstance(value, Excepcion): return value

                value2 = self.expresion.interpretar(tree,table)
                if isinstance(value2,Excepcion): return 2
                

                if value2 == value:
                    result = case.interpretar(tree, table)
                    #Analiza si el case tiene break
                    if (result): 
                        break
            if isinstance(result, Return): return result
            if isinstance(result, Continue): return result
            if not(result) and (self.default != None):
                self.default.interpretar(tree,table)
                
            

    def instruccionesInterpreter(self, instruccion, tree, table):

    # Realiza las acciones
        if isinstance(instruccion, list): 
            for element in instruccion:
                self.instruccionesInterpreter(element, tree,table)
        else:              
            value = instruccion.interpretar(tree,table)
            if isinstance(value, Excepcion) :
                tree.getExcepciones().append(value)
                tree.updateConsola(value.toString())
    
    def getNodo(self):
        nodo = NodoAST("Switch")
        instrucciones = NodoAST("INSTRUCCIONES")
        for instr in self.cases:
            instrucciones.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(instrucciones)
        return nodo