''' 
Jeffrey Menendez
Proyecto de Organizacion de lenguajes y compiladores 1

JPR Interpreter
'''
import re
from tkinter.constants import CHAR
from TS.Tipo import OperadorAritmetico, TIPO
from TS.Excepcion import Excepcion
from TS.Arbol import Arbol
from TS.TablaSimbolos import TablaSimbolos
from Abstract.Instruccion import Instruccion
from Instrucciones.Imprimir import Imprimir
from Expresiones.Primitivos import Primitivos
from TS.Tipo import OperadorAritmetico, OperadorLogico, TIPO, OperadorRelacional
from Expresiones.Aritmetica import Aritmetica
from Expresiones.Relacional import Relacional
from Expresiones.Logica import Logica
import ply.yacc as yacc
import ply.lex as lex

# Palabras reservadas
errores = []
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
    'tolower': 'RTOLOWER',
    'toupper': 'RTOUPPER',
    'length': 'RLENGTH',
    'truncate': 'RTRUNCATE',
    'round': 'RROUND',
    'typeof': 'RTYPEOF',
    'main': 'RMAIN',
    'var': 'RVAR',
    'null': 'RNULL',
}

# Tokens
tokens = [
    'PUNTOCOMA',
    'PARA',
    'PARC',
    'LLAVEA',
    'LLAVEC',
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
t_PARA = r'\('
t_PARC = r'\)'
t_LLAVEA= r'{'
t_LLAVEC= r'}'
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
t_DIFERENTE = r'!='
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
    r'(\'.?\')'
    t.value = t.value[1:-1]  # remuevo las comillas
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
    r'(\".*?\")'
    t.value = t.value[1:-1]  # remuevo las comillas
    t.value=t.value.replace('\\t','\t')
    t.value=t.value.replace('\\n','\n')
    t.value=t.value.replace("\\'","\'")
    t.value=t.value.replace('\\\\','\\')
    return t


# Comentario multilinea 
def t_COMENTARIO_MULTILINEA(t):
    r'\#\*(.|\n)*\*\#'
    t.lexer.lineno += t.value.count('\n')
    
# Comentario simple 
def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += t.value.count('\n')

# Caracteres ignorados
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


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
from Instrucciones.Main import Main
from Instrucciones.Funcion import Funcion
from Instrucciones.Llamada import Llamada


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
                        | asignacion_instr finins
                        | asignacion2_instr finins
                        | if_instr
                        | while_instr
                        | break_instr finins
                        | main_instr
                        | funcion_instr
                        | llamada_instr finins'''
    t[0] = t[1]

def p_finins(t) :
    '''finins       : PUNTOCOMA
                    | '''
    t[0] = None

def p_instruccion_error(t):
    'instruccion        : error PUNTOCOMA'
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
    asignacion2_instr     : ID expresion
    '''
    t[0] = Asignacion(t[1], t[2], t.lineno(1), find_column(input, t.slice[1]))

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
    
#///////////////////////////////////////MAIN//////////////////////////////////////////////////

def p_main(t) :
    'main_instr     : RMAIN PARA PARC LLAVEA instrucciones LLAVEC'
    t[0] = Main(t[5], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////FUNCION//////////////////////////////////////////////////

def p_funcion(t) :
    'funcion_instr     : RFUNC ID PARA PARC LLAVEA instrucciones LLAVEC'
    t[0] = Funcion(t[2], t[6], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////LLAMADA A FUNCION//////////////////////////////////////////////////

def p_llamada(t) :
    'llamada_instr     : ID PARA PARC'
    t[0] = Llamada(t[1], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////TIPO//////////////////////////////////////////////////

def p_tipo(t) :
    '''tipo     : RINT
                | RDOUBLE
                | RCHAR
                | RSTRING
                | RVAR
                | RBOOLEAN '''
    if t[1] == 'int':
        t[0] = TIPO.ENTERO
    elif t[1] == 'double':
        t[0] = TIPO.DECIMAL
    elif t[1] == 'char':
        t[0] = TIPO.CHARACTER
    elif t[1] == 'string':
        t[0] = TIPO.CADENA
    elif t[1] == 'boolean':
        t[0] = TIPO.BOOLEANO
    elif t[1] == 'var':
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
            | expresion INCREMENTO
            | expresion DECREMENTO
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
    elif t[2] == '!=':
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
    
def p_primitivo_incremento(t):
    '''expresion : INCREMENTO'''
    t[0] = Primitivos(TIPO.INCREMENTO,"++", t.lineno(1), find_column(input, t.slice[1]))
    
def p_primitivo_decremento(t):
    '''expresion : DECREMENTO'''
    t[0] = Primitivos(TIPO.DECREMENTO,"--", t.lineno(1), find_column(input, t.slice[1]))

# Se parsea
parser = yacc.yacc()
input = ''


def getErrores():
    return errores


def parse(inp):
    global errores
    global lexer
    global parser
    errores = []
    lexer = lex.lex(reflags= re.IGNORECASE)
    parser = yacc.yacc()
    global input
    input = inp
    return parser.parse(inp)


# Metodo que conecta con el frontend (INTERFAZ)
def analizar(texto):
    entrada = texto
    contador = 0
    # ARBOL AST
    instrucciones = parse(entrada.lower())
    ast = Arbol(instrucciones)
    TSGlobal = TablaSimbolos()
    ast.setTSglobal(TSGlobal)
    for error in errores:
        # Metodo para capturar errores
        ast.getExcepciones().append(error)
        ast.updateConsola(error.toString())
    if ast.getInstrucciones()!=None:
        # Toma declaraciones y asignaciones
        for instruccion in ast.getInstrucciones():      
            if isinstance(instruccion, Funcion):
                # Guarda la funcion
                ast.addFuncion(instruccion)  
            if isinstance(instruccion, Declaracion) or isinstance(instruccion, Asignacion):
                value = instruccion.interpretar(ast,TSGlobal)
                if isinstance(value, Excepcion) :
                    ast.getExcepciones().append(value)
                    ast.updateConsola(value.toString())
                if isinstance(value, Break): 
                    err = Excepcion("Semantico", "Sentencia BREAK fuera de ciclo", instruccion.fila, instruccion.columna)
                    ast.getExcepciones().append(err)
                    ast.updateConsola(err.toString())
        # Toma el Main
        for instruccion in ast.getInstrucciones():      
            if isinstance(instruccion, Main):
                contador += 1
                # Verifica solo 1 main
                if contador == 2: 
                    err = Excepcion("Semantico", "Existen 2 funciones Main", instruccion.fila, instruccion.columna)
                    ast.getExcepciones().append(err)
                    ast.updateConsola(err.toString())
                    break
                value = instruccion.interpretar(ast,TSGlobal)
                if isinstance(value, Excepcion) :
                    ast.getExcepciones().append(value)
                    ast.updateConsola(value.toString())
                if isinstance(value, Break): 
                    err = Excepcion("Semantico", "Sentencia BREAK fuera de ciclo", instruccion.fila, instruccion.columna)
                    ast.getExcepciones().append(err)
                    ast.updateConsola(err.toString())
        # Toma todo lo que esta fuera del main
        for instruccion in ast.getInstrucciones():    
            if not (isinstance(instruccion, Main) or isinstance(instruccion, Declaracion) or isinstance(instruccion, Asignacion) or isinstance(instruccion, Funcion)):
                err = Excepcion("Semantico", "Sentencias fuera de Main", instruccion.fila, instruccion.columna)
                ast.getExcepciones().append(err)
                ast.updateConsola(err.toString())
        
    return ast.getConsola()
