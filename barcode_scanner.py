import os
import datetime
from pyzbar import pyzbar
import cv2
from PIL import ImageGrab


codigo_barra = []


def decode(image):  # Função que decodifica o código de barras
    decoded_objects = pyzbar.decode(image)  # Decodifica o código de barras
    for obj in decoded_objects:  # Percorre todos os objetos decodificados
        # Adiciona o código de barras na lista
        codigo_barra.append(obj.data.decode("utf-8"))
        print(obj.data.decode("utf-8"))  # Imprime o código de barras
        print(obj.type)  # Imprime o tipo de código de barras
    return image


if __name__ == "__main__":
    from glob import glob

    barcodes = ImageGrab.grabclipboard()  # Pegando imagem da área de trabalho
    filename = datetime.datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S")  # Criando nome do arquivo
    filename = filename + ".png"  # Adicionando extensão
    barcodes.save(filename, "PNG")  # Salvando imagem
    barcodes = glob("*.png")  # Pegando todas as imagens com extensão .png

    for barcode_file in barcodes:  # Percorre todas as imagens com extensão .png
        img = cv2.imread(barcode_file)  # Lendo imagem
        img = decode(img)  # Decodificando imagem
        codigo = pyzbar.decode(img)  # Decodificando imagem
        cv2.imshow("img", img)  # Mostrando imagem
        cv2.waitKey(0)  # Aguardando tecla para fechar janela
        cv2.destroyAllWindows()  # Fechando janela

os.remove(filename)  # Removendo arquivo
