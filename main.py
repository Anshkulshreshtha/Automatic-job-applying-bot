from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "c:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# -----------------------------------LOGIN PART
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

time.sleep(5)

Email_phone = driver.find_element(By.ID, "username")
Email_phone.send_keys("*************@gmail.com")   # email

Password = driver.find_element(By.ID, "password")
Password.send_keys("*********")  #password
Password.send_keys(Keys.ENTER)  #login by pressing enter after password

#------------------------------------------login by clicking the sign in button
# Button = driver.find_element(By.CSS_SELECTOR, "div > button")  ---method 1
# sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in") -----method 2(
# # sign_in_button.click()

#------------------------Enter the job credentials

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3227513671&f_AL=true&"
           "f_E=1%2C2&f_JT=F%2CI&f_TPR=r2592000&f_WT=2&keywords=web%20developer&refresh=true")

Easy_apply = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
Easy_apply.click()

next_button =  driver.find_element(By.CSS_SELECTOR, "form button")

for i in range(2):
    next_button.click()

questions = driver.find_element(By.CSS_SELECTOR, '[value="Yes"]')
if (questions):
    questions.click()

time.sleep(5)
experience = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
if experience.text == "":
    experience.send_keys("2")

#-----2nd question
# experience1 = driver.find_element(By.CLASS_NAME, "jobs-easy-apply-form-section__input")  # not working


Review_button = driver.find_element(By.ID, "#ember401")
Review_button.click()

Submit_button = driver.find_element(By.CSS_SELECTOR,"footer button")
Submit_button.click()

time.sleep(5)
driver.quit()
