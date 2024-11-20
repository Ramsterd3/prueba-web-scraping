from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

class DriverConfig:
    
    def __init__(self, cookies_file):
        self.cookies_file = cookies_file
        self.options = webdriver.ChromeOptions()

    def configurar_driver(self):
        driver = webdriver.Chrome(options=self.options)
        
        self.cargar_cookies(driver)
        return driver

    def cargar_cookies(self, driver):

        driver.get("https://www.instagram.com/")
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']"))
        )
        
        cookies = self.cargar_cookies_desde_archivo()
        if cookies:

            for cookie in cookies:
                try:
                    driver.add_cookie(cookie)
                except Exception as e:
                    print(f"Error al agregar cookie: {e}")

            driver.refresh()
        else:
            print("No se encontraron cookies guardadas. Por favor, inicie sesión manualmente y guarde las cookies.")

    def cargar_cookies_desde_archivo(self):
        try:
            with open(self.cookies_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print("No se encontraron cookies guardadas.")
            return []

    def guardar_cookies(self, driver):
        cookies = driver.get_cookies()
        with open(self.cookies_file, "w") as file:
            json.dump(cookies, file)
        print(f"Cookies guardadas en {self.cookies_file}")


if __name__ == "__main__":
    cookies_file = "cookies.json"
    driver_config = DriverConfig(cookies_file)
    

    driver = driver_config.configurar_driver()
    

    if not driver.get_cookies():
        print("Por favor, inicie sesión en Instagram y luego ejecute el siguiente código para guardar las cookies.")
        time.sleep(30)  
        driver_config.guardar_cookies(driver) 
    
