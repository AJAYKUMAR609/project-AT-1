
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.username_locator = (By.NAME, 'username')
        self.password_locator = (By.NAME, 'password')
        self.login_button_locator = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

    def navigate_to_login_page(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_locator)
        ).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password_locator)
        ).send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button_locator)
        ).click()


class LoginFail:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.NAME, 'username')
        self.password_locator = (By.NAME, 'password')
        self.login_button_locator = (By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.username_locator)
        ).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.password_locator)
        ).send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button_locator)
        ).click()

class AddEmployee:
    def __init__(self,driver):
        self.driver = driver
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.username_locator = (By.NAME, "username")
        self.password_locator = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        self.login_button_locator = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        self.pim_module_locator = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span')
        self.click_add=(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
        self.firstname_locator = (By.NAME, "firstName")
        self.middle_name_locator = (By.NAME, "middleName")
        self.lastname_locator = (By.NAME, "lastName")
        self.save_button_locator = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
        self.license_number_locator = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input')
        self.license_expiry_date_locator = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input')
        self.nationality_dropdown_locator = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]')
        self.marital_status_dropdown_locator = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]')
        self.marital_status_option_locator = (By.XPATH, "//span[text()='Single']")
        self.date_of_birth_locator = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input')
        self.gender_locator = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label')
        self.blood_type_dropdown_locator = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]')
        self.blood_type_option_locator = (By.XPATH, "//span[text()='B+']")
        self.final_save_button_locator = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button')

    def navigate_to_login_page(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_locator)
        ).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.password_locator)
        ).send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.login_button_locator)
        ).click()

    def click_pim_locator(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.pim_module_locator)).click()

    def click_on_add(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.click_add)
        ).click()

    def enter_first_name(self, first_name):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.firstname_locator)
            ).send_keys(first_name)

    def enter_second_name(self,middle_name):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.middle_name_locator)
        ).send_keys(middle_name)

    def enter_last_name(self, last_name):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.lastname_locator)
        ).send_keys(last_name)

    def click_save(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.save_button_locator)
        ).click()

    def enter_number(self, number):
        number_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'))
        )
        number_field.clear()
        number_field.send_keys(number)

    def enter_license_expiry(self, number):
        number_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'))
        )
        number_field.clear()
        number_field.send_keys(number)

    def enter_date_of_birth(self, number):
        number_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'))
        )
        number_field.clear()
        number_field.send_keys(number)

    def select_nationality(self,nationality):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.nationality_dropdown_locator)
        ).send_keys(nationality)

    def select_marital_status(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.marital_status_dropdown_locator)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.marital_status_option_locator)
        ).click()

    def select_gender(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.gender_locator)
        ).click()

    def select_blood_type(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.blood_type_dropdown_locator)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.blood_type_option_locator)
        ).click()

    def click_final_save(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.final_save_button_locator)
        ).click()

class TestUpdate:
    def __init__(self,driver):
        self.driver = driver
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.username_locator = (By.NAME, "username")
        self.password_locator = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        self.login_button_locator = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        self.pim_module_locator = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span')
        self.employee_name = (By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input')
        self.search=(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')
        self.action_button = (By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]')
        self.license_locator = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input')

    def navigate_to_login_page(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_locator)
        ).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.password_locator)
        ).send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.login_button_locator)
        ).click()

    def click_pim_locator(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.pim_module_locator)).click()

    def enter_employee_name(self,employee_name):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.employee_name)
        ).send_keys(employee_name)

    def click_search(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.search)
        ).click()

    def click_action_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.action_button)
        ).click()

    def click_license(self, number):
        number_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'))
        )
        number_field.clear()
        number_field.send_keys(number)

class TestDelete:
    def __init__(self,driver):
        self.driver = driver
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.username_locator = (By.NAME, "username")
        self.password_locator = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        self.login_button_locator = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        self.pim_module_locator = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span')
        self.employee_name = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input')
        self.search=(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')
        self.action_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]')
        self.delete_button = (By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]')

    def navigate_to_login_page(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_locator)
        ).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.password_locator)
        ).send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.login_button_locator)
        ).click()

    def click_pim_locator(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.pim_module_locator)).click()

    def enter_employee_name(self,employee_name):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.employee_name)
        ).send_keys(employee_name)

    def click_search(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.search)
        ).click()

    def click_action_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.action_button)
        ).click()

    def click_yes_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.delete_button)
        ).click()








