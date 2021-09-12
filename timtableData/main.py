import time
from selenium import webdriver
from datetime import date
import html2text
import calendar
import re

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

    previous = 0
    # Navigate to Minerva Website where timetable is located
    driver = webdriver.Chrome()
    driver.get("https://minerva.leeds.ac.uk")
    time.sleep(1)
    #beforeUsername = driver.find_element_by_id("i0116")
    #beforeUsername.send_keys("ed19h6a@leeds.ac.uk")
    #driver.find_element_by_id("idSIButton9").click()
   # time.sleep(3)
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
    day = driver.find_element_by_xpath("//span[contains(@class,'date')]").text
    day = day.split(" ", 1)[0] + ": "

    getEvent = driver.find_element_by_xpath("//*[@class='day-events']").get_attribute('innerHTML')

    # run string handling
    preProcessing(getEvent)

    # gets First lesson times
    startTime = driver.find_element_by_xpath("//*[@class='start']").get_attribute('innerHTML')
    endTime = driver.find_element_by_xpath("//*[@class='end']").get_attribute('innerHTML')
    nameOfClass = driver.find_element_by_xpath("//*[@id='events']/li[1]/ul/li[1]/a/div[2]/div[2]/div/div[1]/span[3]").get_attribute('innerHTML')

    # prints out the start and end time of the class
    string = day + startTime.strip()[20:25] + " to " + endTime.strip()[20:25] + "\nYou have: "\
             + nameOfClass.strip()
    # prints out the name of the class to attend
    return string


def preProcessing(getEvent):
    getTimes = []
    getLesson = []
    previous = 0

    getHTML = html2text.html2text(getEvent)
    getHTML = getHTML.split()
    print(getHTML)
    for i in range(len(getHTML)):
        if getHTML[i] == "until":
            getTimes.append(getHTML[i-1:i+2])


    foundD = False
    for i in range(len(getHTML)):
        if getHTML[i] == "d":
            previous = i
            foundD = True
        elif getHTML[i] == "*" and foundD:
            getLesson.append(getHTML[previous+1:i])
            foundD = False

    # Prints out corresponding time and lesson name for day
    for x in range(len(getTimes)):
        print(' '.join(getTimes[x]) + " " + ' '.join(getLesson[x]))
        print()

main()

