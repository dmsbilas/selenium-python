from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.webdriver.common.keys import Keys;
import time;
from config_service import ConfigService;
from selenium.common.exceptions import NoSuchElementException;

# driver = webdriver.Chrome();

class Login:
    def __init__(self):
        self.config = ConfigService().get_config();
        self.driver = webdriver.Chrome();

    def apply_wait(self):
        time.sleep(self.config['default_waiting_time']);

    def open_login_page(self):
        self.driver.get(self.config['base_url']);

    def give_username(self):
        user_name_elm = self.driver.find_element(By.XPATH,'//*[@id="Username"]');
        user_name_elm.send_keys(self.config['user']);

    def give_password(self):
        password_elm = self.driver.find_element(By.XPATH,'//*[@id="Password"]');
        password_elm.send_keys(self.config['password']);

    def submit_login_form(self):
        login_btn_elm = self.driver.find_element(By.XPATH,"/html/body/div/form/div[3]/input");
        login_btn_elm.click();

    def close_popups(self):
        pop_up_modal_elm = self.driver.find_element(By.XPATH,"/html/body/div[4]/div/header/a");
        pop_up_modal_elm.click();

    def login_test_result(self):
        try:
            admin_itm = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[4]/nav/div/ul/li[1]/a/span');
            print("Login successful.");
            assert admin_itm.is_displayed(), "Successfully logged in with valid credentials" ;
        except NoSuchElementException:
            assert "Left sidebar not shown";

    def get_driver_instance(self):
        return self.driver;

    def close_browser(self):
        self.driver.close();

