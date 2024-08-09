import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from Pageobject.Orange_login import LoginPage, LoginFail, AddEmployee,TestUpdate,TestDelete

class TestLogin:
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"
    password1 = "Invalid password"
    first_name = "vijay"
    middle_name = "kumar"
    last_name = "king"
    license_number = "7693"
    license_expiry_date = "2034-12-31"
    date_of_birth = "1996-01-13"
    nationality = "Indian"
    marital_status = "Single"
    gender = "male"
    blood_type = "B+"
    employee="vijay"
    license_number1 = "9001"
    employee1 = "vijay"


    @pytest.fixture()
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lf = LoginFail(self.driver)
        self.ae = AddEmployee(self.driver)
        self.tu = TestUpdate(self.driver)
        self.td = TestDelete(self.driver)
        yield
        self.driver.quit()

    # Test Successful Login Functionality
    def test_successful_login(self,setup_method):
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login_button()

    # Test un-Successful Login Functionality
    def test_failed_login(self,setup_method):
        self.lf.enter_username(self.username)
        self.lf.enter_password(self.password1)
        self.lf.click_login_button()

    # Test for adding new employee in portal
    def test_add_employee(self,setup_method):
        self.ae.enter_username(self.username)
        self.ae.enter_password(self.password)
        self.ae.click_login_button()
        self.ae.click_pim_locator()
        self.ae.click_on_add()
        self.ae.enter_first_name(self.first_name)
        self.ae.enter_second_name(self.middle_name)
        self.ae.enter_last_name(self.last_name)
        self.ae.click_save()
        self.ae.enter_number(self.license_number)
        self.ae.enter_license_expiry(self.license_expiry_date)
        self.ae.enter_date_of_birth(self.date_of_birth)
        self.ae.select_nationality(self.nationality)
        self.ae.select_marital_status()
        self.ae.select_gender()
        self.ae.select_blood_type()
        self.ae.click_final_save()

    # Test for updating  employee in portal
    def test_update_employee(self,setup_method):
        self.tu.enter_username(self.username)
        self.tu.enter_password(self.password)
        self.tu.click_login_button()
        self.tu.click_pim_locator()
        self.tu.enter_employee_name(self.employee)
        self.tu.click_search()
        self.tu.click_action_button()
        self.tu.click_license(self.license_number1)
        self.tu.click_save()

    # Test for deleting employee in portal
    def test_delete_employee(self,setup_method):
        self.td.enter_username(self.username)
        self.td.enter_password(self.password)
        self.td.click_login_button()
        self.td.click_pim_locator()
        self.td.enter_employee_name(self.employee)
        self.td.click_search()
        self.td.click_action_button()
        self.td.click_yes_button()




