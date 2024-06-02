import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

class Test:
    btn_aceptar_cookies = (
      By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
    #txt_caja_busqueda = (By.XPATH, "//input[@placeholder='Buscar...']")
    buscador = (By.XPATH, "//input[@name='q']")
    def test_busqueda(self):
        driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()))
        driver.get("https://es.stackoverflow.com/")
        btn_cookies = driver.find_element(*self.btn_aceptar_cookies)
        assert btn_cookies.is_displayed()
        btn_cookies.click()
        caja_busqueda = driver.find_element(*self.buscador)
        assert caja_busqueda.is_displayed()
        caja_busqueda.clear()
        caja_busqueda.send_keys("python")
        caja_busqueda.send_keys(Keys.ENTER)
        sleep(5)
        assert "python" in driver.title

if __name__ == "__main__":
    pytest.main()