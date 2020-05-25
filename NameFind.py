#     ----------- FUNÇÃO PARA LER O ARQUIVO E ADICIONAR OS NOMES E IDs NOS TUPLES
import webbrowser

import cv2 # Biblioteca de captura de vídeo
import math # Biblioteca de rotação de imagens
import time # Biblioteca de contagem de tempo
import os # Biblioteca de Arquivos

now_time = time.time()

face = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml') # Classificador "face frontal" Haar Cascade
glass_cas = cv2.CascadeClassifier('Haar/haarcascade_eye_tree_eyeglasses.xml') # Classificador "olho" Haar Cascade

WHITE = [255, 255, 255] 

def FileRead():
    Info = open("Names.txt", "r")# Abrir o arquivo de texto em modo read
    NAME = []                    # A tupla para armazenar nomes
    while (True):                # Leia todas as linhas no arquivo e armazene-as em duas tuplas
        Line = Info.readline()
        if Line == '':
            break
        NAME.append(Line.split(",")[1].rstrip())
    print(NAME)
    return NAME        # Retorna a tupla com os nomes cadastrados

def GetSite():
    Info = open("Names.txt", "r")# Abrir o arquivo de texto em modo read        
    SITE = []           # A tupla para armazenar nomes
    while (True):                # Leia todas as linhas no arquivo e armazene-as em duas tuplas
        Line = Info.readline()
        if Line == '':
            break
        SITE.append(Line.split(",")[2].rstrip())
        SITE.append(Line.split(",")[3].rstrip())
        SITE.append(Line.split(",")[4].rstrip())
        SITE.append(Line.split(",")[5].rstrip())
        SITE.append(Line.split(",")[6].rstrip())
    print(SITE)
    return SITE       # Retorne as duas tuplas

Names = FileRead()    # Execute a função acima para obter a tupla de identificação e nomes
Sites = GetSite()

#     ------------------- FUNÇÃO PARA ENCONTRAR O NOME -----------------------------------------------------------

# Verificação do último ID em Names.txt (last_string)
def file_is_empty(path):
    return os.stat(path).st_size==0

with open('Names.txt') as f:
    lines = f.readlines()
    if file_is_empty('Names.txt'):
        last_string = 1
    else:
        last_row = lines[-1]
        string_last = last_row  
        for s in string_last.split(): 
            if s.isdigit():
                last_string = int(s) 
                print("A base possui: " + str(last_string) + " " + "pessoas" )

def ID2Name(ID, conf):
    
    if ID>=1 and ID<=last_string:
        NameString = "Name: " + Names[ID-1] + " Confidence: " + (str(round(conf)) ) # Encontre o nome usando o índice do ID
    else:
        NameString = " Face Not Recognised "  # Encontre o nome usando o índice do ID
    return NameString

def NOME(ID):
    if ID>=1 and ID<=last_string:
        Nome = str(Names[ID-1])
    else:
        Nome = " Face Not Recognised "
    return Nome

def AbrirURL(ID):
    if ID>=1 and ID<=last_string:

        for n in range(5):
            Site = str(Sites[((ID-1)*5)+n])
            webbrowser.open_new(Site)
            time.sleep(1)
        
            

# ------------------- ESTA FUNÇÃO LÊ O ARQUIVO E ADICIONA O NOME AO FIM DO ARQUIVO -----------------

def AddName(Name, Site1, Site2, Site3, Site4, Site5):
    
    Info = open("Names.txt", "r+")
    ID = ((sum(1 for line in Info))+1)
    Info.write(str(ID) + " , " + Name + "," + Site1 + " ," + Site2 + " ," + Site3 + " ," + Site4 + " ," + Site5 + "\n") 
    print ("Name Stored in " + str(ID))
    Info.close()
    return ID

def getID():
    Info = open("Names.txt", "r+")
    ID = ((sum(1 for line in Info)))
    return ID

# ------------------- ESTA FUNÇÃO ALTERA OS DADOS DO USUÁRIO -----------------
def alterarCadastro(ID,Nome,Site,Site2, Site3, Site4, Site5):

    if ID >= 1 and ID <= last_string:

        Names[ID - 1] = Nome
        Sites[((ID - 1) * 5) + 0] = Site
        Sites[((ID - 1) * 5) + 1] = Site2
        Sites[((ID - 1) * 5) + 2] = Site3
        Sites[((ID - 1) * 5) + 3] = Site4
        Sites[((ID - 1) * 5) + 4] = Site5
        print('Lista com os nomes alterados: {}'.format(Names))
        print('Lista com os sites alterados: {}'.format(Sites))


    # Abre o arquivo .txt para gravação
    Info = open("Names.txt", "w")  #r+

    z = ''
    n = 0
    while n <len(Names):
        NomesCadastrados = Names[n]
        for y in range(5):
            sitesUsuario = Sites[(n * 5) + y]
            z = z + sitesUsuario + ' ,'


        imprimir = ' ,' + NomesCadastrados + ',' + z
        ID = (n + 1)
        Info.write(str(ID) + imprimir.rstrip(',') + "\n")
        print(imprimir)
        print("DADOS ALTERADOS!")
        z = ''
        n+=1

    Info.close()

# ------------------- ESTA FUNÇÃO DELETA OS DADOS DO USUÁRIO -----------------
def excluirCadastro(ID):

    # Deleta o nome e sites referentes ao ID passado como parametro
    del(Names[ID - 1])
    del(Sites[(((ID - 1) * 5) + 0):(((ID - 1) * 5) + 5)])
    print("-"*50)
    print("DELETADO!")
    print(Names)
    print(Sites)
    print("-" * 50)

    # Abre o arquivo .txt para gravação
    Info = open("Names.txt", "w")  # r+

    #Inicializa as variaveis z e n
    z = ''
    n = 0

    #O while percorre a lista de nomes do Usuário.
    #O for percorre uma lista com todos os sites,e concatena somente os 5 sites de cada
    #usuario na variavel sitesUsuario, e depois grava os dados dos usuarios novamento no txt .
    while n < len(Names):
        NomesCadastrados = Names[n]
        for y in range(5):
            sitesUsuario = Sites[(n * 5) + y]
            z = z + sitesUsuario + ' ,'

        imprimir = ' ,' + NomesCadastrados + ',' + z
        novoId = (n + 1)
        Info.write(str(novoId) + imprimir.rstrip(',') + "\n")
        z = ''
        n += 1
    Info.close()

    #Abre a pasta com as imagens cadastradas do usuário.
    pasta = 'dataSet'
    for x in range(50):
        arquivo = str('User.{}.{}.jpg'.format(ID, x))
        caminho = os.path.join(pasta, arquivo)


        if arquivo in caminho:              # Exclui as Imagens .jpg referente ao ID passado como parametro.
            os.remove(caminho)
            print(f'Arquivo {arquivo} removido!')

    renomeiaImagens(pasta,ID)

def renomeiaImagens(pasta,ID):
    x=1
    y = 1
    while x <len(Names):
        for i in range(50):
            newID = ID + x

            arquivo = str('User.{}.{}.jpg'.format(newID, i))
            caminho = os.path.join(pasta, arquivo)

            novoArquivo = str('User.{}.{}.jpg'.format((newID - 1), i))
            novoCaminho2 = os.path.join(pasta, novoArquivo)

            try:
                if arquivo in caminho:
                    os.rename(caminho, novoCaminho2)
                    print(f'{caminho} PASSOU A SER: {novoCaminho2}')
                    print('New ID:'+str(newID))
            except FileNotFoundError:
                pass
        x+=1

    import Trainer_All
    cv2.destroyAllWindows()

def abrirPrograma():
    os.system(r"Recogniser_Video_LBPHFace.py")

#     --------  DESENHE A CAIXA AO REDOR DA CARA, ID E CONFIANÇA --------------------------
def DispID(x, y, w, h, NAME, Image):

    #  -------   A POSIÇÃO DA CAIXA DE IDENTIFICAÇÃO -----------------------------------

    Name_y_pos = y - 10
    Name_X_pos = x + w/2 - (len(NAME)*7/2)

    if Name_X_pos < 0:
        Name_X_pos = 0
    elif (Name_X_pos +10 + (len(NAME) * 7) > Image.shape[1]):
          Name_X_pos= Name_X_pos - (Name_X_pos +10 + (len(NAME) * 7) - (Image.shape[1]))
    if Name_y_pos < 0:
        Name_y_pos = Name_y_pos = y + h + 10
          
 #  ------------------------------------  O DESENHO DA CAIXA E ID  --------------------------------------
    
    draw_box(Image, x, y, w, h)
    
    #cv2.rectangle(Image, (int(Name_X_pos-10), int(Name_y_pos-25)),(int(Name_X_pos +10 + (len(NAME) * 7)), int(Name_y_pos-1)), (0,0,0), -2)              
    cv2.rectangle(Image, (int(Name_X_pos-10), int(Name_y_pos-25)),(int(Name_X_pos +10 + (len(NAME) * 7)), int(Name_y_pos-1)), (0,0,0), -2)
    cv2.rectangle(Image, (int(Name_X_pos-10), int(Name_y_pos-25)),(int(Name_X_pos +10 + (len(NAME) * 7)), int(Name_y_pos-1)), WHITE, 1)  # Desenhe um retângulo preto sobre a moldura do rosto
    cv2.putText(Image, NAME, (int(Name_X_pos), int(Name_y_pos - 10)), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)  # Imprimir o nome do ID

#-------------------------------------- TESTE -------------------------------------------

    draw_box(Image, x, y, w, h)
    cv2.rectangle(Image,(660,450),(0,1500),(255, 0, 0), -1)
    cv2.putText(Image, "Cadastrar(alt+C) | Alterar(alt+A) | Deletar(alt+D) | Navegar(alt+N) | Sair(alt+Q)", (10,473), cv2.FONT_HERSHEY_DUPLEX, 0.475,(-10, -10, -10))  # Imprimir o nome do ID
    
#-------------------------------------- TESTE -------------------------------------------

def draw_box(Image, x, y, w, h):
    cv2.line(Image, (x, y), (x + (int(w/5)) ,y), WHITE, 2)
    cv2.line(Image, (x+((int(w/5)*4)), y), (x+w, y), WHITE, 2)
    cv2.line(Image, (x, y), (x, y+(int(h/5))), WHITE, 2)
    cv2.line(Image, (x+w, y), (x+w, y+int((h/5))), WHITE, 2)
    cv2.line(Image, (x, (y+int((h/5*4)))), (x, y+h), WHITE, 2)
    cv2.line(Image, (x, (y+h)), (x + int((w/5)) ,y+h), WHITE, 2)
    cv2.line(Image, (x+(int((w/5)*4)), y+h), (x + w, y + h), WHITE, 2)
    cv2.line(Image, (x+w, (y+int((h/5*4)))), (x+w, y+h), WHITE, 2)

# ---------------  SEGUNDA CAIXA DE IDENTIFICAÇÃO  ----------------------
def DispID2(x, y, w, h, NAME, Image):

#  -------------- A POSIÇÃO DA CAIXA DE IDENTIFICAÇÃO ----------------------  

    Name_y_pos = y - 40
    Name_X_pos = x + w/2 - (len(NAME)*7/2)

    if Name_X_pos < 0:
        Name_X_pos = 0
    elif (Name_X_pos +10 + (len(NAME) * 7) > Image.shape[1]):
          Name_X_pos= Name_X_pos - (Name_X_pos +10 + (len(NAME) * 7) - (Image.shape[1]))
    if Name_y_pos < 0:
        Name_y_pos = Name_y_pos = y + h + 10


 #  ------------------------------------    O DESENHO DA CAIXA E ID   --------------------------------
    cv2.rectangle(Image, (int(Name_X_pos-10), int(Name_y_pos-25)),(int(Name_X_pos +10 + (len(NAME) * 7)), int(Name_y_pos-1)), (0,0,0), -2)
    cv2.rectangle(Image, (int(Name_X_pos-10), int(Name_y_pos-25)),(int(Name_X_pos +10 + (len(NAME) * 7)), int(Name_y_pos-1)), WHITE, 1) # Desenhe um retângulo preto sobre a moldura do rosto
    cv2.putText(Image, NAME, (int(Name_X_pos), int(Name_y_pos - 10)), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)  # Imprimir o nome do ID

# --------------- TERCEIRA ID CAIXA ----------------------
def DispID3(x, y, w, h, NAME, Image):

#  ------------ A POSIÇÃO DA CAIXA DE IDENTIFICAÇÃO -------------------------  

    Name_y_pos = y - 70
    Name_X_pos = x + w/2 - (len(NAME)*7/2)

    if Name_X_pos < 0:
        Name_X_pos = 0
    elif (Name_X_pos +10 + (len(NAME) * 7) > Image.shape[1]):
          Name_X_pos= Name_X_pos - (Name_X_pos +10 + (len(NAME) * 7) - (Image.shape[1]))
    if Name_y_pos < 0:
        Name_y_pos = Name_y_pos = y + h + 10
          
 #  ------------------------------------   O DESENHO DA CAIXA E ID --------------------------------------
    cv2.rectangle(Image, (int(Name_X_pos-10), int(Name_y_pos-25)),(int(Name_X_pos +10 + (len(NAME) * 7)), int(Name_y_pos-1)), (0,0,0), -2)
    cv2.rectangle(Image, (int(Name_X_pos-10), int(Name_y_pos-25)),(int(Name_X_pos +10 + (len(NAME) * 7)), int(Name_y_pos-1)), WHITE, 1)  # Desenhe um retângulo preto sobre a moldura do rosto
    cv2.putText(Image, NAME, (int(Name_X_pos), int(Name_y_pos - 10)), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)   # Imprimir o nome do ID


def DrawBox(Image, x, y, w, h):
    cv2.rectangle(Image, (x, y), (x + w, y + h), (255, 255, 255), 1)  # Desenhe um retângulo ao redor da face
# ------------------------- ESTA FUNÇÃO TEM EM CASCATA ESPECÍFICA, CASCAÇA FACIAL E UMA IMAGEM
# ------------------------- DEVOLVE UM ROSTO CORTADO E SE POSSÍVEL APERTA A INCLINAÇÃO DA CABEÇA

def DetectEyes(Image):
    Theta = 0
    rows, cols = Image.shape
    glass = glass_cas.detectMultiScale(Image)  # Isso projeta os olhos
    for (sx, sy, sw, sh) in glass:
        if glass.shape[0] == 2:                # A imagem deve ter 2 olhos
            if glass[1][0] > glass[0][0]:
                DY = ((glass[1][1] + glass[1][3] / 2) - (glass[0][1] + glass[0][3] / 2))  # Diferença de altura entre o vidro
                DX = ((glass[1][0] + glass[1][2] / 2) - glass[0][0] + (glass[0][2] / 2)) # Diferença de largura entre o vidro
            else:
                DY = (-(glass[1][1] + glass[1][3] / 2) + (glass[0][1] + glass[0][3] / 2)) # Diferença de altura entre o vidro
                DX = (-(glass[1][0] + glass[1][2] / 2) + glass[0][0] + (glass[0][2] / 2)) # Diferença de largura entre o vidro

            if (DX != 0.0) and (DY != 0.0): # Certifique-se de que a alteração ocorra apenas se houver um ângulo
                Theta = math.degrees(math.atan(round(float(DY) / float(DX), 2))) # Encontre o ângulo
                print ("Theta  " + str(Theta))

                M = cv2.getRotationMatrix2D((cols / 2, rows / 2), Theta, 1) # Encontre a matriz de rotação
                Image = cv2.warpAffine(Image, M, (cols, rows))
                # cv2.imshow('ROTATED', Image)  # DESCOMENTE SE QUISER VÊ-LO

                Face2 = face.detectMultiScale(Image, 1.3, 5)  # Isso detecta um rosto na imagem
                for (FaceX, FaceY, FaceWidth, FaceHeight) in Face2:
                    CroppedFace = Image[FaceY: FaceY + FaceHeight, FaceX: FaceX + FaceWidth]
                    return CroppedFace

def tell_time_passed():
    print ('TIME PASSED ' + str(round(((time.time() - now_time)/60), 2)) + ' MINS')
