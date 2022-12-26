'''Thanks for using wifi extractor|Gracias por usar wifi extractor
    GitHub repository: https://github.com/hrdax/WIFI_Extractor
    '''

import os, sys, requests, subprocess
import xml.etree.ElementTree as t

#crea el archivo txt
txt = open("Extracciones.txt", "w")

#lista de exportaciones xml que genera el netsh y Wifis
Archivos_XML_WIFI = []
WIFIs = []

#corre el comando en la command prompt
cmd = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output=True).stdout.decode()

#guarda la ruta actual
ruta = os.getcwd()

#recorre los archivos en la ruta
for archivo in os.listdir(ruta):
    #encuentra los archivos xml exportados y los agrega
    if archivo.endswith(".xml"):
        Archivos_XML_WIFI.append(archivo)

#contador para la lista de wifis
conta = 0

#recorre los archivos xml
for archivo in Archivos_XML_WIFI:
    tr = t.parse(archivo)
    rt = tr.getroot()
    ssid = rt[1][0][1].text
    contrasena = rt[4][0][1][2].text
    ssid_contrasena = f"Nombre/SSID: {ssid} || CONTRASEÑA/PASSWORD: {contrasena}"
    WIFIs.append(ssid_contrasena)
    txt.write(WIFIs[conta]+"\n")
    conta = conta + 1
    os.remove(archivo)

#ciera el archivo txt
txt.close()

