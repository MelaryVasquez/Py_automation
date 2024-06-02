from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class StackHomePage:

    """
    Clase que representa la Page Object de la página principal de Stack Overflow en español.
    """
    txt_locator_buscador = (By.XPATH, "//input[@name='q']")
    btn_aceptar_cookies = (
    By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
    btn_iniciar_sesion = (By.XPATH, "//a[normalize-space()='Iniciar sesión']")
    btn_registrarse = (By.XPATH, "//a[normalize-space()='Registrarse']")
    btn_usuario = (By.CSS_SELECTOR, "#nav-users")

    def __init__(self, driver):
        self.driver = driver

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

    @allure.step("limpiamos el contenido de la caja de búsqueda")
    def limpiar_caja_busqueda(self):
        """
        Método para limpiar el contenido de la caja de búsqueda.
        """
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.txt_locator_buscador)
        )
        self.driver.find_element(*self.txt_locator_buscador).clear()

    @allure.step("buscamos el texto \"{texto}\" en la caja de búsqueda")
    def buscar(self, texto):
        """
        Método para realizar una búsqueda en la caja de búsqueda.
        """
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.txt_locator_buscador)
        )
        self.driver.find_element(*self.txt_locator_buscador).send_keys(texto)
        with allure.step("presionamos la tecla ENTER"):
            self.driver.find_element(
                *self.txt_locator_buscador).send_keys(Keys.ENTER)

    @allure.step("Hacemos clic en el botón para redirigirnos a la página de usuarios")
    def click_usuarios(self):
        """
        Método para dirigirse a la sección de usuarios.
        """
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.btn_usuario)
        )
        if self.driver.find_element(*self.btn_usuario).is_displayed():
            self.driver.find_element(*self.btn_usuario).click()
            print("Hacemos clic en el botón de usuarios")
        else:
            print("El botón de usuarios no está visible")

    @allure.step("Verificamos que la URL contenga el texto esperado")
    def verificar_contenido_URL(self, texto):
        """
        Método para verificar que la URL contenga el texto esperado.
        """
        WebDriverWait(self.driver, 10).until(
        EC.url_contains(texto)
        )
        assert texto in self.driver.current_url, f"La URL no contiene el texto {
        texto}"