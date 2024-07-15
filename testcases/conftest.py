import pytest
from selenium import webdriver
from utilities import read_configurations


@pytest.fixture()
def setup_and_teardown(request):
    global driver
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    driver.maximize_window()
    app_url = read_configurations.read_configuration("basic info", "url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()
