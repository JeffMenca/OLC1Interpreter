''' 
Jeffrey Menendez
Proyecto de Organizacion de lenguajes y compiladores 1

JPR Interpreter
'''

#Imports
import re
import os
import io
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import ttk
from grammar import analizar as analizador
from grammar import getErrores as listaErrores
from grammar import getVariables as listaVariables
from grammar import getFunciones as listaFunciones
from TS.TablaSimbolos import TablaSimbolos as tablaSimbolos


# Variables globales
# Path del archivo en memoria
archivo = ""   
# Metodos
# Actualizar lineas
def lineas(*args):
    lines.delete("all")

    cont = editor.index("@1,0")
    while True:
        dline = editor.dlineinfo(cont)
        if dline is None:
            break
        y = dline[1]
        strline = str(cont).split(".")[0]
        lines.create_text(2, y, anchor="nw", text=strline,
                          font=("Consolas", 10))
        cont = editor.index("%s+1line" % cont)

# Actualizar posicion
def posicion(event=None):
    lbPosicion.config(
        text="Linea: " + str(editor.index(INSERT)).replace(".", ", Columna: "))

# Recorrer el texto para separar palabras por colores
def recorrerInput(i):  
    lista = []
    val = ''
    counter = 0
    while counter < len(i):
            if re.search(r"[a-z|0-9|.|A-Z]", i[counter]):
                val += i[counter]
            elif i[counter] == "\"":
                if len(val) != 0:
                    l = []
                    l.append("cadena")
                    l.append(val)
                    lista.append(l)
                    val = ''
                val = i[counter]
                counter += 1
                
                while counter < len(i):
                    if i[counter] == "\"":
                        val += i[counter]
                        l = []
                        l.append("cadena")
                        l.append(val)
                        lista.append(l)
                        val = ''
                        break
                    val += i[counter]
                    counter += 1
            elif i[counter] == "#":
                if len(val) != 0:
                    l = []
                    l.append("comentario")
                    l.append(val)
                    lista.append(l)
                    val = ''
                val = i[counter]
                counter += 1
                if i[counter] == "*":
                   while counter < len(i):
                        if i[counter] == "#":
                            val += i[counter]
                            l = []
                            l.append("comentario")
                            l.append(val)
                            lista.append(l)
                            val = ''
                            break
                        val += i[counter]
                        counter += 1 
                else:    
                    while counter < len(i):
                        if i[counter] == "\n":
                            val += i[counter]
                            l = []
                            l.append("comentario")
                            l.append(val)
                            lista.append(l)
                            val = ''
                            break
                        val += i[counter]
                        counter += 1
            elif i[counter] == "\'":
                if len(val) != 0:
                    l = []
                    l.append("variable")
                    l.append(val)
                    lista.append(l)
                    val = ''
                val = i[counter]
                counter += 1
                while counter < len(i):
                    if i[counter] == "\'":
                        val += i[counter]
                        l = []
                        l.append("cadena")
                        l.append(val)
                        lista.append(l)
                        val = ''
                        break
                    val += i[counter]
                    counter += 1
            else:
                if len(val) != 0:
                    l = []
                    l.append("variable")
                    l.append(val)
                    lista.append(l)
                    val = ''
                l = []
                l.append("otro")
                l.append(i[counter])
                lista.append(l)
            counter +=1
    for s in lista:
        if s[1] == 'var' or s[1] == 'func' or s[1] == 'read' or s[1] == 'tolower' or s[1] == 'toupper' or s[1] == 'lenght' or s[1] == 'truncate' or s[1] == 'round' or s[1] == 'typeof' or s[1] == 'return' or s[1] == 'break' or s[1] == 'switch' or s[1] == 'case' or s[1] == 'default' or s[1] == 'false' or s[1] == 'true' or s[1] == 'while' or s[1] == 'for' or s[1] == 'continue' or  s[1] == 'else' or s[1] == 'if' or s[1] == 'null' or s[1] == 'boolean' or s[1] == 'string' or s[1] == 'int' or s[1] == 'double' or s[1] == 'char' or s[1] == 'print' or s[1] == 'main':
            s[0] = 'reservada'
        elif re.search(r'\d+',s[1]) or re.search(r'\d+\.\d+',s[1]):
            if re.search(r'\".*?\"',s[1]):
                s[0] = 'cadena'
            elif re.search(r'\#\*(.|\n)*?\*\#|\#.*\n',s[1]):
                s[0] = 'comentario'
            elif re.search(r'[a-z|A-Z]',s[1]):
                s[0]= "otro"
            else:
                s[0] = 'numero'
        elif re.search(r'\".*?\"',s[1]):
            s[0] = 'cadena'
        elif re.search(r'\#\*(.|\n)*?\*\#|\#.*\n',s[1]):
            s[0] = 'comentario'
    return lista

# Llamar metodos
def llamarMetodos(event):
    posicion()
    lineas()
# Nuevo archivo
def nuevo():   
    global archivo
    editor.delete(1.0, END)
    archivo = ""
# Abrir archivo
def abrir():       
    global archivo
    archivo = filedialog.askopenfilename(title = "Abrir Archivo", initialdir = "C:/",filetypes=[("jpr files", ".jpr")])
    entrada = io.open(archivo, 'r',encoding="utf8")
    content = entrada.read()
    editor.delete(1.0, END)
    for s in recorrerInput(content):
        editor.insert(INSERT, s[1], s[0])
    entrada.close()
    lineas()
# Guardar archivo
def guardarArchivo():  
    global archivo
    if archivo == "":
        guardarComo()
    else:
        guardarc = open(archivo, "w")
        guardarc.write(editor.get(1.0, END))
        guardarc.close()
        contenido2= editor.get(1.0, END)
        editor.delete(1.0, "end")
        for s in recorrerInput(contenido2):
            editor.insert(INSERT, s[1], s[0])
# Guardar archivo como
def guardarComo():      
    global archivo
    guardar = filedialog.asksaveasfilename(title = "Guardar Archivo", initialdir = "C:/",filetypes=[("jpr files", ".jpr")],defaultextension='.jpr')
    fguardar = open(guardar, "w+")
    fguardar.write(editor.get(1.0, END))
    fguardar.close()
    archivo = guardar
    contenido2= editor.get(1.0, END)
    editor.delete(1.0, "end")
    for s in recorrerInput(contenido2):
        editor.insert(INSERT, s[1], s[0])
    
 # Analizar
def analizar():   
    console.delete(1.0, "end")
    contenido=analizador(editor.get(1.0, END),console)
    console.insert(INSERT, contenido)
    errores=listaErrores()
    variables=listaVariables()
    funciones=listaFunciones()
    contador=1
    contador2=1
    tv1.delete(*tv1.get_children())
    tv.delete(*tv.get_children())
    for error in errores:
        tv1.insert(parent='', index=contador, iid=contador, text='', values=(contador,error.getTipo(),error.getDescripcion(),error.getFila(),error.getColumna()))
        contador+=1
    contenido2= editor.get(1.0, END)
    editor.delete(1.0, "end")
    for s in recorrerInput(contenido2):
        editor.insert(INSERT, s[1], s[0])
           
    for variable in variables:
        tv.insert(parent='', index=contador2, iid=contador2, text='', values=(contador2,variable.getID(),"Variable",variable.getTipo(),variable.getEntorno(),variable.getValor(),variable.getFila(),variable.getColumna()))
        contador2+=1
        
    for funcion in funciones:
        if funcion.getNombre()=="round" or funcion.getNombre()=="toupper" or funcion.getNombre()=="tolower" or funcion.getNombre()=="length" or funcion.getNombre()=="truncate" or funcion.getNombre()=="typeof":
            continue
        else:
            tv.insert(parent='', index=contador2, iid=contador2, text='', values=(contador2,funcion.getNombre(),"Funcion",funcion.getTipo(),"----","----",funcion.getFila(),funcion.getColumna()))
            contador2+=1
    
    
# Reportes
def reporteErrores():
    archivo = "reporteErrores.dot"
    salida = "digraph errores {\n"
    salida += "tbl [\n shape = plaintext\n"
    salida += "label=<\n"
    salida += "<table border=\"1\" bgcolor=\"cadetblue2\">\n"
    salida += "<tr> <td colspan='5'>Reporte de errores</td> </tr> \n"
    salida += "<tr> <td>#</td> <td>Tipo</td> <td>Descripcion</td> <td>Linea</td> <td>Columna</td> </tr> \n"
    excepciones = listaErrores()
    cont = 1
    for excepcion in excepciones:
        salida += "<tr> <td>"+str(cont)+"</td> <td>"+excepcion.getTipo()+"</td> <td>"+excepcion.getDescripcion()+"</td> <td>"+str(excepcion.getFila())+"</td> <td>"+str(excepcion.getColumna())+"</td> </tr> \n"
        cont += 1
    salida += "</table>\n"
    salida += ">];\n"
    salida += "}"
    with open(archivo,'w') as f:
        f.write(salida) 
    os.system('dot -Tpng '+archivo+' -o reporteErrores.png')
    os.startfile("reporteErrores.png") 
def reporteArbol():
    os.startfile("ast.pdf")
    
def reporteSimbolos():
    archivo = "reporteSimbolos.dot"
    salida = "digraph simbolos {\n"
    salida += "tbl [\n shape = plaintext\n"
    salida += "label=<\n"
    salida += "<table border=\"1\" bgcolor=\"cadetblue2\">\n"
    salida += "<tr> <td colspan='5'>Reporte de simbolos</td> </tr> \n"
    salida += "<tr> <td>#</td> <td>ID</td> <td>Tipo</td> <td>Tipo2</td> <td>Entorno</td> <td>Valor</td> <td>Linea</td> <td>Columna</td> </tr> \n"
    variables = listaVariables()
    funciones=listaFunciones()
    cont = 1
    for variable in variables:
        salida += "<tr> <td>"+str(cont)+"</td> <td>"+str(variable.getID())+"</td> <td>"+"Variable"+"</td> <td>"+str(variable.getTipo())+"</td> <td>"+str(variable.getEntorno())+"</td> <td>"+str(variable.getValor())+"</td> <td>"+str(variable.getFila())+"</td> <td>"+str(variable.getColumna())+"</td> </tr> \n"
        cont += 1
    for funcion in funciones:
        if funcion.getNombre()=="round" or funcion.getNombre()=="toupper" or funcion.getNombre()=="tolower" or funcion.getNombre()=="length" or funcion.getNombre()=="truncate" or funcion.getNombre()=="typeof":
            continue
        else:
            salida += "<tr> <td>"+str(cont)+"</td> <td>"+str(funcion.getNombre())+"</td> <td>"+"Funcion"+"</td> <td>"+str(funcion.getTipo())+"</td> <td>"+"---"+"</td> <td>"+"---"+"</td> <td>"+str(funcion.getFila())+"</td> <td>"+str(funcion.getColumna())+"</td> </tr> \n"
            cont += 1
    salida += "</table>\n"
    salida += ">];\n"
    salida += "}"
    with open(archivo,'w') as f:
        f.write(salida) 
    os.system('dot -Tpng '+archivo+' -o reporteSimbolos.png')
    os.startfile("reporteSimbolos.png") 

        
# Declaracion del tk
raiz = Tk()
raiz.title("JPR Editor")
# Frame principal
frame = Frame(raiz, bg="gray12")
frame.grid(sticky='news')
# Canvas
canvas = Canvas(frame, bg="gray12")
canvas.grid(row=0, column=1)
# Frame del canvas
ventana = Frame(canvas, bg="gray12")
canvas.create_window((0, 0), window=ventana, anchor="nw")
canvas.configure(width=1150, height=700)

# Componentes
# Label de fila y columna
lbPosicion= Label(ventana, text="Fila: 0, Columna: 0",width=76)
lbPosicion.grid(column=0, row=3,sticky="nw",padx=25,pady=50)
# Label de resultado
lbResultado= Label(ventana, text="Resultado del interprete",width=71)
lbResultado.grid(column=1, row=3,sticky="nw",padx=0,pady=50)
# ScrolledText del editor
editor = scrolledtext.ScrolledText(ventana, undo=True, width=60, height=15,background='grey12',foreground='white')
editor.grid(column=0, row=3, pady=75, padx=60)
# ScrolledText de la consola
console = scrolledtext.ScrolledText(ventana, undo=True, width=60, height=15,background='black',foreground='SpringGreen2')
console.grid(column=1, row=3, pady=75, padx=0,sticky="w")
# Canvas de fila del editor
lines = Canvas(ventana, width=30, height=240, background='gray60')
lines.grid(column=0, row=3,padx=25,sticky="w")
# Boton de analizar
boton1= Button(ventana,text="Analizar",width=12,height=2,background='grey12',font="Helvetica 15",foreground='SpringGreen2',command=analizar)
boton1.grid(row=0,column=1,sticky="e")
# Menu bar
menu = Menu(ventana)
# Archivo
new_item = Menu(menu,tearoff=0)
new_item.add_command(label='Nuevo',command=nuevo)
new_item.add_command(label='Abrir',command=abrir)
new_item.add_command(label='Guardar',command=guardarArchivo)
new_item.add_command(label='Guardar como',command=guardarComo)
menu.add_cascade(label='Archivo', menu=new_item)
# Analizar
new_item = Menu(menu,tearoff=0)
new_item.add_command(label='Analizar')
menu.add_cascade(label='Analizar', menu=new_item)
# Reportes
new_item = Menu(menu,tearoff=0)
new_item.add_command(label='Simbolos',command=reporteSimbolos)
new_item.add_command(label='Errores',command=reporteErrores)
new_item.add_command(label='Arbol AST',command=reporteArbol)
menu.add_cascade(label='Reportes', menu=new_item)
raiz.config(menu=menu)

#Titulo
Label(ventana,text="JPR Editor",font="Helvetica 25",foreground='DodgerBlue2',background='gray12').grid(row=0,column=0,sticky="e")
#Label Tabla de Simbolos
Label(ventana,text="Tabla de Simbolos",font="Helvetica 15",foreground='green2',background='gray12').grid(row=4,column=0)
#Label Tabla de Errores
Label(ventana,text="Tabla de Errores",font="Helvetica 15",foreground='red2',background='gray12').grid(row=4,column=1)

#Tabla De Simbolos
tv=ttk.Treeview(ventana,height=7)
tv['columns']=('#', 'Identificador', 'Tipo','Tipo2', 'Entorno', 'Valor', 'Linea', 'Columna')
tv.column('#0', width=0, stretch=NO)
tv.column('#', anchor=CENTER, width=20)
tv.column('Identificador', anchor=CENTER, width=90)
tv.column('Tipo', anchor=CENTER, width=80)
tv.column('Tipo2', anchor=CENTER, width=80)
tv.column('Entorno', anchor=CENTER, width=60)
tv.column('Valor', anchor=CENTER, width=80)
tv.column('Linea', anchor=CENTER, width=60)
tv.column('Columna', anchor=CENTER, width=70)
tv.heading('#0', text='', anchor=CENTER)
tv.heading('#', text='#', anchor=CENTER)
tv.heading('Identificador', text='Identificador', anchor=CENTER)
tv.heading('Tipo', text='Tipo', anchor=CENTER)
tv.heading('Tipo2', text='Tipo2', anchor=CENTER)
tv.heading('Entorno', text='Entorno', anchor=CENTER)
tv.heading('Valor', text='Valor', anchor=CENTER)
tv.heading('Linea', text='Linea', anchor=CENTER)
tv.heading('Columna', text='Columna', anchor=CENTER)
tv.grid(column=0, row=5,padx=25,pady=15,sticky="w")

#Tabla Reporte de errores
tv1=ttk.Treeview(ventana,height=7)
tv1['columns']=('#', 'Tipo', 'Descripcion', 'Linea', 'Columna')
tv1.column('#0', width=0, stretch=NO)
tv1.column('#', anchor=CENTER, width=10)
tv1.column('Tipo', anchor=CENTER, width=100)
tv1.column('Descripcion', anchor=CENTER, width=250)
tv1.column('Linea', anchor=CENTER, width=70)
tv1.column('Columna', anchor=CENTER, width=70)
tv1.heading('#0', text='', anchor=CENTER)
tv1.heading('#', text='#', anchor=CENTER)
tv1.heading('Tipo', text='Tipo', anchor=CENTER)
tv1.heading('Descripcion', text='Descripcion', anchor=CENTER)
tv1.heading('Linea', text='Linea', anchor=CENTER)
tv1.heading('Columna', text='Columna', anchor=CENTER)
tv1.grid(row=5,column=1,pady=15)

# Estilo tabla
style=ttk.Style()
style.theme_use("default")
style.configure("Treeview",
    foreground='white',
    background="grey75",
    fieldbackground="grey35")

style.map('Treeview',background=[('selected','DodgerBlue2')])

# Tags para pintar el texto
editor.tag_config('reservada', foreground='DodgerBlue2')
editor.tag_config('cadena', foreground='orange')
editor.tag_config('numero', foreground='purple2')
editor.tag_config('comentario', foreground='gray')
editor.tag_config('otro', foreground='green2')

# Acciones del teclado
editor.bind('<Return>', llamarMetodos)
editor.bind('<BackSpace>', llamarMetodos)
editor.bind('<<Change>>', llamarMetodos)
editor.bind('<Configure>', llamarMetodos)
editor.bind('<Motion>', llamarMetodos)
editor.bind('<KeyPress>', posicion)
editor.bind('<KeyRelease>', llamarMetodos)
editor.bind('<Button>', posicion)
editor.bind('<Key>', llamarMetodos)
editor.bind('<Enter>', llamarMetodos)


# Main loop
raiz.mainloop()
