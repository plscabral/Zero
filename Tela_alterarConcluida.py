from tkinter import *

def FecharJanela():
    root.destroy()

# Inicio app root
root = Tk()
root.title("ZERO - Alterar")
root.iconbitmap("logo.ico")
root.geometry("265x100")
root.resizable(width=FALSE, height=FALSE)

# Titulo
titulo = Label(root, text='Alteração concluída com sucesso!', font='Arial 10 bold')
titulo.place(x=20, y=10)

# Config btnIniciarSessao
btnFecharJanela = Button(root, text='OK', command=FecharJanela)
btnFecharJanela.place(x=120, y=50)

root.mainloop()