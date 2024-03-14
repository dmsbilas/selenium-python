from selenium import webdriver

# Create a new instance of the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("http://bilassiddiq.com/")

# Locate the form element (assuming it has an ID)
form_element = driver.find_element(By.ID, "form_id")

# Close the browser window
# driver.close();