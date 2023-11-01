from behave import *
from modules.login_module import LModel

@given('Collection of credentials')
def step_impl(context):
    model = getattr(context, "model", None)
    if not model:
        context.model = LModel()
    #iterate rows of table
    for r in context.table:
        context.model.usr_addition(r["username"], password=r["password"])
        assert r["username"] == "failed"