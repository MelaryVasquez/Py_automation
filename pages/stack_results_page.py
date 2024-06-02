import allure

class StackResultPage:

    """
    Clase que representa la Page Object de la página de resultados de Stack Overflow en español.
    """
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Validamos que el texto \"{texto}\" se encuentre en la URL")
    def validar_contenido_URL(self, texto):
        """
        Método para validar que el texto dado está presente en la URL actual.
        """
        assert texto in self.driver.current_url, f"El valor {
            texto} no se encuentra en la URL"