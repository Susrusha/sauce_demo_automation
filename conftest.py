import pytest
from config.config import BASE_URL

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
# to start the process of chrome
from webdriver_manager.chrome import ChromeDriverManager
# tells which version needs to be installed

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture # decorator - used for setup and tear down.
# bcoz, when we use this we need not write setup code in every single test
def driver(request):
    browser_name = request.config.getoption("--browser")
    print(browser_name)
    
    if(browser_name == "chrome"):
        chromeService = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=chromeService)
    elif(browser_name == "firefox"):
        firefoxService = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=firefoxService)
    else:
      raise ValueError(f"Unsupported browser: {browser_name}")
        
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", default = "chrome")


