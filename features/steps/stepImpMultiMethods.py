from behave import *
from behave import register_type
from parse_type import TypeBuilder

parse_dress = TypeBuilder.make_choice(["shirts", "t-shirts"])
parse_pant = TypeBuilder.make_choice(["pants", "gowns"])
register_type(Dress=parse_dress)
register_type(Pant=parse_pant)

@given("User is on shop")
def step_user_shop(context):
    pass

# multiple methods being used .
@when(u"user purchases {count:n} {d:Dress}")
def step_dress(context, count, d):
    print("User purchased: ")
    print(d)
    print("Count is:")
    print(count)

@when(u"user purchases {count:n} {p:Pant}")
def step_pant(context, count, p):
    print("User purchased: ")
    print(p)
    print("Count is:")
    print(count)