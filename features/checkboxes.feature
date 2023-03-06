Feature: Test Checkboxes functionality on the-internet.herokuapp.com webpage

  Background:
    Given Home page: I am on the-internet.herokuapp.com

  Scenario: Check if I can select one checkbox
    When Homepage: I check for "Checkboxes" element and I click on it
    When Element page : I select one checkbox
    Then Element page : I am able to select the desired checkbox

  Scenario: Check if I can selet all checkboxes at the same time
    When Homepage: I check for "Checkboxes" element and I click on it
    When Element page : I select both checkboxes
    Then Element page : I am able to see both checkboxes at the same time