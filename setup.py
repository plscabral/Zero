import sys
from cx_Freeze import setup, Executable
import webbrowser
import cv2 # Biblioteca de captura de vídeo
import math # Biblioteca de rotação de imagens
import time # Biblioteca de contagem de tempo
import os # Biblioteca de Arquivos
import keyboard
import numpy as np 
from tkinter import *

base = None
icon = "logo.ico"
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("Recogniser_Video_LBPHFace.py", base=base),
        Executable("Face_Capture_With_Rotate.py", base=base),
        Executable("NameFind.py", base=base),
        Executable("Trainer_All.py", base=base),
        Executable("Tela_cadastro.py", base=base),
        Executable("Tela_cadastroConcluido.py", base=base),
        Executable("Tela_alterarCadastro.py", base=base),
        Executable("Tela_alterarConcluida.py", base=base),
        Executable("Tela_deletar.py", base=base),
        Executable("Tela_deletarConcluida.py", base=base),
        Executable("Tela_principal.py", base=base),
]

buildOptions = dict(
        packages = [],
        includes = ["cv2", "tkinter", "os", "time", "math", "numpy", "webbrowser", "keyboard"],
        include_files = [ 'logo.ico', 'dataSet', 'Haar', 'Recogniser', 'SaveData','Names.txt'],
        excludes = []
)

setup(
    name = "ZERO",
    version = "1.0",
    description = "Atalho de navegação utilizando Reconhecimento Facial",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
