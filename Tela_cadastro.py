from tkinter import *
import NameFind

# Funções
def EnviarDados():
    NameFind.AddName(nome.get(),site1.get(),site2.get(),site3.get(),site4.get(),site5.get())
    root.destroy()
    import Face_Capture_With_Rotate

# Inicio app root
root = Tk()
root.title("ZERO - Cadastro")
root.iconbitmap("logo.ico")
root.geometry("300x260")
root.resizable(width=FALSE, height=FALSE)

# Titulo
titulo = Label(root, text='Preencha os dados abaixo', font='Arial 10 bold')
titulo.place(x=60, y=0)

# Label e Entry --> Nome
nomeLabel = Label(root, text='Nome:', font='Arial 10')
nomeLabel.place(x=10, y=25)
nome = Entry(root, width= 37)
nome.place(x=60, y=25)

# Titulo2
titulo2 = Label(root, text='Sites Favoritos', font='Arial 10 bold')
titulo2.place(x=100, y=50)

# Label e Entry --> Site1
site1label = Label(root, text='1º Site', font='Arial 10')
site1label.place(x=10, y= 80)
site1 = Entry(root, width=37)
site1.place(x=60, y=80)

# Label e Entry --> Site2
site2label = Label(root, text='2º Site', font='Arial 10')
site2label.place(x=10, y= 110)
site2 = Entry(root, width=37)
site2.place(x=60, y=110)

# Label e Entry --> Site3
site3 = Label(root, text='3º Site', font='Arial 10')
site3.place(x=10, y= 140)
site3 = Entry(root, width=37)
site3.place(x=60, y=140)

# Label e Entry --> Site4
site4label = Label(root, text='4º Site', font='Arial 10')
site4label.place(x=10, y= 170)
site4 = Entry(root, width=37)
site4.place(x=60, y=170)

# Label e Entry --> Site5
site5label = Label(root, text='5º Site', font='Arial 10')
site5label.place(x=10, y= 200)
site5 = Entry(root, width=37)
site5.place(x=60, y=200)

# Config btnIniciarSessao
btnEnviarDados = Button(root, text='Enviar Dados', command=EnviarDados)
btnEnviarDados.place(x=110, y=230)

root.mainloop()