import time
import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By


class TestCase(unittest.TestCase):

    # Setup for Unittest TestCase
    @classmethod
    def setUp(self):
        ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome()
        #FirefoxService(GeckoDriverManager().install())
        #self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://the-internet.herokuapp.com/")
        self.wait = WebDriverWait(self.driver, 10)


###################################################
    # Testing Site Variation
    def test_A_B_Variation(self):
        self.driver.find_element(By.LINK_TEXT, "A/B Testing").click()
        #time.sleep(1)
        variation_text = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/h3").text
        #print(variation_text)
        if variation_text == "A/B Test Variation 1":
            assert variation_text == "A/B Test Variation 1" , "Variation 1 was tested!"
        elif variation_text == "A/B Test Control":
            assert variation_text == "A/B Test Control" , "Variation 2 was tested!"
        else:
            self.fail("Neither of the variations were found")
        #print(variation_text)

    def test_Add_Elements(self):
        self.driver.find_element(By.LINK_TEXT, "Add/Remove Elements").click()
        #Add
        add_element_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/button")))
        number_of_elements = 5
        for i in range(0, number_of_elements):
            add_element_button.click()
        #Check
        number_of_buttons_list = self.driver.find_elements(By.CLASS_NAME, "added-manually")
        number_of_added_elements = 0
        for button in number_of_buttons_list:
            number_of_added_elements += 1
        assert number_of_added_elements == number_of_elements

    def test_Remove_Elements(self):
        self.driver.find_element(By.LINK_TEXT, "Add/Remove Elements").click()
        #Add
        add_element_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/button")))
        number_of_elements = 5
        for i in range(0, number_of_elements):
            add_element_button.click()
        #Remove
        remove_button_list = self.driver.find_elements(By.CLASS_NAME, "added-manually")
        number_of_present_elements = number_of_elements
        for button in remove_button_list:
            button.click()
            number_of_present_elements -= 1
        assert number_of_present_elements == 0




















########################################################

    # Teardown function for Unittest TestCase
    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()