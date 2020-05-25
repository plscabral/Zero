from tkinter import *
import NameFind
import Recogniser_Video_LBPHFace


def Abrir():
    import Tela_principal
    NameFind.AbrirURL(Recogniser_Video_LBPHFace.Recogniser.ID)


# Inicio app root
root = Tk()
root.title("ZERO - Menu")
root.iconbitmap("logo.ico")
root.geometry("265x100")
root.resizable(width=FALSE, height=FALSE)

# Titulo
titulo = Label(root, text='Abrir!', font='Arial 10 bold')
titulo.place(x=20, y=10)

# Config btnIniciarSessao
btnAbrir = Button(root, text='Abrir', command=Abrir)
btnAbrir.place(x=120, y=50)

root.mainloop()