import requests
import os

# Lista de URLs de las imágenes que quieres descargar
urls = [
    "https://vinopremier.com/media/catalog/product/1/5/1544664459.jpeg",
    "https://vinopremier.com/media/catalog/product/1/5/1552039335.jpeg",
    "https://vinopremier.com/media/catalog/product/1/5/1552039430.jpeg",
    # Agrega el resto de URLs aquí
]

# Directorio donde quieres guardar las imágenes
# Asegúrate de que este directorio exista en tu máquina
save_dir = 'C:\\Users\\NESTORIVANYZMAYATARI\\Downloads\\DownloadVinoPremier'

for url in urls:
    # Extrae el nombre de la imagen de la URL
    filename = url.split('/')[-1]
    
    # Combina el directorio de guardado con el nombre de archivo
    save_path = os.path.join(save_dir, filename)
    
    # Realiza una petición GET a la URL
    response = requests.get(url)
    
    # Verifica si la petición fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Abre un archivo en el directorio de guardado con el nombre de la imagen
        # y escribe el contenido binario de la respuesta
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Imagen {filename} descargada con éxito.")
    else:
        print(f"Error al descargar {filename}. Estado: {response.status_code}")

print("Descarga completada.")
