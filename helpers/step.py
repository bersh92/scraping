from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Class for steps abstract methods.


class StepHelper:

    def get_how(self, locator):
        if locator.startswith("//"):
            how = By.XPATH
        else:
            how = By.CSS_SELECTOR
        return how

    def is_element_present(self, locator, wd):
        time = 3
        try:
            WebDriverWait(wd, time).until(
                EC.presence_of_element_located((self.get_how(locator), locator)))
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False
        return True

    def click_on_element(self, locator, wd):
        WebDriverWait(wd, 10).until(
            EC.visibility_of_element_located((self.get_how(locator), locator)))
        element = WebDriverWait(wd, 10).until(
            EC.element_to_be_clickable((self.get_how(locator), locator))
        )
        ActionChains(wd).move_to_element(element).pause(0.3).click().perform()

    def input_text(self, locator, text, wd):
        element = WebDriverWait(wd, 10).until(
            EC.visibility_of_element_located((self.get_how(locator), locator)))
        element.clear()
        element.send_keys(text)

    def get_list_of_elements(self, locator, wd):
        by = self.get_how(locator)
        WebDriverWait(wd, 10).until(
            EC.presence_of_all_elements_located((self.get_how(locator), locator)))
        return wd.find_elements(by=by, value=locator)

    def get_element_text(self, locator, wd):
        element = WebDriverWait(wd, 10).until(
            EC.visibility_of_element_located((self.get_how(locator), locator)))
        return element.text

    def specified_element_is_not_present(self, locator, wd):
        time = 3
        WebDriverWait(wd, time).until(
            EC.invisibility_of_element_located((self.get_how(locator), locator)))

    def wait_for_element(self, locator, wd):
        element = WebDriverWait(wd, 10).until(
            EC.visibility_of_element_located((self.get_how(locator), locator)))
        return element
