@current
Feature: Parse

Scenario: Check Debit transactions
    Given user is on "debit" screen
    When user makes a payment

Scenario: Check Credit transactions
    Given user is on "credit" screen