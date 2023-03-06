from behave import *
@When("Element page : I select one checkbox")
def step_impl(context):
    context.checkboxes_page_object.select_one_checkbox()

@Then("Element page : I am able to select the desired checkbox")
def step_impl(context):
    context.checkboxes_page_object.check_first_checkbox_is_selected()

@When("Element page : I select both checkboxes")
def step_impl(context):
    context.checkboxes_page_object.select_both_checkboxes()

@Then("Element page : I am able to see both checkboxes at the same time")
def step_impl(context):
    context.checkboxes_page_object.check_both_checkbox_are_selected()
