Feature: User information
Scenario Outline: Check login functionality
   Given user enters "<name>" and "<password>"
   Then user should be logged in
   Examples: Credentials
      | name  | password |
      | user1 | pwd1     |
      | user2 | pwd2     |

Scenario: Multiline functionality
   Given user enters name and password
         """
         Tutorialspoint Behave
          Topic – Multiline Text
         """
   Then user should be logged in

Scenario: Check login functionality
   Given Collection of credentials
      | username |password |
      | user1    | pwd1    |
      | user2    | pwd2    |
   Then user should be logged in
