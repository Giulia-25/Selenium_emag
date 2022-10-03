import selenium.webdriver
import pytest
import selenium.webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def browser():
    #before tests
    global driver
    # initializam un browser
    options = Options()
    # options.add_argument('--headless')
    s = Service(ChromeDriverManager().install())
    driver = selenium.webdriver.Chrome(service=s, chrome_options=options)
    # driver = selenium.webdriver.Firefox(executable_path=GeckoDriverManager().install())

    driver.maximize_window()
    #selenium va cauta toate elementele x secunde inainte sa dea eroare
    driver.implicitly_wait(5)
    #return driver
    yield driver
    #after tests
    driver.quit()
    return driver