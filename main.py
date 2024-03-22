from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get('https://cloud.dealerappvantage.com/Account/SignIn?ReturnUrl=%2F#welcome');

time.sleep(3) # Let the user actually see something!

# input id Username
# input id Password

# Getting user login form elements

user_name = driver.find_element(By.XPATH,'//*[@id="Username"]');
password = driver.find_element(By.XPATH,'//*[@id="Password"]');

user_name.send_keys("abilas");
time.sleep(3) # Let the user actually see something!
password.send_keys("welcome1");
time.sleep(5) # Let the user actually see something!

# click login button
driver.find_element(By.XPATH,"/html/body/div/form/div[3]/input").click();
time.sleep(10);

# find next button
# driver.find_element(By.XPATH,"/html/body/div[4]/div/footer/ul/li/a").click();
# driver.find_element(By.XPATH,'/html/body/div[4]/div/footer/ul/li/a').click();

driver.refresh()

time.sleep(10);

# It seems login is done
# left sidebar menu items
admin = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[4]/nav/div/ul/li[1]/a/span');
app_management_center = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[4]/nav/div/ul/li[1]');
communication = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[4]/nav/div/ul/li[4]/a');
analytics = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[4]/nav/div/ul/li[3]');
marketing = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[4]/nav/div/ul/li[6]');




# marketing_app_selection_bar = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]'); 


admin.click();
time.sleep(30);


jobs = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[4]/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/ul/li[1]/a');
users = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[4]/div[3]/div/div[4]/div/div[1]/div/div/div[2]/div/ul/li[2]/a');
clients = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[4]/div[3]/div/div[4]/div/div[1]/div/div/div[2]/div/ul/li[3]/a');
accounts = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[4]/div[3]/div/div[4]/div/div[1]/div/div/div[2]/div/ul/li[4]/a');

# jobs.click();

# time.sleep(15);
# driver.navigate().back(); 
# Now I am on Admin Dashboard page
# time.sleep(5);

def left_items(left_menu_name, item_arr):
    left_menu_name.click();
    time.sleep(10);
    for item in item_arr:
        item.click();
        time.sleep(10);
        driver.navigate().back(); 
        time.sleep(10);

while (True) :
    left_items(admin, [jobs, users, clients, accounts]);
