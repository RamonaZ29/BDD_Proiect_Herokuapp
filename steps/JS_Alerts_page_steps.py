from behave import *

@When('Element page: I click "Click for JS Prompt" button')
def step_impl(context):
    context.JS_Alerts_page_object.click_JS_prompt_button()

@When('Element page:I insert "Have a good one!" and I click "OK" button')
def step_impl(context):
    context.JS_Alerts_page_object.accept_alert_with_text()

@Then('Then Element page: Message is displayed under the "Result:"')
def step_impl(context):
    context.JS_Alerts_page_object.check_displayed_text_result()

@When('When Element page: Pop-up window shows up and I click "Cancel" button')
def step_impl(context):
    context.JS_Alerts_page_object.cancel_popup_window_without_text()

@Then('Then Element page: I get displayed "You entered: null" message under "Result:"')
def step_impl(context):
    context.JS_Alerts_page_object.check_result_when_cancel_popup()

@When('Element page: I click "Click for JS Alert" button')
def step_impl(context):
    context.JS_Alerts_page_object.click_JS_alert_button()

@When('Element page:I click "OK" on the pop up window')
def step_impl(context):
    context.JS_Alerts_page_object.accept_alert()

@Then('Element page: "You successfully clicked an alert" message is displayed under the "Result:"')
def step_impl(context):
    context.JS_Alerts_page_object.check_accept_message_result()


