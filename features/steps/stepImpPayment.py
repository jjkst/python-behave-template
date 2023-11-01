from behave import *

@given('User is on Payment screen')
def impl_bkpy(context):
    print('User is on Payment screen')

@when('User clicks on Payment types')
def impl_bkpy(context):
    print('User clicks on Payment types')

@then('User should get Types Cheque and Cash')
def impl_bkpy(context):
    print('User should get Types Cheque and Cash')