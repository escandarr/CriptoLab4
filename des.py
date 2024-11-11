from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

def ajustar_clave(clave, tamano_necesario=8):
    # Completa la clave con bytes aleatorios si es más corta o la trunca si es más larga
    if len(clave) < tamano_necesario:
        clave += get_random_bytes(tamano_necesario - len(clave))
    elif len(clave) > tamano_necesario:
        clave = clave[:tamano_necesario]
    print(f"Clave ajustada a {tamano_necesario} bytes (DES):", clave)
    print(f"Longitud de la clave ajustada: {len(clave)} bytes")
    return clave

def cifrar_des(texto, clave, iv):
    cipher = DES.new(clave, DES.MODE_CBC, iv)
    texto_cifrado = cipher.encrypt(pad(texto, DES.block_size))
    return base64.b64encode(texto_cifrado).decode()

def descifrar_des(texto_cifrado, clave, iv):
    texto_cifrado = base64.b64decode(texto_cifrado)
    cipher = DES.new(clave, DES.MODE_CBC, iv)
    return unpad(cipher.decrypt(texto_cifrado), DES.block_size).decode()
