import cv2                  # Importando o opencv
import numpy as np          # Importar Python Numarical
import NameFind             # Importar Função NameFind
import Recogniser_Video_LBPHFace
import os

WHITE = [255, 255, 255]

# Importar as cascatas de Haar para detecção de rosto

face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml') # Classificador "face frontal" Haar Cascade
eye_cascade = cv2.CascadeClassifier('Haar/haarcascade_eye.xml') # Classificador "olho" Haar Cascade

ID = Recogniser_Video_LBPHFace.Recogniser.ID
Count = 0
cap = cv2.VideoCapture(0)                                                                           # Camera object

# Remove as ultimas 5 imagens do usuário
try:
    for y in range(5):
        os.remove(str('dataSet/User.{}.{}.jpg'.format(ID,(y+45))))
except FileNotFoundError:
    pass

# Atualiza as imagens

for i in range(44,-1,-1):

    antigo = str('dataSet/User.{}.{}.jpg'.format(ID,i))
    novo = str('dataSet/User.{}.{}.jpg'.format(ID,(i+5)))
                    
    try:
        os.rename(antigo, novo)
        print(f'{antigo} PASSOU A SER: {novo}')
    except FileNotFoundError:
        pass


while Count < 5:
    # print('ID: '+ str(ID))
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Converta a câmera em grayScale

    if np.average(gray) > 110: # Testando o brilho da imagem
        faces = face_cascade.detectMultiScale(gray, 1.3, 5) # Detecte os rostos e armazene as posições
        for (x, y, w, h) in faces:  # Quadros LOCALIZAÇÃO X, LARGURA Y, ALTURA
            FaceImage = gray[y - int(h / 2): y + int(h * 1.5), x - int(x / 2): x + int(w * 1.5)] # O rosto é isolado e cortado
            Img = (NameFind.DetectEyes(FaceImage))
            cv2.putText(gray, "FACE DETECTADA", (x+int((w/2)), y-5), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)
            if Img is not None:
                frame = Img     # Mostrar os rostos detectados
            else:
                frame = gray[y: y+h, x: x+w]
            cv2.imwrite("dataSet/User." + str(ID) + "." + str(Count) + ".jpg", frame)
            cv2.waitKey(300)

            # cv2.imshow("Foto Capturada", frame)  # mostra a imagem capturada
            Count = Count + 1
    # cv2.imshow('Sistema de captura de fotos', gray)  # Mostrar o vídeo
    # if cv2.waitKey(1) and 0xFF == ord('q'):
        # break
print ('Face capturada com sucesso!')

import Trainer_All

cap.release()
cv2.destroyAllWindows()