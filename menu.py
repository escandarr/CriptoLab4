import aes
import des
import desdesdes

def solicitar_datos(tamano_clave, tamano_iv):
    while True:
        try:
            clave = input("Ingrese la clave: ").encode()  # Convertir clave a bytes
            iv = input("Ingrese el vector de inicialización (IV): ").encode()  # Convertir IV a bytes
            texto = input("Ingrese el texto a cifrar: ").encode()  # Convertir texto a bytes
            
            # Validación de tamaño de clave e IV
            if len(iv) != tamano_iv:
                print(f"Error: El IV debe tener exactamente {tamano_iv} bytes.")
                continue
            
            return clave, iv, texto
        except Exception as e:
            print("Error al ingresar datos:", e)
            continue

while True:
    print("\nSeleccione el algoritmo de cifrado:")
    print("1. AES-256")
    print("2. DES")
    print("3. 3DES")
    print("4. Salir")
    opcion = input("Ingrese su opción: ").strip()

    if opcion == "1":
        print("\n--- Cifrado AES-256 ---")
        clave, iv, texto = solicitar_datos(tamano_clave=32, tamano_iv=16)
        clave = aes.ajustar_clave(clave)
        try:
            texto_cifrado = aes.cifrar_aes(texto, clave, iv)
            print("Texto cifrado (Base64):", texto_cifrado)
            print("Texto descifrado:", aes.descifrar_aes(texto_cifrado, clave, iv))
        except Exception as e:
            print("Error en el cifrado/descifrado:", e)

    elif opcion == "2":
        print("\n--- Cifrado DES ---")
        clave, iv, texto = solicitar_datos(tamano_clave=8, tamano_iv=8)
        clave = des.ajustar_clave(clave)
        try:
            texto_cifrado = des.cifrar_des(texto, clave, iv)
            print("Texto cifrado (Base64):", texto_cifrado)
            print("Texto descifrado:", des.descifrar_des(texto_cifrado, clave, iv))
        except Exception as e:
            print("Error en el cifrado/descifrado:", e)

    elif opcion == "3":
        print("\n--- Cifrado 3DES ---")
        clave, iv, texto = solicitar_datos(tamano_clave=16, tamano_iv=8)
        clave = desdesdes.ajustar_clave(clave)
        try:
            texto_cifrado = desdesdes.cifrar_3des(texto, clave, iv)
            print("Texto cifrado (Base64):", texto_cifrado)
            print("Texto descifrado:", desdesdes.descifrar_3des(texto_cifrado, clave, iv))
        except Exception as e:
            print("Error en el cifrado/descifrado:", e)

    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
