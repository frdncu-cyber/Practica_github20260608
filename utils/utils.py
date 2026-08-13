import json
import urllib.request

def obtener_mi_ip():
    url = "https://ipinfo.io/json"
    
    try:
        # Hacemos la petición a la API pública
        with urllib.request.urlopen(url) as respuesta:
            datos = json.loads(respuesta.read().decode())
            
        print("=== INFORMACIÓN DE CONEXIÓN ===")
        print(f"IP Pública: {datos.get('ip')}")
        print(f"Ciudad:     {datos.get('city')}")
        print(f"Región:     {datos.get('region')}")
        print(f"País:       {datos.get('country')}")
        print(f"Proveedor:  {datos.get('org')}")
        
    except Exception as e:
        print(f"Ocurrió un error al consultar: {e}")

# Ejecutar la función
obtener_mi_ip()