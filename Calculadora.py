import tkinter as tk

#TELA
tela = tk.Tk()
tela.title("calculadora")
tela.geometry('280x380')
tela.config(bg = "pink")
tela.resizable(False,False)

#VISOR
label = tk.Label(tela,text = "Seja bem-vindo!",font =("arial"),pady= 10, bg= "pink")
label.pack()
visor = tk.Entry(tela,bg= "pink")
visor.pack()


#FUNÇÕES

def botao_click(numero):
    atual= visor.get()
    visor.delete(0,tk.END)
    visor.insert(tk.END,str(atual)+str(numero))


def igual():
    segundo_numero  = visor.get()
    visor.delete(0,tk.END)
    if matematica == "soma":
        visor.insert(0,p_numero + float(segundo_numero))

    if matematica == "subtraçao":
        visor.insert(0,p_numero - float(segundo_numero))

    if matematica == "multiplicaçao":
        visor.insert(0,p_numero * float(segundo_numero))

    if matematica== "divisao":
        visor.insert(0,p_numero / float(segundo_numero))

def botao_ponto():
    visor.insert(tk.END,".")

def deletar():
    visor.delete(0,tk.END)

def soma():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica= "soma"
    p_numero = float(primeiro_numero)
    visor.delete(0,tk.END)

def subtr():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica= "subtraçao"
    p_numero = float(primeiro_numero)
    visor.delete(0,tk.END)


def mult():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica= "multiplicaçao"
    p_numero = float(primeiro_numero)
    visor.delete(0,tk.END)


def divisao():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica= "divisao"
    p_numero = float(primeiro_numero)
    visor.delete(0,tk.END)


#BOTÕES #FILEIRA1
botao1 = tk.Button(tela,text = "1", bg= "white", pady = 14,padx =14,bd=4,command=lambda:botao_click("1"))
botao1.place(x=10, y=100)

botao2= tk.Button(tela,text = "2", bg= "white", pady = 14,padx =14,bd=4,command=lambda:botao_click("2") )
botao2.place(x=10, y=155)

botao3 = tk.Button(tela,text = "3", bg= "white", pady = 14,padx =14,bd=4, command=lambda:botao_click("3") )
botao3.place(x=10,y= 210)

botao0 = tk.Button(tela,text = "0", bg= "white", pady = 14,padx =40,bd=4,command=lambda:botao_click("0") )
botao0.place(x=10,y= 265)

#FILEIRA 2
botao4 = tk.Button(tela,text = "4", bg= "white", pady = 14,padx =14,bd=4,command=lambda:botao_click("4") )
botao4.place(x=60, y=100)

botao5 = tk.Button(tela,text = "5", bg= "white", pady = 14,padx =14,bd=4,command=lambda:botao_click("5") )
botao5.place(x=60, y=155)

botao6 = tk.Button(tela,text = "6", bg= "white", pady = 14,padx =14,bd=4,command=lambda:botao_click("6") )
botao6.place(x=60, y=210)

#FILEIRA 3
botao7 = tk.Button(tela,text = "7", bg= "white", pady = 14,padx =14,bd=4,command=lambda:botao_click("7") )
botao7.place(x=110, y=100)

botao8 = tk.Button(tela,text = "8", bg= "white", pady = 14,padx =14,bd=4,command=lambda:botao_click("8") )
botao8.place(x=110, y=155)

botao9= tk.Button(tela,text = "9", bg= "white", pady = 14,padx =14,bd=4,command=lambda:botao_click("9") )
botao9.place(x=110, y=210)

botaoP= tk.Button(tela,text = ".", bg= "white", pady = 14,padx =14,bd=4,command=lambda:botao_ponto())
botaoP.place(x=110, y=265)

#FILEIRA 4
botaoSOMA = tk.Button(tela,text = "+", bg= "violet", pady = 14,padx =14,bd=4,command=lambda:soma())
botaoSOMA.place(x=160, y=100)

botaoSUBT = tk.Button(tela,text = "-", bg= "violet", pady = 14,padx =14,bd=4,command=lambda:subtr())
botaoSUBT.place(x=160, y=155)

botaoMULT = tk.Button(tela,text = "*", bg= "violet", pady = 14,padx =14,bd=4, command=lambda:mult())
botaoMULT.place(x=160, y=210)

botaoDIVI = tk.Button(tela,text = "/", bg= "violet", pady = 14,padx =14,bd=4,command=lambda:divisao())
botaoDIVI.place(x=160, y=265)

#BOTA C
botaoC = tk.Button(tela,text = "C", bg= "white", pady = 119,padx =14,bd=4,command=lambda:deletar())
botaoC.place(x=210, y=100)

#BOTAO =
botao = tk.Button(tela,text = "=", bg= "white", pady = 14,padx =119,bd=4,command=lambda:igual())
botao.place(x=10, y=320)


tela.mainloop()