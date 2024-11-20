from obtener import InstagramScraper  
from guardar_csv import GuardarCSV
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def obtener_driver():
    options = Options()
    options.add_argument('user-agent=TuUserAgentAqui') 
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options)
    

    driver.maximize_window()
    
    return driver

def main():
    guardar_csv_cuentas = GuardarCSV('Cuentas.csv')
    guardar_csv_publicaciones = GuardarCSV('Publicaciones.csv')

    guardar_csv_cuentas.crear_encabezado(es_cuenta=True)
    guardar_csv_publicaciones.crear_encabezado(es_cuenta=False)

    driver = obtener_driver()

    cuenta_url = "https://www.instagram.com/xiaomi.global/" 

    instagram_scraper = InstagramScraper()  
    nombre_cuenta = instagram_scraper.obtener_datos_cuenta(driver, cuenta_url, guardar_csv_cuentas)

    publicaciones = instagram_scraper.obtener_publicaciones(driver, cuenta_url, nombre_cuenta, guardar_csv_publicaciones)

    driver.quit()

if __name__ == "__main__":
    main()
