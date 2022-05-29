from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import gmtime, strftime
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json
import datetime
# driver = webdriver.Chrome(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(ChromeDriverManager().install() , options=options)
try:
    # driver.get("https://www.forexfactory.com/timezone")


    # select = Select(driver.find_element_by_id('timezone'))
    # select.select_by_index(92)
    # selected_option = select.first_selected_option
    # time.sleep(10)
    # button = driver.find_element_by_class_name('button--pressable')
    # # print(button)
    # button.click()
   
    # time.sleep(15)

    driver.get("https://www.forexfactory.com/calendar?week=this")
    # Get the table
    table = driver.find_element(By.CLASS_NAME, "calendar__table ")
    # print(table)
    # # Iterate over each table row
    dataDict = {
        "dateTime" : [] 
    }
    for row in table.find_elements(By.TAG_NAME, "tr"):
        # list comprehension to get each cell's data and filter out empty cells
        row_data = list(filter(None, [td.text for td in row.find_elements(By.TAG_NAME, "td")]))

        if row_data == []:
            continue
        dataDict['dateTime'].append(row_data)
    with open('./Data.json' , "r") as readingJsonData:
        jsonData = json.load(readingJsonData)
        jsonData.append(dataDict)
    with open("./Data.json" , "w") as writingJsonData:
        json.dump(jsonData , writingJsonData , indent = 4)


except Exception as e:
    pass
finally:
    driver.quit()