''' 
Jeffrey Menendez
Proyecto de Organizacion de lenguajes y compiladores 1

JPR Interpreter
'''
import re
import os
from Abstract.NodoAST import NodoAST
from tkinter.constants import CHAR
from TS.Tipo import OperadorAritmetico, TIPO
from TS.Excepcion import Excepcion
from TS.Arbol import Arbol
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Imprimir import Imprimir
from Expresiones.Primitivos import Primitivos
from TS.Tipo import OperadorAritmetico, OperadorLogico, TIPO, OperadorRelacional
from Expresiones.Aritmetica import Aritmetica
from Expresiones.Relacional import Relacional
from Expresiones.Logica import Logica
import sys
import ply.yacc as yacc
import ply.lex as lex
sys.setrecursionlimit(3000)

# Palabras reservadas
errores = []
variables=[]
funciones=[]
reservadas = {
    'int': 'RINT',
    'double': 'RDOUBLE',
    'string': 'RSTRING',
    'print': 'RPRINT',
    'boolean': 'RBOOLEAN',
    'char': 'RCHAR',
    'if': 'RIF',
    'else': 'RELSE',
    'switch': 'RSWITCH',
    'case': 'RCASE',
    'default': 'RDEFAULT',
    'break': 'RBREAK',
    'while': 'RWHILE',
    'for': 'RFOR',
    'continue': 'RCONTINUE',
    'return': 'RRETURN',
    'func': 'RFUNC',
    'read': 'RREAD',
    'main': 'RMAIN',
    'var': 'RVAR',
    'new': 'RNEW',
    'null': 'RNULL',
    
}

# Tokens
tokens = [
    'PUNTOCOMA',
    'COMA',
    'DOSPUNTOS',
    'PARA',
    'PARC',
    'LLAVEA',
    'LLAVEC',
    'CORA',
    'CORC',
    'MAS',
    'MENOS',
    'INCREMENTO',
    'DECREMENTO',
    'POR',
    'DIV',
    'POT',
    'MOD',
    'MENORQUE',
    'MAYORQUE',
    'IGUALIGUAL',
    'IGUAL',
    'AND',
    'OR',
    'NOT',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    'ID',
    'BOOLEANO',
    'CHARACTER',
    'DIFERENTE',
    'MAYORIGUAL',
    'MENORIGUAL'
] + list(reservadas.values())

# Asignacion de valor de tokens
t_PUNTOCOMA = r';'
t_COMA = r','
t_DOSPUNTOS = r':'
t_PARA = r'\('
t_PARC = r'\)'
t_LLAVEA= r'{'
t_LLAVEC= r'}'
t_CORA= r'\['
t_CORC= r'\]'
t_MAS = r'\+'
t_POR = r'\*'
t_DIV = r'/'
t_POT = r'\*\*'
t_MOD = r'%'
t_MENOS = r'-'
t_INCREMENTO = r'\+\+'
t_DECREMENTO = r'--'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_IGUALIGUAL = r'=='
t_IGUAL= r'='
t_DIFERENTE = r'=!'
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'


# Decimal
def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

# Booleano
def t_BOOLEANO(t):
    r'true|false'
    try:
        if t.value=='true':
            t.value=True
        elif t.value=='false':
            t.value=False
    except ValueError:
        print("Value not boolean %d", t.value)
        t.value = 0
    return t

# Caracter (Char)
def t_CHARACTER(t):
    r'\'(\\\'|\\"|\\t|\\n|\\\\|[^\'\\])?\''
    t.value = t.value[1:-1] 
    t.value = t.value.replace('\\t','\t')
    t.value = t.value.replace('\\n','\n')
    t.value = t.value.replace('\\"','\"')
    t.value = t.value.replace("\\'","\'")
    t.value = t.value.replace('\\\\','\\') 
    return t

# Entero
def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# ID
def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'ID')
    return t

# Cadena
def t_CADENA(t):
    r'\"(\\"|.)*?\"'
    t.value = t.value[1:-1] 
    t.value = t.value.replace('\\t','\t')
    t.value = t.value.replace('\\n','\n')
    t.value = t.value.replace('\\"','\"')
    t.value = t.value.replace("\\'","\'")
    t.value = t.value.replace('\\\\','\\')
    return t


# Comentario multilinea 
def t_COMENTARIO_MULTILINEA(t):
    r'\#\*(.|\n)*?\*\#'
    t.lexer.lineno += t.value.count('\n')
    
# Comentario simple 
def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def p_error(t):
    try:
        errores.append(Excepcion("Lexico", "Error léxico." +
                    t.value[0], t.lexer.lineno, find_column(input, t)))
    except:
        errores.append(Excepcion("Lexico", "Error léxico." , 0, 0))
        
def t_error(t):
    errores.append(Excepcion("Lexico", "Error léxico." +
                   t.value[0], t.lexer.lineno, find_column(input, t)))
    t.lexer.skip(1)

# Compute column.
#     input is the input text string
#     token is a token instance


def find_column(inp, token):
    line_start = inp.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


# Construyendo el analizador léxico
lexer = lex.lex(reflags= re.IGNORECASE)

# Asociación de operadores y precedencia
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'UNOT'),
    ('left', 'MENORQUE', 'MAYORQUE', 'MAYORIGUAL', 'MENORIGUAL', 'DIFERENTE', 'IGUALIGUAL'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIV', 'MOD'),
    ('nonassoc', 'POT'),
    ('right', 'UMENOS'),
    ('left', 'INCREMENTO','DECREMENTO'),
)


# Definición de la gramática

# Abstract
from Abstract.Instruccion import Instruccion
from Instrucciones.Imprimir import Imprimir
from Expresiones.Primitivos import Primitivos
from TS.Tipo import OperadorAritmetico, OperadorLogico, TIPO, OperadorRelacional
from Expresiones.Aritmetica import Aritmetica
from Expresiones.Relacional import Relacional
from Expresiones.Logica import Logica
from Instrucciones.Declaracion import Declaracion
from Expresiones.Identificador import Identificador
from Instrucciones.Asignacion import Asignacion
from Instrucciones.If import If 
from Instrucciones.While import While
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue
from Instrucciones.For import For
from Instrucciones.Switch import Switch
from Instrucciones.Case import Case
from Instrucciones.Main import Main
from Instrucciones.Return import Return
from Instrucciones.Funcion import Funcion
from Instrucciones.Llamada import Llamada
from Nativas.ToLower import ToLower
from Nativas.ToUpper import ToUpper
from Nativas.Length import Length
from Nativas.Truncate import Truncate
from Nativas.Round import Round
from Nativas.TypeOf import TypeOf
from Expresiones.Read import Read
from Expresiones.Casteo import Casteo
from Instrucciones.DeclaracionArr1 import DeclaracionArr1
from Instrucciones.DeclaracionArrReferencia import DeclaracionArrReferencia
from Expresiones.AccesoArreglo import AccesoArreglo
from Instrucciones.ModificarArreglo import ModificarArreglo


# ///////////////////////////////////////GRAMATICA//////////////////////////////////////////////////

def p_init(t):
    'init            : instrucciones'
    t[0] = t[1]


def p_instrucciones_instrucciones_instruccion(t):
    'instrucciones    : instrucciones instruccion'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

# ///////////////////////////////////////INSTRUCCIONES//////////////////////////////////////////////////


def p_instrucciones_instruccion(t):
    'instrucciones    : instruccion'
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

#///////////////////////////////////////INSTRUCCION//////////////////////////////////////////////////

def p_instruccion(t) :
    '''instruccion      : imprimir_instr finins
                        | declaracion_instr finins
                        | declaracion2_instr finins
                        | if_instr
                        | switch_instr
                        | for_instr
                        | while_instr
                        | break_instr finins
                        | continue_instr finins
                        | main_instr
                        | funcion_instr
                        | llamada_instr finins
                        | return_instr finins
                        | asignacion_instr finins
                        | asignacion2_instr finins
                        | declArr_instr finins
                        | modArr_instr finins'''
    t[0] = t[1]

def p_finins(t) :
    '''finins       : PUNTOCOMA
                    | '''
    t[0] = None

def p_instruccion_error(t):
    '''
    instruccion        : error PUNTOCOMA
    | error
    '''
    errores.append(Excepcion("Sintáctico","Error Sintáctico." + str(t[1].value) , t.lineno(1), find_column(input, t.slice[1])))
    t[0] = ""
    
#///////////////////////////////////////WHILE//////////////////////////////////////////////////

def p_while(t) :
    'while_instr     : RWHILE PARA expresion PARC LLAVEA instrucciones LLAVEC'
    t[0] = While(t[3], t[6], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////BREAK//////////////////////////////////////////////////

def p_break(t) :
    'break_instr     : RBREAK'
    t[0] = Break(t.lineno(1), find_column(input, t.slice[1]))
    
#///////////////////////////////////////CONTINUE//////////////////////////////////////////////////

def p_continue(t) :
    'continue_instr     : RCONTINUE'
    t[0] = Continue(t.lineno(1), find_column(input, t.slice[1]))
    
# ///////////////////////////////////////IMPRIMIR//////////////////////////////////////////////////

def p_imprimir(t):
    '''
    imprimir_instr     : RPRINT PARA expresion PARC PUNTOCOMA
    | RPRINT PARA expresion PARC 
    '''
    t[0] = Imprimir(t[3], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////DECLARACION//////////////////////////////////////////////////

def p_declaracion(t) :
    '''
    declaracion_instr     : tipo ID IGUAL expresion
    '''
    t[0] = Declaracion(t[1], t[2], t.lineno(2), find_column(input, t.slice[2]), t[4])
    
#///////////////////////////////////////DECLARACION NULA//////////////////////////////////////////////////

def p_declaracion2(t) :
    '''
    declaracion2_instr     : tipo ID 
    '''
    t[0] = Declaracion(t[1], t[2], t.lineno(2), find_column(input, t.slice[2]), None)

#///////////////////////////////////////ASIGNACION//////////////////////////////////////////////////

def p_asignacion(t) :
    '''
    asignacion_instr     : ID IGUAL expresion
    '''
    t[0] = Asignacion(t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))
    
def p_asignacion2(t) :
    '''
    asignacion2_instr     : ID INCREMENTO
    | ID DECREMENTO
    '''
    t[0] = Asignacion(t[1], str(t[2]), t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////IF//////////////////////////////////////////////////

def p_if1(t) :
    'if_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC'
    t[0] = If(t[3], t[6], None, None, t.lineno(1), find_column(input, t.slice[1]))

def p_if2(t) :
    'if_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE LLAVEA instrucciones LLAVEC'
    t[0] = If(t[3], t[6], t[10], None, t.lineno(1), find_column(input, t.slice[1]))

def p_if3(t) :
    'if_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE if_instr'
    t[0] = If(t[3], t[6], None, t[9], t.lineno(1), find_column(input, t.slice[1]))
    
#///////////////////////////////////////FOR//////////////////////////////////////////////////

def p_for_instr(t):
    '''
    for_instr : RFOR PARA asignacion_instr PUNTOCOMA expresion PUNTOCOMA asignacion2_instr PARC LLAVEA instrucciones LLAVEC
    '''
    t[0] = For(t[3],t[5],t[7],t[10],t.lineno(1), find_column(input, t.slice[1]))
def p_for_instr2(t):
    '''
    for_instr : RFOR PARA declaracion_for PUNTOCOMA expresion PUNTOCOMA asignacion2_instr PARC LLAVEA instrucciones LLAVEC
    '''
    t[0] = For(t[3],t[5],t[7],t[10],t.lineno(1), find_column(input, t.slice[1]))
def p_for_instr3(t):
    '''
    for_instr : RFOR PARA expresion PUNTOCOMA expresion PUNTOCOMA asignacion2_instr PARC LLAVEA instrucciones LLAVEC    
    '''
    t[0] = For(t[3],t[5],t[7],t[10],t.lineno(1), find_column(input, t.slice[1]))
def p_declaracion_for(t):
    '''
    declaracion_for :  tipo_for ID IGUAL expresion
    '''
    t[0] = Declaracion(t[1], t[2], t.lineno(2), find_column(input, t.slice[2]), t[4])
    
#///////////////////////////////////////SWITCH//////////////////////////////////////////////////
def p_switch_instr(t):
    '''
    switch_instr : RSWITCH PARA expresion PARC LLAVEA cases LLAVEC
    '''
    t[0] = Switch(t[3],t[6],None,t.lineno(5), find_column(input, t.slice[5]))
def p_switch_instr2(t):
    '''
    switch_instr : RSWITCH PARA expresion PARC LLAVEA cases default LLAVEC
    '''
    t[0] = Switch(t[3], t[6], t[7], t.lineno(5), find_column(input, t.slice[5]))
def p_switch_instr3(t):
    '''
    switch_instr : RSWITCH PARA expresion PARC LLAVEA default LLAVEC
    '''
    t[0] = Switch(t[3], None, t[6], t.lineno(5), find_column(input, t.slice[5]))
def p_switch_cases(t):
    '''
    cases : cases case
    '''
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]
def p_switch_cases2(t):
    '''
    cases : case
    '''
    t[0] = [t[1]]
def p_switch_case(t):
    '''
    case : RCASE expresion DOSPUNTOS instrucciones
    '''
    t[0] = Case(t[2],t[4],t.lineno(3), find_column(input, t.slice[3]))
def p_switch_default(t):
    '''
    default : RDEFAULT DOSPUNTOS instrucciones
    '''
    t[0] = Case(t[1],t[3],t.lineno(2), find_column(input, t.slice[2]))
    
#///////////////////////////////////////MAIN//////////////////////////////////////////////////

def p_main(t) :
    '''
    main_instr     : RMAIN PARA PARC LLAVEA instrucciones LLAVEC
    '''
    t[0] = Main(t[5], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////FUNCION//////////////////////////////////////////////////

def p_funcion_1(t) :
    'funcion_instr     : RFUNC ID PARA parametros PARC LLAVEA instrucciones LLAVEC'
    t[0] = Funcion(t[2], t[4], t[7], t.lineno(1), find_column(input, t.slice[1]))

def p_funcion_2(t) :
    'funcion_instr     : RFUNC ID PARA PARC LLAVEA instrucciones LLAVEC'
    t[0] = Funcion(t[2], [], t[6], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////PARAMETROS//////////////////////////////////////////////////

def p_parametros_1(t) :
    'parametros     : parametros COMA parametro'
    t[1].append(t[3])
    t[0] = t[1]
    
def p_parametros_2(t) :
    'parametros    : parametro'
    t[0] = [t[1]]

#///////////////////////////////////////PARAMETRO//////////////////////////////////////////////////

def p_parametro(t) :
    'parametro     : tipo ID'
    t[0] = {'tipo':t[1],'identificador':t[2]}

#///////////////////////////////////////LLAMADA A FUNCION//////////////////////////////////////////////////

def p_return(t) :
    'return_instr     : RRETURN expresion'
    t[0] = Return(t[2], t.lineno(1), find_column(input, t.slice[1]))
    
def p_llamada1(t) :
    'llamada_instr     : ID PARA PARC'
    t[0] = Llamada(t[1], [], t.lineno(1), find_column(input, t.slice[1]))

def p_llamada2(t) :
    'llamada_instr     : ID PARA parametros_llamada PARC'
    t[0] = Llamada(t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////PARAMETROS LLAMADA A FUNCION//////////////////////////////////////////////////

def p_parametrosLL_1(t) :
    'parametros_llamada     : parametros_llamada COMA parametro_llamada'
    t[1].append(t[3])
    t[0] = t[1]
    
def p_parametrosLL_2(t) :
    'parametros_llamada    : parametro_llamada'
    t[0] = [t[1]]

#///////////////////////////////////////PARAMETRO LLAMADA A FUNCION//////////////////////////////////////////////////

def p_parametroLL(t) :
    'parametro_llamada     : expresion'
    t[0] = t[1]
    
#///////////////////////////////////////DECLARACION ARREGLOS//////////////////////////////////////////////////

def p_declArr(t) :
    '''declArr_instr    : tipo1
    | declArrReferencia
    '''
    t[0] = t[1]
    
def p_tipo1(t) :
    '''tipo1     : tipo lista_Dim ID IGUAL RNEW tipo lista_expresiones
    '''
    t[0] = DeclaracionArr1(t[1], t[2], t[3], t[6], t[7], t.lineno(3), find_column(input, t.slice[3]))
    
def p_declArrReferencia(t) :
    '''declArrReferencia : tipo lista_Dim ID IGUAL ID
    '''
    t[0] = DeclaracionArrReferencia(t[1], t[2], t[3], t[5], t.lineno(3), find_column(input, t.slice[3]))
    
def p_lista_Dim1(t) :
    'lista_Dim     : lista_Dim CORA CORC'
    t[0] = t[1] + 1

def p_lista_Dim2(t) :
    'lista_Dim    : CORA CORC'
    t[0] = 1

def p_lista_expresiones_1(t) :
    'lista_expresiones     : lista_expresiones CORA expresion CORC'
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_expresiones_2(t) :
    'lista_expresiones    : CORA expresion CORC'
    t[0] = [t[2]]


#///////////////////////////////////////MODIFICACION ARREGLOS//////////////////////////////////////////////////


def p_modArr(t) :
    '''modArr_instr     :  ID lista_expresiones IGUAL expresion'''
    t[0] = ModificarArreglo(t[1], t[2], t[4], t.lineno(1), find_column(input, t.slice[1]))


#///////////////////////////////////////TIPO//////////////////////////////////////////////////

def p_tipo(t) :
    '''tipo     : RINT
                | RDOUBLE
                | RCHAR
                | RSTRING
                | RVAR
                | RBOOLEAN '''
    if t[1].lower() == 'int':
        t[0] = TIPO.ENTERO
    elif t[1].lower() == 'double':
        t[0] = TIPO.DECIMAL
    elif t[1].lower() == 'char':
        t[0] = TIPO.CHARACTER
    elif t[1].lower() == 'string':
        t[0] = TIPO.CADENA
    elif t[1].lower() == 'boolean':
        t[0] = TIPO.BOOLEANO
    elif t[1].lower() == 'var':
        t[0] = TIPO.VAR
        
def p_tipo_for(t) :
    '''tipo_for  : RINT
                | RVAR '''
    if t[1].lower() == 'int':
        t[0] = TIPO.ENTERO
    elif t[1].lower() == 'var':
        t[0] = TIPO.VAR

# ///////////////////////////////////////EXPRESION//////////////////////////////////////////////////

# Expresion binaria
def p_expresion_binaria(t):
    '''
    expresion : expresion MAS expresion
            | expresion MENOS expresion
            | expresion POR expresion
            | expresion DIV expresion
            | expresion POT expresion
            | expresion MOD expresion
            | expresion MENORQUE expresion
            | expresion MAYORQUE expresion
            | expresion MENORIGUAL expresion
            | expresion MAYORIGUAL expresion
            | expresion DIFERENTE expresion
            | expresion IGUALIGUAL expresion
            | expresion AND expresion
            | expresion OR expresion
    '''
    if t[2] == '+':
        t[0] = Aritmetica(OperadorAritmetico.MAS, t[1], t[3],
                          t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '-':
        t[0] = Aritmetica(OperadorAritmetico.MENOS, t[1], t[3],
                          t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '*':
        t[0] = Aritmetica(OperadorAritmetico.POR, t[1], t[3],
                          t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '/':
        t[0] = Aritmetica(OperadorAritmetico.DIV, t[1], t[3],
                          t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '**':
        t[0] = Aritmetica(OperadorAritmetico.POT, t[1], t[3],
                          t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '%':
        t[0] = Aritmetica(OperadorAritmetico.MOD, t[1], t[3],
                          t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<':
        t[0] = Relacional(OperadorRelacional.MENORQUE, t[1],
                          t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>':
        t[0] = Relacional(OperadorRelacional.MAYORQUE, t[1],
                          t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<=':
        t[0] = Relacional(OperadorRelacional.MENORIGUAL, t[1],
                          t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>=':
        t[0] = Relacional(OperadorRelacional.MAYORIGUAL, t[1],
                          t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '=!':
        t[0] = Relacional(OperadorRelacional.DIFERENTE, t[1],
                          t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '==':
        t[0] = Relacional(OperadorRelacional.IGUALIGUAL, t[1],
                          t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '&&':
        t[0] = Logica(OperadorLogico.AND, t[1], t[3],
                      t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '||':
        t[0] = Logica(OperadorLogico.OR, t[1], t[3], t.lineno(2),
                      find_column(input, t.slice[2]))
    elif t[2] == '++':
        t[0] = Aritmetica(OperadorAritmetico.INCREMENTO, t[1],str(t[2]), t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '--':
        t[0] = Aritmetica(OperadorAritmetico.DECREMENTO, t[1],str(t[2]), t.lineno(2), find_column(input, t.slice[2]))

# Expresion unaria
def p_expresion_unaria(t):
    '''
    expresion : MENOS expresion %prec UMENOS 
            | NOT expresion %prec UNOT 
    '''
    if t[1] == '-':
        t[0] = Aritmetica(OperadorAritmetico.UMENOS, t[2],
                          None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == '!':
        t[0] = Logica(OperadorLogico.NOT, t[2], None,
                      t.lineno(1), find_column(input, t.slice[1]))

# Expresion agrupacion
def p_expresion_agrupacion(t):
    '''
    expresion :   PARA expresion PARC 
    '''
    t[0] = t[2]
    
# Expresion llamada
def p_expresion_llamada(t):
    '''expresion : llamada_instr'''
    t[0] = t[1]
 
 # Expresiones y primitivos   
def p_expresion_identificador(t):
    '''expresion : ID'''
    t[0] = Identificador(t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_entero(t):
    '''expresion : ENTERO'''
    t[0] = Primitivos(TIPO.ENTERO, t[1], t.lineno(1),
                      find_column(input, t.slice[1]))

def p_primitivo_decimal(t):
    '''expresion : DECIMAL'''
    t[0] = Primitivos(TIPO.DECIMAL, t[1], t.lineno(1),
                      find_column(input, t.slice[1]))

def p_primitivo_cadena(t):
    '''expresion : CADENA'''
    t[0] = Primitivos(TIPO.CADENA, str(t[1]).replace(
        '\\n', '\n'), t.lineno(1), find_column(input, t.slice[1]))
    
def p_primitivo_character(t):
    '''expresion : CHARACTER'''
    t[0] = Primitivos(TIPO.CHARACTER, str(t[1]).replace(
        '\\n', '\n'), t.lineno(1), find_column(input, t.slice[1]))
    
def p_primitivo_booleano(t):
    '''expresion : BOOLEANO'''
    t[0] = Primitivos(TIPO.BOOLEANO,bool(t[1]), t.lineno(1), find_column(input, t.slice[1])) 
    
def p_primitivo_null(t):
    '''expresion : RNULL'''
    t[0] = Primitivos(TIPO.NULO,None, t.lineno(1), find_column(input, t.slice[1]))
    
def p_expresion_read(t):
    '''expresion : RREAD PARA PARC'''
    t[0] = Read(t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_cast(t):
    '''expresion : PARA tipo PARC expresion'''
    t[0] = Casteo(t[2], t[4], t.lineno(1), find_column(input, t.slice[1]))
    
def p_expresion_Arreglo(t):
    '''expresion : ID lista_expresiones'''
    t[0] = AccesoArreglo(t[1], t[2], t.lineno(1), find_column(input, t.slice[1]))
    


# Se parsea
parser = yacc.yacc()
input = ''


def getErrores():
    return errores

def getVariables():
    return variables

def getFunciones():
    return funciones


def parse(inp):
    global errores
    global variables
    global funciones
    global lexer
    global parser
    errores = []
    variables=[]
    funciones=[]
    lexer = lex.lex(reflags= re.IGNORECASE)
    parser = yacc.yacc()
    global input
    input = inp
    return parser.parse(inp)


def crearNativas(ast):          # CREACION Y DECLARACION DE LAS FUNCIONES NATIVAS
    nombre = "toupper"
    parametros = [{'tipo':TIPO.CADENA,'identificador':'toUpper##Param1'}]
    instrucciones = []
    toUpper = ToUpper(nombre, parametros, instrucciones, -1, -1)
    ast.addFuncion(toUpper)     # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)

    nombre = "tolower"
    parametros = [{'tipo':TIPO.CADENA,'identificador':'toLower##Param1'}]
    instrucciones = []
    toLower = ToLower(nombre, parametros, instrucciones, -1, -1)
    ast.addFuncion(toLower)     # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)
    
    nombre = "length"
    parametros = [{'tipo':TIPO.CADENA,'identificador':'length##Param1'}]
    instrucciones = []
    length = Length(nombre, parametros, instrucciones, -1, -1)
    ast.addFuncion(length)     # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)
        
    nombre = "truncate"
    parametros = [{'tipo':TIPO.DECIMAL,'identificador':'truncate##Param1'}]
    instrucciones = []
    truncate = Truncate(nombre, parametros, instrucciones, -1, -1)
    ast.addFuncion(truncate)     # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)
    
    nombre = "round"
    parametros = [{'tipo':TIPO.DECIMAL,'identificador':'round##Param1'}]
    instrucciones = []
    roundNumber = Round(nombre, parametros, instrucciones, -1, -1)
    ast.addFuncion(roundNumber)     # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)
    
    nombre = "typeof"
    parametros = [{'tipo':TIPO.CADENA,'identificador':'typeof##Param1'}]
    instrucciones = []
    typeof = TypeOf(nombre, parametros, instrucciones, -1, -1)
    ast.addFuncion(typeof)     # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)
    

# Metodo que conecta con el frontend (INTERFAZ)
def analizar(texto):
    entrada = texto
    contador = 0
    # ARBOL AST
    instrucciones = parse(entrada)
    ast = Arbol(instrucciones)
    TSGlobal = TablaSimbolos()
    ast.setTSglobal(TSGlobal)
    if len(TSGlobal.getVariables())!=0:
        TSGlobal.vaciarVariables()
    crearNativas(ast)
    for error in errores:
        # Metodo para capturar errores
        ast.getExcepciones().append(error)
        ast.updateConsola(error.toString())
    if ast.getInstrucciones()!=None:
        # Toma declaraciones y asignaciones
        for instruccion in ast.getInstrucciones():   
            TSGlobal.setEntorno("Global")   
            if isinstance(instruccion, Funcion):
                # Guarda la funcion
                ast.addFuncion(instruccion)  
            if isinstance(instruccion, Declaracion) or isinstance(instruccion, Asignacion) or isinstance(instruccion, DeclaracionArr1) or isinstance(instruccion, ModificarArreglo):
                value = instruccion.interpretar(ast,TSGlobal)
                if value !=None:
                    if isinstance(value, Excepcion) :
                            ast.getExcepciones().append(value)
                            ast.updateConsola(value.toString())
                            errores.append(value)
                    elif isinstance(value, Break): 
                            err = Excepcion("Semantico", "Sentencia BREAK fuera de ciclo", instruccion.fila, instruccion.columna)
                            ast.getExcepciones().append(err)
                            errores.append(err)
                            ast.updateConsola(err.toString())
                    elif isinstance(value, Continue): 
                            err = Excepcion("Semantico", "Sentencia CONTINUE fuera de ciclo", instruccion.fila, instruccion.columna)
                            ast.getExcepciones().append(err)
                            errores.append(err)
                            ast.updateConsola(err.toString())
                    else:
                        for error in value:
                            errores.append(error)
        # Toma el Main
        for instruccion in ast.getInstrucciones():   
            TSGlobal.setEntorno("Main")   
            if isinstance(instruccion, Main):
                contador += 1
                # Verifica solo 1 main
                if contador == 2: 
                    err = Excepcion("Semantico", "Existen 2 funciones Main", instruccion.fila, instruccion.columna)
                    ast.getExcepciones().append(err)
                    ast.updateConsola(err.toString())
                    errores.append(err)
                    break
                value = instruccion.interpretar(ast,TSGlobal)
                if value !=None:
                    if isinstance(value, Excepcion) :
                        ast.getExcepciones().append(value)
                        ast.updateConsola(value.toString())
                        errores.append(value)
                    elif isinstance(value, Break): 
                        err = Excepcion("Semantico", "Sentencia BREAK fuera de ciclo", instruccion.fila, instruccion.columna)
                        ast.getExcepciones().append(err)
                        errores.append(err)
                        ast.updateConsola(err.toString())
                    elif isinstance(value, Return): 
                        err = Excepcion("Semantico", "Sentencia RETURN fuera de ciclo", instruccion.fila, instruccion.columna)
                        ast.getExcepciones().append(err)
                        errores.append(err)
                        ast.updateConsola(err.toString())
                    elif isinstance(value, Continue): 
                        err = Excepcion("Semantico", "Sentencia CONTINUE fuera de ciclo", instruccion.fila, instruccion.columna)
                        ast.getExcepciones().append(err)
                        errores.append(err)
                        ast.updateConsola(err.toString())
                    else:
                        for error in value:
                            errores.append(error)
        # Toma todo lo que esta fuera del main
        for instruccion in ast.getInstrucciones():    
            if not (isinstance(instruccion, Main) or isinstance(instruccion, Declaracion) or isinstance(instruccion, Asignacion) or isinstance(instruccion, Funcion) or isinstance(instruccion, DeclaracionArr1)  or isinstance(instruccion, ModificarArreglo)):
                err = Excepcion("Semantico", "Sentencias fuera de Main", instruccion.fila, instruccion.columna)
                ast.getExcepciones().append(err)
                ast.updateConsola(err.toString())
                errores.append(err)
    
        init = NodoAST("RAIZ")
        instr = NodoAST("INSTRUCCIONES")
        for instruccion in ast.getInstrucciones():
            instr.agregarHijoNodo(instruccion.getNodo())
        init.agregarHijoNodo(instr)
        grafo = ast.getDot(init) #DEVUELVE EL CODIGO GRAPHVIZ DEL AST
        dirname = os.path.dirname(__file__)
        direcc = os.path.join(dirname, 'ast.dot')
        arch = open(direcc, "w+")
        arch.write(grafo)
        arch.close()
        os.system('dot -T pdf -o ast.pdf ast.dot')
        for variable in TSGlobal.getVariables():
            variables.append(variable)
        for funcion in ast.getFunciones():
            funciones.append(funcion)
             
    return ast.getConsola()
