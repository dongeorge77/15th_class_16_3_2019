from selenium import webdriver
import requests

driver=webdriver.Chrome()
driver.get("http://google.com")
driver.maximize_window()

element=driver.find_elements_by_tag_name("a")
print(len(element))
print(type(element))

broken_link=[]
correct_link=[]

for i in element:
    if(requests.head(i.get_attribute("href")) !=200):
        broken_link.append(i.get_attribute("href"))

    else:
        correct_link.append(i.get_attribute("href"))

print("Broken Link: ",broken_link)
print("Correct Link: ",correct_link)