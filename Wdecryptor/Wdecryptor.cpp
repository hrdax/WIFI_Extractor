//Thanks for using wdecryptor more info here https://github.com/hrdax
#include <iostream>
#include <Windows.h>
#pragma comment (lib, "Crypt32.lib")
#include <fstream>

void DecryptWifi(BYTE* buffer, DWORD SizeBuffer, std::string key)
{
    DATA_BLOB DataIn;
    DATA_BLOB DataOut;

    DataIn.pbData = buffer;
    DataIn.cbData = SizeBuffer;

    if (CryptUnprotectData(&DataIn, 0, NULL, NULL, NULL, 0, &DataOut))
    {
        std::ofstream archivo("decrypted.txt");
        archivo.is_open();
        archivo << key + ": " + (char*)DataOut.pbData;
        printf("\n[+] WIFI Decrypted Password: %s", (char*)DataOut.pbData);
        printf("\n[+] Contrasena WIFI desencriptada: %s\n", (char*)DataOut.pbData);
        LocalFree(DataOut.pbData);
        archivo.close();
        
    }
    else
    {

        printf("\n[*] Usage: Wdecryptor.exe --key '<key>'\n");
        printf("\n[*] If you are having issues maybe you can check the readme at https://github.com/hrdax/WIFI_Extractor#readme\n");

        printf("\n[-] Cant decrypt the password\n");
        printf("[-] No se pudo desencriptar la contrasena\n");
        printf("\n[*] Possible issues | Posibles problemas:\n");
        printf("[*] 1. are you with system authority?\n");
        printf("[*] 1. estas ejecutando con privilegios del sistema?\n");
        printf("[*] 2. is the key totally correct?\n");
        printf("[*] 2. la key es totalmente correcta?\n");
    }
}

int main(int argc, char* argv[])
{
    std::string valor_a_entregar;

    for (int i = 1; i < argc; i++) {
        if (std::string(argv[i]) == "--key") {
            if (i + 1 < argc) {
                valor_a_entregar = argv[i + 1];
                break;
            }
        }
    }

    const char* data = valor_a_entregar.c_str();
    int length = strlen(data);

    BYTE buffer[2000];

    for (int i = 0; i < length; i += 2)
    {
        sscanf_s(&data[i], "%02x", &buffer[i / 2], sizeof(buffer) / 2);
    }
    printf("\n[*] Trying to decrypt the password of the following key..");
    printf("\n[*] Tratando de desencriptar la contrasena de la siguiente key..\n");
    Sleep(2000);
    printf("\nKey:\n\n");
    for (int i = 0; i < length; i++)
    {
        printf("%02X ", buffer[i]);
        Sleep(5);
        
    }
    printf("\n");
    DecryptWifi(buffer, sizeof(buffer), valor_a_entregar);
}