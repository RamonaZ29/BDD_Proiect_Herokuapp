Feature: Check Javascript Alerts functionality on the-internet.herokuapp.com webpage

  Background:
    Given Home page: I am on the-internet.herokuapp.com

   @JSAlerts @JSPrompt @1
  Scenario: I insert text in the JS Prompt pop-up window
    When Homepage: I check for "JavaScript Alerts" element and I click on it
    When Element page: I click "Click for JS Prompt" button
    When Element page:I insert "Have a good one!" and I click "OK" button
    Then Element page: Message is displayed under the "Result:"

   @JSAlerts @JSPrompt
  Scenario: I click "Cancel" on JS Prompt pop-up window without input
    When Homepage: I check for "JavaScript Alerts" element and I click on it
    When Element page: I click "Click for JS Prompt" button
    When Element page: Pop-up window shows up and I click "Cancel" button
    Then Element page: I get displayed "You entered: null" message under "Result:"

    @JSAlerts @JSAlert
    Scenario: I accept JS Alert
    When Homepage: I check for "JavaScript Alerts" element and I click on it
    When Element page: I click "Click for JS Alert" button
    When Element page:I click "OK" on the pop up window
    Then Element page: "You successfully clicked an alert" message is displayed under the "Result:"

