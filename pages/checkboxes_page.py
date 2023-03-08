import time

from browser import Browser
from selenium.webdriver.common.by import By

class Checkboxes(Browser):

    FIRST_CHECKBOX = (By.XPATH, '//form/input[1]')
    SECOND_CHECKBOX = (By.XPATH, '//form/input[2]')
    def select_one_checkbox(self):
        desired_checkbox = self.chrome.find_element(*self.FIRST_CHECKBOX)
        desired_checkbox.click()

    def check_first_checkbox_is_selected(self):
        first_checkbox = self.chrome.find_element(*self.FIRST_CHECKBOX)
        assert first_checkbox.is_selected(), f"Checkbox not selected!"

    def select_both_checkboxes(self):
        pass
        first_checkbox = self.chrome.find_element(*self.FIRST_CHECKBOX)
        first_checkbox.click()
        # second_checkbox = self.chrome.find_element(*self.SECOND_CHECKBOX)
        # second_checkbox.click() # acest pas nu este necesar deoarece cand se deschide
                                  # pagina elementului "Checkboxes", ,checkbox 2 este deja selectat, by default.

    def check_both_checkbox_are_selected(self):
        first_checkbox = self.chrome.find_element(*self.FIRST_CHECKBOX)
        second_checkbox = self.chrome.find_element(*self.SECOND_CHECKBOX)
        assert first_checkbox.is_selected(), f"Checkbox 1 not selected!"
        assert second_checkbox.is_selected(), f"Checkbox 2 not selected!"







