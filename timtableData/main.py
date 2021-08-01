
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from datetime import date
import calendar
def main():
    #theDay = getDate()
    lesson = usingSelenium()

    print("For", lesson)


# Gets the day of today assuming you are checking timetable for today
def getDate():
    theDate = date.today()
    theDate = calendar.day_name[theDate.weekday()]
    return theDate

def usingSelenium():

    # Navigate to Minerva Website where timetable is located
    driver = webdriver.Chrome()
    driver.get("https://minerva.leeds.ac.uk")
    # Enter email and passwords
    username = driver.find_element_by_id("userNameInput")
    username.clear()
    username.send_keys("")

    password = driver.find_element_by_id("passwordInput")
    password.clear()
    password.send_keys("")
    driver.find_element_by_id("submitButton").click()
    # Navigate to timetable page
    driver.get("https://mytimetable.leeds.ac.uk/m")
    time.sleep(2)

    # get the date from the timetable page
    day = driver.find_element_by_xpath("//*[@class='day-header']").get_attribute('innerHTML')
    print(date)

    # Find lesson times
    startTime = driver.find_element_by_xpath("//*[@class='start']").get_attribute('innerHTML')
    endTime = driver.find_element_by_xpath("//*[@class='end']").get_attribute('innerHTML')
    nameOfClass = driver.find_element_by_xpath("//*[@id='events']/li[1]/ul/li[1]/a/div[2]/div[2]/div/div[1]/span[3]").get_attribute('innerHTML')

    # prints out the start and end time of the class
    string = "Your lesson is from: " + startTime.strip()[20:25] + " to " + endTime.strip()[20:25] + "\n" + "Lesson Name: "\
             + nameOfClass.strip()
    # prints out the name of the class to attend
    return string

main()

