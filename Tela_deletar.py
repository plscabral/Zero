from tkinter import *
import NameFind


def DeletarDados():
    import Recogniser_Video_LBPHFace
    ID = Recogniser_Video_LBPHFace.Recogniser.ID
    NameFind.excluirCadastro(ID)
    root.destroy()
    import Tela_deletarConcluida

def Cancelar():
    root.destroy()
    import Tela_principal

# Inicio app root
root = Tk()
root.title("ZERO - Deletar")
root.iconbitmap("logo.ico")
root.geometry("300x100")
root.resizable(width=FALSE, height=FALSE)

# Titulo
titulo = Label(root, text='Você deseja excluir seus dados?', font='Arial 10 bold')
titulo.place(x=40, y=10)

# Config btnIniciarSessao
btnDeletarDados = Button(root, text='Confirmar', command=DeletarDados)
btnDeletarDados.place(x=80, y=50)

btnCancelar = Button(root, text='Cancelar', command=Cancelar)
btnCancelar .place(x=160, y=50)

root.mainloop()