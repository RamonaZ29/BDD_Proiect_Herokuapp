from browser import  Browser
from pages.JS_Alerts_page import JS_Alerts
from pages.checkboxes_page import Checkboxes
from pages.homepage_page import Home_page
from pages.login_page import Login_page
from pages.secure_page import Secure_page

#  before_all este o metoda recunoscuta de libraria behave si se va executa inainte de toate testele
def before_all(context):  # context - cutiuta in care vom stoca toate atributele ce pot fi folosite in alte fisiere
	context.browser = Browser()
	context.home_page_object = Home_page()
	context.login_page_object = Login_page()
	context.secure_page_object = Secure_page()
	context.JS_Alerts_page_object = JS_Alerts()
	context.checkboxes_page_object = Checkboxes ()

#  after_all este o metoda recunoscuta de libraria behave si care se va executa dupa toate testele
def after_all(context):
	context.browser.close()