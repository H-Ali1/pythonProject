from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
import html2text

iteratedPlaces = []

def main():
    getLink = linkToWeb()


def linkToWeb():

    driver = webdriver.Chrome()
    # link to York Area in list format
    driver.get("https://www.spareroom.co.uk/flatshare/?search_id=1125846612&mode=list")
    driver.implicitly_wait(10)

    for i in range(1, 11):
        listofPlaces = driver.find_element(by=By.XPATH, value="//*[@id='maincontent']/ul/li["+ str(i) +"]/article").text
        print(listofPlaces)
        print()
        process = processing(listofPlaces)


def processing(places):

    newCount = 0
    getHTML = html2text.html2text(places)
    getHTML = getHTML.split()
    print(getHTML)

    for i in range(len(getHTML)):
        #print(getHTML[i])
        if getHTML[i] == "TODAY":
            iteratedPlaces.append(getHTML[newCount:i])
            newCount = i

    print(iteratedPlaces)
main()