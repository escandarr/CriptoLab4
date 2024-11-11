from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

def ajustar_clave(clave, tamano_necesario=32):
    # Completa la clave con bytes aleatorios si es más corta o la trunca si es más larga
    if len(clave) < tamano_necesario:
        clave += get_random_bytes(tamano_necesario - len(clave))
    elif len(clave) > tamano_necesario:
        clave = clave[:tamano_necesario]
    print(f"Clave ajustada a {tamano_necesario} bytes (AES):", clave)
    print(f"Longitud de la clave ajustada: {len(clave)} bytes")
    return clave

def cifrar_aes(texto, clave, iv):
    cipher = AES.new(clave, AES.MODE_CBC, iv)
    texto_cifrado = cipher.encrypt(pad(texto, AES.block_size))
    return base64.b64encode(texto_cifrado).decode()

def descifrar_aes(texto_cifrado, clave, iv):
    texto_cifrado = base64.b64decode(texto_cifrado)
    cipher = AES.new(clave, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(texto_cifrado), AES.block_size).decode()
