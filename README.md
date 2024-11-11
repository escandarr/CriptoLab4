# 🔐 Proyecto de Cifrado y Descifrado en Modo CBC

Este proyecto implementa algoritmos de cifrado y descifrado en modo CBC (Cipher Block Chaining) utilizando los métodos **AES**, **DES** y **3DES**. Los usuarios pueden cifrar y descifrar textos de manera segura con claves y vectores de inicialización personalizables.

## 📋 Características

- **Algoritmos Soportados**: AES-256, DES y 3DES.
- **Modo de Operación**: Cipher Block Chaining (CBC).
- **Entrada Personalizada**: Clave, vector de inicialización (IV) y texto a cifrar.
- **Compatibilidad con Servicios Externos**: Resultados compatibles con servicios de cifrado en línea.
- **Soporte de Padding**: Ajuste de claves y padding automático para compatibilidad.

1. Ejecuta el archivo principal `menu.py`:
   ```bash
   python menu.py
   ```
2. Sigue las instrucciones en la terminal para seleccionar el algoritmo de cifrado, ingresar la clave, el IV y el texto que deseas cifrar o descifrar.

### Ejemplo de Uso

```plaintext
--- Cifrado AES-256 ---
Ingrese la clave: 12345678123456781234567812345678
Ingrese el vector de inicialización (IV): 1234567812345678
Ingrese el texto a cifrar: mensaje

Resultado:
Texto cifrado (Base64): jFLT6SAhW7BqkRWtSaBYPQ==
Texto descifrado: mensaje
```

## 🛠️ Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal.
- **Cryptography Library**: Para la implementación de algoritmos de cifrado.

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.
