import random
import string

def generar_contrasena(longitud=12):
    # Unimos letras (mayúsculas y minúsculas), números y símbolos
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Seleccionamos caracteres al azar para formar la clave
    contrasena = "".join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

# Ejemplo de uso (genera una clave de 16 caracteres):
nueva_clave = generar_contrasena(16)
print(f"Tu contraseña segura es: {nueva_clave}")