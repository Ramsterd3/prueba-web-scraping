import json
from DriverConfig import configurar_driver  # Usar tu configuración ya existente

def sacar_cookies():
    driver = configurar_driver()  # Inicializa el navegador con la configuración existente
    print("Inicia sesión manualmente en Instagram desde cero.")
    driver.get("https://www.instagram.com/Google")

    # Pausa para que el usuario pueda iniciar sesión manualmente
    input("Presiona Enter después de iniciar sesión en la pestaña...")
    
    # Extraer cookies y sobrescribir el archivo JSON
    cookies = driver.get_cookies()
    with open("cookies_instagram.json", "w") as file:
        json.dump(cookies, file, indent=4)  # Formato legible

    print("Cookies guardadas exitosamente en 'cookies_instagram.json'.")
    driver.quit()
