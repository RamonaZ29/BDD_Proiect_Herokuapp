from browser import Browser
from selenium.webdriver.common.by import By

class JS_Alerts(Browser):
    JS_PROMPT = (By.XPATH, '//*[@id="content"]/div/ul/li[3]/button')
    DISPLAYED_TEXT_IDENTIFICATION = (By.ID, "result")
    INSERTED_TEXT = "Have a good one!"
    JS_ALERT = (By.XPATH, '//*[@id="content"]/div/ul/li[1]/button' )

    def click_JS_prompt_button(self):
        self.chrome.find_element(*self.JS_PROMPT).click()

    def accept_alert_with_text(self):
        popup_window = self.chrome.switch_to.alert
        popup_window.send_keys("Have a good one!")
        popup_window.accept()

    def check_displayed_text_result(self):
        displayed_text_result = self.chrome.find_element(*self.DISPLAYED_TEXT_IDENTIFICATION).text
        assert self.INSERTED_TEXT in displayed_text_result.strip(), f"Error, expected the message: " \
                                                    f"{self.INSERTED_TEXT}, but we got: {displayed_text_result}"

    def cancel_popup_window_without_text(self):
        popup_window = self.chrome.switch_to.alert
        popup_window.dismiss()

    def check_result_when_cancel_popup(self):
        displayed_text_result = self.chrome.find_element(*self.DISPLAYED_TEXT_IDENTIFICATION).text
        expected_text = "You entered: null"
        assert expected_text == displayed_text_result, f"Error, expected the message: " \
                                                    f"{expected_text}, but we got: {displayed_text_result}"

    def click_JS_alert_button(self):
        self.chrome.find_element(*self.JS_ALERT).click()

    def accept_alert(self):
        popup_window = self.chrome.switch_to.alert
        popup_window.accept()
    def check_accept_message_result(self):
        displayed_text_result = self.chrome.find_element(*self.DISPLAYED_TEXT_IDENTIFICATION).text
        expected_text = "You successfully clicked an alert"
        assert expected_text == displayed_text_result, f"Error, expected the message: " \
                                                    f"{expected_text}, but we got: {displayed_text_result}"