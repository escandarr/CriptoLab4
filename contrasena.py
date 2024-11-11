# Solicitar la contraseña y el padding en formato de bytes (por ejemplo: \xd9\xf8\xa3\x92&\x96;\rt\xd3\xfe)
password = input("Ingresa la contraseña: ")
padding_raw = input("Ingresa el padding en formato de bytes (por ejemplo, \\xd9\\xf8\\xa3): ")

# Convertir el padding a su formato de bytes
try:
    # Interpreta la cadena `\x..` como bytes
    padding_bytes = bytes.fromhex(padding_raw.replace("\\x", ""))
except ValueError:
    print("Error: Asegúrate de que el padding esté en el formato correcto (por ejemplo: \\xd9\\xf8).")
    exit()

# Combinar la contraseña en formato de bytes
combined_password = password.encode() + padding_bytes

print("Contraseña en bytes con padding:", combined_password)
print("Contraseña con padding en ASCII:", combined_password.decode(errors='ignore'))
