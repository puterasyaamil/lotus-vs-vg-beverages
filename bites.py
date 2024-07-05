import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

url ='https://www.bites.com.my/collections/beverages?sort_by=price-ascending'

name =[]
price=[]
page= 1

driver = webdriver.Chrome()

driver.get(url)

time.sleep(5)

zipcode = driver.find_element(By.XPATH,'//*[@id="postcode-popup-inner"]/div[1]/div/input')
zipcode.send_keys('53000')

time.sleep(5)

contbutton = driver.find_element(By.XPATH,'//*[@id="postcode-popup-inner"]/div[3]/div')
contbutton.click()

time.sleep(3.5)

while page < 22:
    listing = driver.find_elements(By.CSS_SELECTOR,'div.col-lg-3.col-md-3.col-6')
    for item in listing:
        names = item.find_element(By.CSS_SELECTOR,'a.cd.chp').text
        prices = item.find_element(By.CSS_SELECTOR,'span.money').text
        


        name.append(names)
        price.append(prices)

    df = pd.DataFrame({
        'Products Name':name,
        'Price':price
    })

    try:
        next_page = driver.find_element(By.LINK_TEXT,'Next')

        time.sleep(3.2)

        if next_page.is_displayed():
            next_page.click()
            page +=1
        else:
            break
    
    except NoSuchElementException:
        break

print(df)

df.to_csv('bites.csv', index=False)

time.sleep(5)

driver.quit()