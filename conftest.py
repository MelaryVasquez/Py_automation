# conftest.py
import pytest
from config.browser import BrowserConfig
import os

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
    help="Escoger navegador: chrome o edge")
    parser.addoption("--ambiente", action="store", default="qa",
    help="Seleccionando el ambiente: qa o prod")

def pytest_configure(config):
    os.environ["ambiente"] = config.getoption("ambiente")
    os.environ["browser"] = config.getoption("browser")

@pytest.fixture(autouse=True)
def driver(request):
    """
    Fixture para inicializar el driver del navegador
    """
    browser_seleccionado = request.config.getoption("--browser")
    driver = BrowserConfig(browser_seleccionado).select_browser()
    driver.maximize_window()
    # Retorna el objeto driver para las pruebas que lo necesiten (yield es como un return pero no cierra el driver)
    yield driver
    print("Cerrar Browser")
    driver.quit()

@pytest.fixture
def lenguaje():
    return ["Java", "Python"]