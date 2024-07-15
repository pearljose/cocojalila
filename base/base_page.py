
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class PageBase:
    def __init__(self, driver):
        self.driver = driver



    def click(self, webelement):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(expected_conditions.visibility_of_element_located(webelement))
        #self._highlight_element(element, "green")
        element.click()

    def fill_text(self, webelement, txt):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(expected_conditions.visibility_of_element_located(webelement))
        element.clear()
        #self._highlight_element(element, "green")
        element.send_keys(txt)

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)




    def is_ele_displayed(self, webelement):
        wait = WebDriverWait(self.driver, 10)
        try:
            element = wait.until(expected_conditions.visibility_of_element_located(webelement))
            return element.is_displayed()  # Return True if element is displayed
        except TimeoutException:
            # Handle the case where the element is not visible within the timeout
            print(f"Element with locator {webelement} not visible within the timeout.")
            return False
        except NoSuchElementException:
            # Handle the case where the element is not found
            print(f"Element with locator {webelement} not found.")
            return False


    def return_ele(self, webelement):
        wait = WebDriverWait(self.driver, 120)
        element = wait.until(expected_conditions.visibility_of_element_located(webelement))
        return element

    def wait_until_element_is_visible(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 15)
        return wait.until(expected_conditions.visibility_of_element_located((locator_type, locator)))