from selenium import webdriver
import requests

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://google.com")
ele = driver.find_elements_by_tag_name("a")
print(type(ele))
el1=[]
el2=[]
for i in ele:
    r = requests.head(i.get_attribute("href"))
    if r.status_code !=200:
        el1.append(i.get_attribute("href"))
    else:
        el2.append(i.get_attribute("href"))
print("BROKEN LINK: ",el1)
print(("CORRECT LINK: ",el2))