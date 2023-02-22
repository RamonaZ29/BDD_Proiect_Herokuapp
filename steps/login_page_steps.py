from behave import *

@When('Login page: I enter "{username}" in the username text field')
def step_impl(context, username):
	context.login_page_object.enter_username(username)

@When('Login page: I enter "{password}" in the password text field')
def step_impl(context, password):
	context.login_page_object.enter_password(password)

@when('Login page: I click on login button')
def step_impl(context):
	context.login_page_object.click_on_login_button()

@Then('I am on the secured area')
def step_impl(context):
	context.login_page_object.check_login_success()

@Then('Login page: I read the "You logged out of the secure area!" message')
def step_impl(context):
	context.login_page_object.check_logout_success()