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
        self.driver.get("https://es.stackoverflow.com/")
        yield # Lo que este despues de yield se ejecuta despues de cada test
        print("Cerrar Browser")
        self.driver.quit()

    @allure.title("Validar Busqueda desde la caja de texto")
    @allure.description(
        "Validar que la caja de texto funcione correctamente realizando una busqueda y validando el resultado"
    )
    def test_validar_caja_texto_nuevo(self):
        """
        Test para validar la funcionalidad de la caja de búsqueda.
        """
        with allure.step("Nos dirigimos a la pagina Stack Overflow en español"):
            self.driver.get("https://es.stackoverflow.com/")
        home_page = StackHomePage(self.driver)
        home_page.click_aceptar_cookies()
        home_page.limpiar_caja_busqueda()
        home_page.buscar("python")
        result_page = StackResultPage(self.driver)
        result_page.validar_contenido_URL("python")

if __name__ == "__main__":
    pytest.main()