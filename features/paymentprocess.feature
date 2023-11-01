Feature: Payment Process
    Background:
        Given launch application
        Then Input credentials
    Scenario: Credit card transaction
        Given user is on credit card payment screen
        Then user should be able to complete credit card payment
    Scenario: Debit card transaction
        Given user is on debit card payment screen
        Then user should be able to complete debit card payment

    Scenario Outline: Credit card transaction with data type
        Given user is on credit card payment screen
        When user makes a payment of "<p>" percent of total
        Examples: Amounts
            | p   |
            | 80% |
            | 90% |

    Scenario Outline: Credit card transaction with user defined data type
        Given user is on credit card payment screen
        When user makes a payment of "<amount>" of total
        Examples: Amounts
            | amount |
            | 75     |
            | 85     |

    Scenario: Response
        When User asks "Is payment done?"
        Then response is "No"