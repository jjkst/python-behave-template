from behave import *

@when('User enters payment details')
def enters_payment_details(context):
    print('When User enters payment details')

@when('User completes payment')
def completes_payment(context):
    print('When User completes payment')

@then('User should get success message')
def get_success_message(context):
    print('Then User should get success message')

@given('User keys in payment info and submits')
def payment_info_and_submits(context):
#passing steps within steps with context.execute_steps
    context.execute_steps(u"""
        Given User is on payment screen
        When User enters payment details
        And User completes payment
        """)

@then('success message should get displayed')
def success_message(context):
    print('Then success message should get displayed')