from selenium import webdriver
import pandas as pd
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url ='https://www.lotuss.com.my/en/category/beverages?sort=price:ASC'

name =[]
price =[]
max_scroll=100
scroll_count=0
prev_height=-1

driver = webdriver.Chrome()

driver.get(url)
time.sleep(5)
driver.maximize_window()
time.sleep(5)

while scroll_count < max_scroll:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == prev_height:
        break
    prev_height =new_height
    scroll_count +=1

time.sleep(5)

listing = driver.find_elements(By.CLASS_NAME,'product-grid-item')

for item in listing:
    names = item.find_element(By.ID,'product-title').text
    prices = item.find_element(By.CLASS_NAME,'sc-kHxTfl').text

    name.append(names)
    price.append(prices)

    df = pd.DataFrame({
        'Products Name':name,
        'Price in RM':price
    })

print(df)

df.to_csv('lotus.csv', index=False)

driver.quit()