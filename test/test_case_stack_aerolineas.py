import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.stack_home_page import StackHomePage
from pages.stack_results_page import StackResultPage

class Test:

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        self.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
        self.driver.maximize_window()
        self.driver.get("https://www.aerolineas.com.ar/arplus/acceso")
        yield # Lo que este despues de yield se ejecuta despues de cada test
        print("Cerrar Browser")
        self.driver.quit()

    @allure.title("Verificar que los elementos de la pagina acceso se muestre en Aerolienas Argentinas")
    @allure.description(
        "Validar diferentes botones y caja de texto en Aerolineas Argentina"
    )
    def test_validar_Aerolineas(self):
        """
        Test para validar caja de textos y diferentes botones en Aerolineas Argentina.
        """
        with allure.step("Nos dirigimos a la pagina Aerolineas Argentina"):
            self.driver.get("https://www.aerolineas.com.ar/arplus/acceso")
        home_page = StackHomePage(self.driver)
        home_page.click_aceptar_cookies()
        home_page.txt_contraseña()
        home_page.is_displayed_btn_ingresar()
        home_page.btn_registrarse()

if __name__ == "__main__":
    pytest.main()