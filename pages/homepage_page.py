from browser import Browser
from selenium.webdriver.common.by import By

class Home_page(Browser):

	def navigate_to_homepage(self):
		self.chrome.get("https://the-internet.herokuapp.com/")  # main page

	def click_on_element(self, element):
		self.chrome.find_element(By.LINK_TEXT, element).click()

	def check_actual_page(self, element_page):
		current_url = self.chrome.current_url # check actual page
		assert element_page == current_url, f"Error, the page expected is: {element_page}, but we got: {current_url}"

	def click_alerts(self):
		self.chrome.find_element(By.LINK_TEXT, "JavaScript Alerts").click()

	def navigate_to_checkboxes(self):
		self.chrome.find_element(By.LINK_TEXT, "Checkboxes").click()