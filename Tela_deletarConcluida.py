from tkinter import *
import cv2

def Encerrar():
    root.destroy()
    cv2.destroyAllWindows()

# Inicio app root
root = Tk()
root.title("ZERO - Deletar")
root.iconbitmap("logo.ico")
root.geometry("265x100")
root.resizable(width=FALSE, height=FALSE)

# Titulo
titulo = Label(root, text='Dados deletados com sucesso!!', font='Arial 10 bold')
titulo.place(x=30, y=10)

# Config btnIniciarSessao
btnEncerrar = Button(root, text='OK', command=Encerrar)
btnEncerrar.place(x=120, y=50)

root.mainloop()