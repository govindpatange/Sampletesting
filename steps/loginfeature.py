from behave import *
from selenium import webdriver

@given(u'i am in login page')
def step_impl(context):
    context.driver=webdriver.Chrome(executable_path="C:\\Users\\ABC\\PycharmProjects\\pythonProjecttesting\\chromedriver.exe")
    context.driver.get("https://demo.guru99.com/test/newtours/index.php")

@when(u'i enter username "{user}" and password "{pwd}"')
def step_impl(context,user,pwd):
    context.driver.find_element_by_name("userName").send_keys(user)
    context.driver.find_element_by_name("password").send_keys(pwd)


@when(u'click on submit')
def step_impl(context):
    context.driver.find_element_by_name("submit").click()


@then(u'i will redirect to home page verify the title')
def step_impl(context):
    print(context.driver.title)