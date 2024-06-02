import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

class Test:
    btn_aceptar_cookies = (
        By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
    txt_caja_busqueda = (By.XPATH, "//input[@placeholder='Buscar...']")
    buscador = (By.XPATH, "//input[@name='q']")

    @allure.title("Validar busqueda en stackoverflow")
    @allure.description("Validar que se pueda buscar en stackoverflow")
    def test_busqueda(self):
        driver = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()))
        driver.get("https://es.stackoverflow.com/")
        driver.maximize_window()


        with allure.step("Validar que se muestre el boton de aceptar cookies"):
            btn_cookies = driver.find_element(*self.btn_aceptar_cookies)
            assert btn_cookies.is_displayed()
        with allure.step("Aceptar cookies"):
            btn_cookies.click()
        with allure.step("Validar que se muestre el buscador"):
            caja_busqueda = driver.find_element(*self.buscador)
            assert caja_busqueda.is_displayed()
        with allure.step("Realizar busqueda"):
            caja_busqueda.clear()
            caja_busqueda.send_keys("python")
            caja_busqueda.send_keys(Keys.ENTER)
            sleep(3)
        with allure.step("Validar que se muestre el resultado de la busqueda"):
            assert "python" in driver.title

if __name__ == "__main__":
    pytest.main()