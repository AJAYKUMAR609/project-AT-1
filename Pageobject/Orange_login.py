
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
        try:
            self.driver.get(self.url)
        except:
            print("Page load timed out. Check your internet connection or URL.")

    def enter_username(self, username):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.username_locator)).send_keys(username)
        except:
            print("Username input field not found. Verify your locator.")

    def enter_password(self, password):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.password_locator)).send_keys(password)
        except:
            print("Password input field not found. Verify your locator.")

    def click_login_button(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button_locator)).click()
        except:
            print("Login button not clickable. Check your page state or locator.")


class LoginFail:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.NAME, 'username')
        self.password_locator = (By.NAME, 'password')
        self.login_button_locator = (By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

    def enter_username(self, username):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.username_locator)).send_keys(username)
        except:
            print("check username and enter")

    def enter_password(self, password):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.password_locator)).send_keys(password)
        except:
            print("password is not correct check and enter ")

    def click_login_button(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button_locator)).click()
        except:
            print("Login button not clickable. Check your page state or locator.")


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
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.username_locator)).send_keys(username)
        except :
            print("enter correct user name ")

    def enter_password(self, password):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.password_locator)).send_keys(password)
        except:
            print("enter valid password")

    def click_login_button(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button_locator)).click()
        except:
            print("Login button not clickable. Check your page state or locator.")

    def click_pim_locator(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.pim_module_locator)).click()
        except:
            print("not able to click pim")

    def click_on_add(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.click_add)).click()
        except:
            print("Add button not found or not clickable. Verify your locator.")

    def enter_first_name(self, first_name):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.firstname_locator)).send_keys(first_name)
        except:
            print("first name  not found or not clickable. Verify your locator.")

    def enter_second_name(self,middle_name):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.middle_name_locator)).send_keys(middle_name)
        except:
            print("second name  not clickable. Verify your locator.")

    def enter_last_name(self, last_name):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.lastname_locator)).send_keys(last_name)
        except:
            print("last name  not clickable. Verify your locator.")


    def click_save(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.save_button_locator)).click()
        except:
            print("save button not found or not clickable. Verify your locator.")

    def enter_number(self, number):
        try:
           number_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input')))
           number_field.clear()
           number_field.send_keys(number)
        except:
            print("enter  button not found or not clickable. Verify your locator.")

    def enter_license_expiry(self, number):
        try:
            number_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input')))
            number_field.clear()
            number_field.send_keys(number)
        except:
            print("enter license  button not found or not clickable. Verify your locator.")

    def enter_date_of_birth(self, number):
        try:
            number_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input')))
            number_field.clear()
            number_field.send_keys(number)
        except:
           print("dob button not found or not clickable. Verify your locator.")

    def select_nationality(self,nationality):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.nationality_dropdown_locator)).send_keys(nationality)
        except:
            print("nationality button not found or not clickable. Verify your locator.")

    def select_marital_status(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.marital_status_dropdown_locator)).click()
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.marital_status_option_locator)).click()
        except:
            print("marital button not found or not clickable. Verify your locator.")

    def select_gender(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.gender_locator)).click()
        except:
            print("Add gender button not found or not clickable. Verify your locator.")

    def select_blood_type(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.blood_type_dropdown_locator)).click()
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.blood_type_option_locator)).click()
        except:
            print("Add  blood type button not found or not clickable. Verify your locator.")

    def click_final_save(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.final_save_button_locator)).click()
        except:
            print("save  button not found or not clickable. Verify your locator.")

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
        self.save_button_locator = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button')


    def navigate_to_login_page(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.username_locator)).send_keys(username)
        except:
            print("enter user name  not found or not clickable. Verify your locator.")

    def enter_password(self, password):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.password_locator)).send_keys(password)
        except:
            print("enter password is not found or not clickable. Verify your locator.")

    def click_login_button(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.login_button_locator)).click()
        except:
            print("click login button not found or not clickable. Verify your locator.")

    def click_pim_locator(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.pim_module_locator)).click()
        except:
            print("pim button not found or not clickable. Verify your locator.")

    def enter_employee_name(self,employee_name):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.employee_name)).send_keys(employee_name)
        except:
            print("employee name search button not found or not clickable. Verify your locator.")

    def click_search(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.search)).click()
        except:
            print("search button not found or not clickable. Verify your locator.")

    def click_action_button(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.action_button)).click()
        except:
            print("Action button not found or not clickable. Verify your locator.")

    def click_license(self, number):
        try:
            number_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input')))
            number_field.clear()
            number_field.send_keys(number)
        except:
            print("click button not found or not clickable. Verify your locator.")

    def click_save(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.save_button_locator)).click()
        except:
            print("save button not found or not clickable. Verify your locator.")

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
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.username_locator)).send_keys(username)
        except:
            print("user name  button not found or not clickable. Verify your locator.")

    def enter_password(self, password):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.password_locator)).send_keys(password)
        except:
            print("password button not found or not clickable. Verify your locator.")

    def click_login_button(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.login_button_locator)).click()
        except:
            print("click login button not found or not clickable. Verify your locator.")

    def click_pim_locator(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.pim_module_locator)).click()
        except:
            print("pim button not found or not clickable. Verify your locator.")

    def enter_employee_name(self,employee_name):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.employee_name)).send_keys(employee_name)
        except:
           print("employee name  button not found or not clickable. Verify your locator.")

    def click_search(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.search)).click()
        except:
            print("search  button not found or not clickable. Verify your locator.")

    def click_action_button(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.action_button)).click()
        except:
            print("Action button not found or not clickable. Verify your locator.")

    def click_yes_button(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.delete_button)).click()
        except:
            print("click yes button not found or not clickable. Verify your locator.")








