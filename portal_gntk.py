import requests
import time
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from dotenv import load_dotenv
import os

load_dotenv('config.env')

# driver_chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver_edge = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
# driver_firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver_path_edge = './drivers/edgedriver/win64/125.0.2535.92/msedgedriver.exe'
driver_path_firefox = './drivers/geckodriver/win64/v0.34.0/geckodriver.exe'


url = os.getenv('URL')
btn_login_id = os.getenv('BTN_LOGIN_ID')
confirm_label_id = os.getenv('CONFIRM_LABEL_ID')
navegator = os.getenv('NAVEGATOR')


class NavegatorError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def open_portal(url):
        if navegator == 'edge': 
            driver = webdriver.Edge(service=EdgeService(driver_path_edge))

        elif navegator == 'firefox':
            driver = webdriver.Firefox(service=FirefoxService(driver_path_firefox))

        else:
            raise NavegatorError(f'No existe driver para el navegador: ({navegator})')

        driver.get(url)
        wait = WebDriverWait(driver, 10)
        boton = wait.until(EC.element_to_be_clickable((By.ID, btn_login_id)))
        boton.click()
        # Asegúrate de reemplazar 'id_del_boton' con el ID real del botón
        wait.until(EC.presence_of_element_located((By.ID, confirm_label_id)))


def check_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
    except requests.ConnectionError:
        pass
    return False


while True:
    time.sleep(1)
    print('Comprobando Conexion con: ', url + '...')
    if check_url(url):
        print(f'La URL {url} está disponible.')
        try:
            open_portal(url)
            continue

        except Exception as e:
            print(e)
            root = tk.Tk()
            root.withdraw()  # Oculta la ventana principal de Tk
            messagebox.showinfo("Te Has conectado a un portal.")  # Muestra una ventana emergente
            root.destroy()  # Destruye la ventana principal cuando se cierra la ventana emergente
            
            while True:
                time.sleep(1)

        except NavegatorError as e:
            print(e)
