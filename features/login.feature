Feature: Login Functionality
  Scenario: Successful login with valid credentials
    Given user is on the login page
    When user enters valid username & password
    And click on the login button
    Then the user should be redirected to the dashboard page