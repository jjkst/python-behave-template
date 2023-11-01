from behave import *

@given('user enters "{name}" and "{password}"')
def step_implpy(context, name, password):
    print("Username for login: {}".format(name))
    print("Password for login: {}".format(password))

@given('user enters name and password')
def step_impl(context):
#access multiline text with .text attribute
      print("Multiline Text: " + context.text)

@then('user should be logged in')
def step_implpy(context):
    pass