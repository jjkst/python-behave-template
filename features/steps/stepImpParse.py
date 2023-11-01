from behave import *

#define parser type
use_step_matcher("parse")
@given('user is on "{p}" screen')
def step_impl(context, p):
   print(p)
@when('user makes a payment')
def step_pay_complete(context):
   pass