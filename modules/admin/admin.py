from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.webdriver.common.keys import Keys;
import time;
from config_service import ConfigService;
from selenium.common.exceptions import NoSuchElementException;
import random;

class AdminDashboard:
    def __init__(self, driver_instance):
        self.config = ConfigService().get_config();
        self.driver = driver_instance;
        self.dashboard_urls = [
            "https://cloud.dealerappvantage.com/#system_administration",
            "https://cloud.dealerappvantage.com/#jobs",
            "https://cloud.dealerappvantage.com/#users",
            "https://cloud.dealerappvantage.com/#clients",
            "https://cloud.dealerappvantage.com/#accounts",
            "https://cloud.dealerappvantage.com/#apps",
            "https://cloud.dealerappvantage.com/#app_management_center",
            "https://cloud.dealerappvantage.com/#communication",
            "https://cloud.dealerappvantage.com/#messaging",
            "https://cloud.dealerappvantage.com/#messaging?filter=Location",
            "https://cloud.dealerappvantage.com/#marketing",
            "https://cloud.dealerappvantage.com/#customization",
        ];
        self.dashboard_urls_react_site = [
            "https://dapp.getdealerapp.com/",
            "https://dapp.getdealerapp.com/staffs?page=1",
            "https://dapp.getdealerapp.com/app_management_center",
            "https://dapp.getdealerapp.com/clients",
            "https://dapp.getdealerapp.com/communication",
            "https://dapp.getdealerapp.com/customer_profiles?page=1",
            "https://dapp.getdealerapp.com/departments?page=1&sort=3",
            "https://dapp.getdealerapp.com/rewards?sort=3&page=1"
        ];


    def traverse_admin_dashboard(self):
        for url in self.dashboard_urls:
            self.driver.get(url);
            num_r = random.randint(10, 20)
            time.sleep(num_r);


    def traverse_admin_dashboard_react_site(self):
        for url in self.dashboard_urls_react_site:
            self.driver.get(url);
            num_r = random.randint(10, 20)
            time.sleep(num_r);
