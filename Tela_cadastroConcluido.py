from tkinter import *
import NameFind

def FecharJanela():
    root.destroy()
    NameFind.abrirPrograma()
    
# Inicio app root
root = Tk()
root.title("ZERO - Cadastro")
root.iconbitmap("logo.ico")
root.geometry("265x100")
root.resizable(width=FALSE, height=FALSE)

# Titulo
titulo = Label(root, text='Cadastro Concluído com Sucesso!', font='Arial 10 bold')
titulo.place(x=20, y=10)

# Config btnIniciarSessao
btnFecharJanela = Button(root, text='OK', command=FecharJanela)
btnFecharJanela.place(x=120, y=50)

root.mainloop()