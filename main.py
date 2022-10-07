import tkinter.messagebox
from tkinter import messagebox
from tkinter import *
import random

# INICIO DEL PROGRAMA PARA GENERAR LAS CONTRASEÑAS


def generar_contraseñas():
    texto_contraseña.delete(1.0, END)
    texto_contraseña.insert(END, f'Contraseñas seguras:\n\n')
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v',
              'w', 'x', 'y', 'z']
    signos = ['{', '=', '.', ',', ';', ':', '&', '}', '(', ')', '/', '$', '#', '@', '!', '?', '*', '-']
    password = []
    contra = []
    cont = 0

    def elegir_letra():
        for i in range(1, 10):
            tamanio = len(letras) - 1
            password.append(letras[random.randint(1, tamanio)])

        for letra in range(1, len(password) - 1, 4):
            let = str(password[letra])
            contra.append(let.upper())
            password.pop(letra)

    def elegir_numero():
        for x in range(1, 5):
            tamnio = len(numeros) - 1
            password.append(numeros[random.randint(1, tamnio)])

    def elegir_signo():
        for x in range(1, 3):
            tamnio = len(signos) - 1
            password.append(signos[random.randint(1, tamnio)])

    def comprobrar_repeticion(lista):
        dup = {x for x in lista if lista.count(x) > 1}
        # print(dup,len(dup))
        n1 = 0
        n2 = 1
        if len(dup) >= 1:
            lista.clear()
            return lista, n1
        else:
            return lista, n2

    while cont < 10:
        elegir_letra()
        elegir_numero()
        elegir_signo()

        pas = password + contra

        random.shuffle(pas)
        random.shuffle(pas)

        x, conta = comprobrar_repeticion(pas)
        cont += conta

        if len(x) > 1:
            contra = ''.join(x)
            texto_contraseña.insert(END, f'{cont}.- {contra}\n')
            # print(f'{contra}')

        contra = []
        password = []


def generar_palabra_clave(plb):
    signos = ['{', '=', '.', ',', ';', ':', '&', '}', '(', ')', '/', '$', '#', '@', '!', '?', '*', '-']
    password = []

    def cambio_letras():
        palabra =plb
        letras = palabra.replace('A', '4')
        letras = letras.replace('B', '8')
        letras = letras.replace('I', '1')
        letras = letras.replace('G', '6')
        letras = letras.replace('S', '5')
        letras = letras.replace('T', '7')
        letras = letras.replace('o', '0')
        letras = letras.replace('3', 'E')
        palabra_numeros = list(letras)
        return palabra_numeros

    def elegir_signo():
        for x in range(1, 3):
            tamnio = len(signos) - 1
            password.append(signos[random.randint(1, tamnio)])

    con_numeros = cambio_letras()
    elegir_signo()
    pas = con_numeros + password
    pas_junta = ''.join(pas)
    return pas_junta


def crear():
    if variable_palabra.get() == 1 and texto_palabra.get() != '':
        texto_contraseña.delete(1.0, END)
        clave = texto_palabra.get()
        texto_contraseña.insert(END, f'{generar_palabra_clave(clave)}')
    elif variable_palabra.get() == 1 and texto_palabra.get() == '':
        tkinter.messagebox.showwarning(title=None, message='Ingrese palabra/oración')
    else:
        generar_contraseñas()
        texto_contraseña.config(state=NORMAL)

# FIN DEL PROGRAMA PARA GENERAR LAS CONTRASEÑAS


def revisar_check():
    if variable_palabra.get() == 1:
        cuadro_palabra.config(state=NORMAL)
        cuadro_palabra.delete(0, END)
        cuadro_palabra.focus()
        # boton_generar.config(state=DISABLED)
    else:
        cuadro_palabra.config(state=DISABLED)
        texto_palabra.set('Sin palabra clave')
        # boton_generar.config(state=NORMAL)



# iniciar tkinte
aplicacion = Tk()

# tamaño de la ventana
aplicacion.geometry('450x650')

# evitar maximizar
aplicacion.resizable(0,0)

# titulo de la ventana
aplicacion.title("Generador de contraseñas seguras")

# color de fondo de pantalla
aplicacion['background'] = '#1F2833'

# panel superior
panel_superior = Frame(aplicacion, bd=0, relief=FLAT)
panel_superior.pack(side=TOP)

# etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Generador de contraseñas seguras', fg='#c5c6c7',
                        font=('Dosis', 20), bg='#1F2833', width=27)
etiqueta_titulo.grid(row=0, column=0)

# panel inferior
panel_inferior = Frame(aplicacion, bd=0, relief=FLAT,bg='#1F2833')

panel_inferior.pack(side=TOP)

# panel palabra clave (panel donde esta el check y el label)
panel_palabra_clave = Frame(panel_inferior, bd=0, relief=FLAT, bg='#1F2833')
panel_palabra_clave.pack(side=TOP)

# panel contraseña generada
panel_contraseña_generada = Frame(panel_inferior, bd=1, relief=FLAT, bg='#45A29E')
panel_contraseña_generada.pack(side=TOP)

# texto donde se muestran las contraseñas
texto_contraseña = Text(panel_contraseña_generada,
                        font=('Dosis', 10, 'bold'),
                        fg='#C5C6C7',
                        bd=1,
                        width=42,
                        height=15,
                        bg='#1F2833')
texto_contraseña.grid(row=0,
                      column=0)


# panel boton
panel_boton = Frame(panel_inferior, bd=1, relief=FLAT, bg='#45A29E')
panel_boton.pack(side=BOTTOM, pady=50)

# boton de generar
boton_generar = Button(panel_boton, text='Generar', font=('Dosis', 13,'bold'),
                       fg='#66FCF1',bg='#0B0C10', bd=1, width=8)
boton_generar.grid(row=0, column=0, ipady=10)

# generar item comida
variable_palabra = ''
variable_palabra = IntVar()
cuadro_palabra = ''
texto_palabra = ''

texto_palabra = StringVar()
texto_palabra = set('0')


# check palabra clave
check_Palabra = Checkbutton(panel_palabra_clave,
                            text='Palabra clave',
                            font=('Dosis', 12, 'bold'),
                            fg='#66FCF1',
                            onvalue=1,
                            offvalue=0,
                            bg='#1F2833',
                            activebackground='#45A29E',
                            variable=variable_palabra,
                            command=revisar_check)
check_Palabra.grid(row=1,
                   column=0,
                   sticky=W,
                   padx=15, ipady=4, pady=8)

# crear los cuadros de entrada
texto_palabra = StringVar()
texto_palabra.set('Sin palabra clave')

cuadro_palabra = Entry(panel_palabra_clave,
                       font=('Dosis', 10, 'bold'),
                       bd=1,
                       width=20,
                       state=DISABLED,
                       textvariable=texto_palabra)
cuadro_palabra.grid(row=0, column=0, ipady=5, pady=15)










# funcion del boton
boton_generar.config(command=crear)

# evitar que la pantalla se cierre
aplicacion.mainloop()