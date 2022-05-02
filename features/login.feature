Feature: validate login

  Scenario: verify with correct user details
    Given i am in login page
    When  i enter username "admin" and password "admin"
    And  click on submit
    Then i will redirect to home page verify the title