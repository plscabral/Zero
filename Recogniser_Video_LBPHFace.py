#   RECONHECEDOR DO RECONHECEDOR LBPH FACE 
#   PARA O RECONHECIMENTO FACIAL, TODAS AS CARAS SÃO NECESSÁRIAS DE MESMO TAMANHO 

import cv2                  # Importando o opencv
import numpy as np          # Importar Python Numarical
import NameFind
import webbrowser
import time
import keyboard

class Recogniser:

    ID = None

    def executarRecogniser(self):

        # Importe as cascatas de Haar para obter a detecção de rosto e olho
        face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml')
        eye_cascade = cv2.CascadeClassifier('Haar/haarcascade_eye.xml')

        recognise = cv2.face.LBPHFaceRecognizer_create(2, 2, 7, 7, 15)   # Objeto reconhecedor de rosto LBPH
        recognise.read("Recogniser/trainingDataLBPH.xml")  # Carregue os dados de treinamento do treinador para reconhecer os rostos

        # ---------------------- INICIAR A ALIMENTAÇÃO DE VÍDEO -----------------------------------------

        cap = cv2.VideoCapture(0)                 # Objeto da câmera
        # cap = cv2.VideoCapture('TestVid.wmv')   # Objeto de vídeo
        path = 'dataSet'  # caminho para as fotos
        
        condicao = True
        while condicao:
            ret, img = cap.read()                      # Leia o objeto da câmera
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        # Converta a câmera em cinza
            faces = face_cascade.detectMultiScale(gray, 1.3, 5) # Detecte os rostos e armazene as posições

            for (x, y, w, h) in faces:    # Quadros LOCALIZAÇÃO X, LARGURA Y, ALTURA

                # Os olhos devem estar dentro do rosto.
                gray_face = gray[y: y+h, x: x+w]                # O rosto é isolado e cortado
                eyes = eye_cascade.detectMultiScale(gray_face)
                for (ex, ey, ew, eh) in eyes:
                    ID, conf = recognise.predict(gray_face)     # Determine o ID da foto
                    Recogniser.ID = ID
                    # NAME = NameFind.ID2Name(ID, conf)
                    # NameFind.DispID(x, y, w, h, NAME, gray)
                    if conf <= 4:
                         NAME = NameFind.ID2Name(ID, conf)
                         NameFind.DispID(x, y, w, h, NAME, gray)
                    else:
                        NameFind.DispID(x, y, w, h,"NAO RECONHECIDO ", gray)
                        ID = 1

            cv2.imshow('ZERO', gray)   # Mostrar o vídeo
            cv2.waitKey(1)

            # if keyboard.is_pressed('z'):             # A tecla 'z' atualiza as imagens !!
            #     if ID!=1:
            #         import AtualizarFace

            # A tecla 'n' abre o navegador !!
            if keyboard.is_pressed('alt+n'):
                if ID != 1:
                    NameFind.AbrirURL(ID)
                continue

            # Saia se a chave for Q
            if keyboard.is_pressed('alt+q'):
                break

            # Apertar a tecla 'c' para realizar o cadastro
            if keyboard.is_pressed('alt+c'):
                cv2.destroyAllWindows()
                import Tela_cadastro
                continue

            # Apertar a tecla a para alterar o cadastro
            if keyboard.is_pressed('alt+a'):
                if ID!=1:
                    cv2.destroyAllWindows()
                    import Tela_alterarCadastro
                    continue

            try:
                if keyboard.is_pressed('alt+d'):            # Apertar a tecla d para excluir o cadastro
                    cv2.destroyAllWindows()
                    import Tela_deletar
                    condicao=False
                    break
            except:
                pass


            # if keyboard.is_pressed('alt+v'):           # Apertar a tecla 'v' para visitar github
            #     webbrowser.open('https://github.com/systemzeroo/systemzeroo')
            #     continue

        #NameFind.tell_time_passed()
        cap.release()
        cv2.destroyAllWindows()