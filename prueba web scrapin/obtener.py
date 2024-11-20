import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from googletrans import Translator
import emoji
from guardar_csv import GuardarCSV

class InstagramScraper:
    def __init__(self):
        self.translator = Translator()

    @staticmethod
    def eliminar_emojis(descripcion):
        """Elimina emojis de una cadena de texto."""
        return ''.join([char for char in descripcion if char not in emoji.UNICODE_EMOJI['en']])

    def obtener_datos_cuenta(self, driver, cuenta_url, guardar_csv):
        try:
            time.sleep(2)  # Esperar a que la página se cargue completamente
            driver.get(cuenta_url)
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.TAG_NAME, 'article'))
            )

            # Extraer datos de la cuenta
            nombre_cuenta = driver.find_element(By.XPATH, "//h1").text
            cuenta_nombre = cuenta_url.split("/")[-2]  # Obtener el nombre de usuario de la URL

            numero_publicaciones = driver.find_element(By.XPATH, "//span[@class='_ac2a']").text
            numero_seguidores = driver.find_element(By.XPATH, f"//a[@href='/{cuenta_nombre}/followers/']/span").text
            numero_seguidos = driver.find_element(By.XPATH, f"//a[@href='/{cuenta_nombre}/following/']/span").text

            try:
                descripcion = driver.find_element(By.XPATH, "//div[@class='_aa_c']").text
            except:
                descripcion = "N/A"

            # Traducir la descripción
            descripcion = self.eliminar_emojis(descripcion)
            descripcion_traducida = self.translator.translate(descripcion, src='auto', dest='es').text

            # Guardar los datos de la cuenta
            guardar_csv.guardar_cuenta(nombre_cuenta, numero_publicaciones, numero_seguidores, numero_seguidos, descripcion_traducida)
            return nombre_cuenta

        except TimeoutException:
            print(f"No se pudo cargar la página de la cuenta: {cuenta_url}")
            return None

    def obtener_publicaciones(self, driver, cuenta_url, id_cuenta, guardar_csv):
        try:
            time.sleep(2)  # Esperar a que la página se cargue completamente
            driver.get(cuenta_url + "/posts/")  # Ir a la página de publicaciones de la cuenta
            publicaciones = []
            publicaciones_urls = driver.find_elements(By.XPATH, "//a[@href]")  # Obtener todos los enlaces a publicaciones

            for publicacion in publicaciones_urls:
                url_publicacion = publicacion.get_attribute('href')
                driver.get(url_publicacion)
                
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, 'article')))

                try:
                    descripcion_publicacion = driver.find_element(By.XPATH, "//div[@class='_aa_c']").text
                except:
                    descripcion_publicacion = "N/A"

                descripcion_publicacion = self.eliminar_emojis(descripcion_publicacion)
                descripcion_traducida = self.translator.translate(descripcion_publicacion, src='auto', dest='es').text

                try:
                    reacciones = driver.find_element(By.XPATH, "//span[@class='x1n2f8k x1v4j9b']").text
                except:
                    reacciones = "N/A"

                comentarios = driver.find_elements(By.XPATH, "//div[@class='_a9--']")
                comentarios_reacciones = []
                for comentario in comentarios[:10]:  # Solo obtener los primeros 10 comentarios
                    comentario_texto = comentario.text
                    comentario_reaccion = comentario.find_element(By.XPATH, ".//span").text
                    comentarios_reacciones.append((comentario_texto, comentario_reaccion))

                guardar_csv.guardar_publicacion(id_cuenta, url_publicacion, descripcion_traducida, reacciones, comentarios_reacciones)
                publicaciones.append((url_publicacion, comentarios_reacciones))

            return publicaciones

        except TimeoutException:
            print(f"No se pudo cargar la publicación en: {url_publicacion}")
            return []
