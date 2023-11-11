import datetime
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

#Fix
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# set options to be headless, ..
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pandas as pd 
from bs4 import BeautifulSoup
options = Options()

# Adding argument to disable the AutomationControlled flag 
options.add_argument("--disable-blink-features=AutomationControlled") 
 
# Exclude the collection of enable-automation switches 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
 
# Turn-off userAutomationExtension 
options.add_experimental_option("useAutomationExtension", False) 

options.add_argument('--ignore-certificate-errors')

# open it, go to a website, and get results
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#wd.get(input("Enter your bigc url : "))


url = "https://airlinehistory.co.uk/location/albania/"
driver.get(url)

filename = "testx.xlsx"


soup = BeautifulSoup(driver.page_source,'html.parser')
#print(driver.page_source)
url_lis = []

c = 1
for item in soup.find_all('option'): 
    

        link = "https://airlinehistory.co.uk/airline/"+item['value']
        #print(item['value'])
        print(link)
        url_lis.append(link)


url_lis = url_lis[1:]


note_lis = []
title_lis = []
status_lis = []
op_lis = []
code_lis = []
country_lis = []
reg_lis = []
update_lis = []

for i in url_lis:

    
        driver.get(i)
        
        try:
                note = driver.find_element(By.XPATH,'//*[@id="ah-single-airline-wrapper"]/div[1]/div[5]').text 
                print(note)
                note_lis.append(note)
        except: 
                note_lis.append(" ")
        
        try:
                title = driver.find_element(By.CSS_SELECTOR,'.entry-title').text 
                print(title)
                title_lis.append(title)
        except: 
                title_lis.append(" ")
                
        try:
                status = driver.find_element(By.XPATH,'//*[@id="ah-single-airline-wrapper"]/div[1]/div[2]/div[1]/span[2]').text 
                print(status)
                status_lis.append(status)
        except: 
                status_lis.append(" ")


        try:
                operating_date = driver.find_element(By.XPATH,'//*[@id="ah-single-airline-wrapper"]/div[1]/div[2]/div[2]').text 
                print(operating_date)
                op_lis.append(operating_date)
        
        except: 
                op_lis.append(" ")
        
        try:

                code = driver.find_element(By.XPATH,'//*[@id="ah-single-airline-wrapper"]/div[1]/div[2]/div[3]').text 
                print(code)
                code_lis.append(code)
        except:
                code_lis.append(code)
        
        try:

                country = driver.find_element(By.XPATH,'//*[@id="ah-single-airline-wrapper"]/div[1]/div[2]/div[4]/a').text 
                print(country)
                country_lis.append(country)
        except: 
                country_lis.append(country)

        try:
                reg = driver.find_element(By.XPATH,'//*[@id="ah-single-airline-wrapper"]/div[1]/div[2]/div[5]/a').text 
                print(reg)
                reg_lis.append(reg)
        
        except: 
                reg_lis.append(" ")

        try:

     

                # Use the adjacent sibling combinator '+' to select the next <span> element
                update = driver.find_element(By.XPATH,'//*[@id="ah-single-airline-wrapper"]/div[1]/div[5]/div[1]/div/span[2]').text
                print(update)
                update_lis.append(update)
        except: 
                update_lis.append(update)

df = pd.DataFrame()
df['Title'] = title_lis 
df['Country'] = country_lis 
df['Status'] = status_lis 
df['Code'] = code_lis 
df['Operating Date'] = op_lis
df['Register'] = reg_lis 
df['Note'] = note_lis
df['Update'] = update_lis 
df['URL'] = url_lis

    
df.to_excel(filename)
    





print("Hello : ",url_lis[0])




df = pd.DataFrame()


