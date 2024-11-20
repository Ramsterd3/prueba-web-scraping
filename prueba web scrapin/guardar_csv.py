import csv
class GuardarCSV:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def guardar_cuenta(self, nombre_cuenta, numero_publicaciones, numero_seguidores, numero_seguidos, descripcion):
        """Guardar los datos de la cuenta en el archivo CSV."""
        with open(self.nombre_archivo, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([nombre_cuenta, numero_publicaciones, numero_seguidores, numero_seguidos, descripcion])

    def guardar_publicacion(self, id_cuenta, id_publicacion, descripcion, reacciones, comentarios_reacciones):
        """Guardar los datos de la publicación en el archivo CSV."""
        with open(self.nombre_archivo, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([id_cuenta, id_publicacion, descripcion, reacciones, comentarios_reacciones])

    def crear_encabezado(self, es_cuenta=True):
        """Crear los encabezados de los archivos CSV si es necesario."""
        with open(self.nombre_archivo, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            if es_cuenta:
                writer.writerow(['nombre_cuenta', 'numero_publicaciones', 'numero_seguidores', 'numero_seguidos', 'descripcion'])
            else:
                writer.writerow(['id_cuenta', 'id_publicacion', 'descripcion', 'reacciones', 'comentarios_reacciones'])
