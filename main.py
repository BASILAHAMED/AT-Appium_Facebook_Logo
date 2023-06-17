from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Appium server configuration
appium_server = 'http://localhost:4723/wd/hub'

# Desired capabilities for Chrome browser
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'pixel_3a',
    'browserName': 'Chrome',
    'chromedriverExecutable': 'set driver path here'
}

# Initialize the webdriver
driver = webdriver.Remote(appium_server, desired_caps)

# Open facebook.com in Chrome browser
driver.get('https://m.facebook.com')

# Check if the Facebook logo is displayed to verify if the page loaded successfully
try:
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//button[@value="Log In"]')))

    # Facebook logo element found, page loaded successfully
    print("Facebook page loaded successfully!")
except NoSuchElementException:
    # Facebook logo element not found, page failed to load
    print("Failed to load Facebook page!")

# Close the browser and quit the webdriver
driver.quit()
