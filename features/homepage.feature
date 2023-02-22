
Feature: Test homepage on the-internet.herokuapp.com webpage

  Background:
    Given Home page: I am on the-internet.herokuapp.com

    @Home
  Scenario Outline: Check that the homepage has access to 3 different elements
    When Home page: I look for "<element>" and I click on it
    Then I am on the "<element_page>" page
    Examples:
      | element               | element_page                                                     |
      | Form Authentication   | https://the-internet.herokuapp.com/login                         |
      | File Download         | https://the-internet.herokuapp.com/download                      |
      | Redirect Link         | https://the-internet.herokuapp.com/redirector                    |