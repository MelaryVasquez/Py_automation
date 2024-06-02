import pytest
import allure
from pages.stack_home_page import StackHomePage
from pages.stack_results_page import StackResultPage

class Test:
    """
    Clase para realizar las pruebas de la página de Stack Overflow en español.
    """
    @allure.title("Validar Busqueda desde la caja de texto")
    @allure.description(
        "Validar que la caja de texto funcione correctamente realizando una busqueda y validando el resultado"
    )
    @pytest.mark.noprod
    def test_validar_caja_texto_nuevo(self, driver,lenguaje):
        """
        Test para validar la funcionalidad de la caja de búsqueda.
        """
        with allure.step("Nos dirigimos a la pagina Stack Overflow en español"):
            driver.get("https://es.stackoverflow.com/")
        home_page = StackHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.limpiar_caja_busqueda()
        leng = lenguaje[1]
        home_page.buscar(leng)
        result_page = StackResultPage(driver)
        result_page.validar_contenido_URL(leng)
    @allure.title("Validar redireccion a la página de usuarios")
    @allure.description("Validar que se redireccione a la página de usuarios")
    @pytest.mark.smoke
    def test_ir_usuarios(self, driver):
        """
        Test para verificar la navegación a la página de usuarios.
        """
        with allure.step("Nos dirigimos a la pagina Stack Overflow en español"):
            driver.get("https://es.stackoverflow.com/")
        home_page = StackHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.click_usuarios()
        result_page = StackResultPage(driver)
        result_page.validar_contenido_URL("users")

if __name__ == "__main__":
    pytest.main()