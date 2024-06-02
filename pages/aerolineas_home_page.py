from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class AerolineasHomePage:

    """
    Clase que representa la Page Object de la página principal de Aerolineas Argentinas.
    """
    btn_locator_registrarte = (By.XPATH, "//button[normalize-space()='registrate']")
    btn_locator_aceptar_cookies = (By.XPATH, "//button[@id='cookies']")
    btn_locator_ingresar = (By.XPATH, "//button[normalize-space()='INGRESAR']")
    txt_locator_contraseña = (By.XPATH, "//input[@id = 'passwordInput']")

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Verificar el boton registrar")
    def btn_registrarte(self):
        """
        Método para validar el boton registrarte.
        """
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.btn_locator_registrarte)
        )
        self.driver.find_element(*self.btn_locator_registrarte).is_displayed()
    
    @allure.step("Hacemos clic en el botón de aceptar cookies")
    def click_aceptar_cookies(self):
        """
        Método para hacer clic en el botón de aceptar cookies.
        """
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.btn_aceptar_cookies)
        )
        if self.driver.find_element(*self.btn_aceptar_cookies).is_displayed():
            self.driver.find_element(*self.btn_aceptar_cookies).click()
    
    @allure.step("Verificar el boton ingresar")
    def is_displayed_btn_ingresar(self):
        """
        Método para validar el boton ingresar.
        """
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.btn_locator_ingresar)
        )
        self.driver.find_element(*self.btn_locator_ingresar).is_displayed()
    
    @allure.step("Limpiar el contenido de la caja de contraseña")
    def txt_contraseña(self):
        """
        Método para limpiar el contenido de la contraseña.
        """
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.txt_locator_contraseña)
        )
        self.driver.find_element(*self.txt_locator_contraseña).is_displayed()