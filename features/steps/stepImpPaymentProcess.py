from behave import *
from behave import register_type
from parse_type import TypeBuilder

@given('launch application')
def launch_application(context):
   print('launch application')

@then('Input credentials')
def input_credentials(context):
   print('Input credentials')

@given('user is on credit card payment screen')
def credit_card_pay(context):
   print('User is on credit card payment screen')

@then('user should be able to complete credit card payment')
def credit_card_pay_comp(context):
   print('user should be able to complete credit card pay')

@given('user is on debit card payment screen')
def debit_card_pay(context):
   print('User is on debit card payment screen')

@then('user should be able to complete debit card payment')
def debit_card_pay_comp(context):
   print('user should be able to complete debit card payment')

#passing parameter in % datatype enclosed in {}
@when('user makes a payment of "{p:%}" percent of total')
def step_impl(context, p):
   print('Number is: ')
   print(p)

#convert parsed text to float
def parse_percent(t):
   return float(t)
#register user-defined type
register_type(Float=parse_percent)

@when('user makes a payment of "{amount:Float}" of total')
def step_impl(context, amount):
   print('Number is: ')
   print(amount)

# -- ENUM: Yields True (for "yes"), False (for "no")
parse_response = TypeBuilder.make_enum({"yes": True, "no": False})
register_type(Response=parse_response)

@when('User asks "{q}"')
def step_question(context, q):
   print("Question is: ")
   print(q)

@then('response is "{a:Response}"')
def step_answer(context, a):
   print("Answer is: ")
   print(a)