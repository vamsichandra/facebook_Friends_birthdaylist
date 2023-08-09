from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set your Facebook username and password
username = "facebookid"
password = "facebookpassword"
PATH="C:/Users/bonam/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# Create a Chrome browser instance
driver = webdriver.Chrome(PATH)

# Navigate to Facebook
driver.get("https://www.facebook.com")

# Log in
email_input = driver.find_element_by_id("email")
email_input.send_keys(username)

password_input = driver.find_element_by_id("pass")
password_input.send_keys(password)

login_button = driver.find_element_by_name("login")
login_button.click()

time.sleep(5)  # Allow to load

# Navigate to the birthday page
driver.get("https://www.facebook.com/events/birthdays/")

time.sleep(5)  # Allow  to load

# Scroll to load more content
body = driver.find_element_by_tag_name("body")
for _ in range(5):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)

# Find & extract_birthdays_month-wise
birthday_elements = driver.find_elements_by_class_name("_43q7")
birthdays = {}

for element in birthday_elements:
    birthday = element.get_attribute("textContent").strip()
    if birthday:
        month = birthday.split()[0]
        day = birthday.split()[1]
        if month in birthdays:
            birthdays[month].append(day)
        else:
            birthdays[month] = [day]


with open("birthdays.txt", "w") as file:
    for month, days in birthdays.items():
        file.write(f"{month}: {', '.join(days)}\n")

# Close the browser
driver.quit()

print("Birthdays saved to birthdays.txt")
