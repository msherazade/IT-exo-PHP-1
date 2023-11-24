from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

chromedriver_path = r"T:\DRIVER\msedgedriver.exe"

driver = webdriver.Edge()



driver.get("http://localhost/php1/IT-exo-PHP/projet/form.php")
time.sleep(2)

driver.find_element(By.ID, "firstName").send_keys("moi" )
time.sleep(2)

                         
driver.find_element(By.ID, "lastName").send_keys("sherazade" )
time.sleep(2)                        



driver.find_element(By.ID, "username").send_keys("helloa" )
time.sleep(2)  


driver.find_element(By.ID, "email").send_keys("") 
time.sleep(2) 

driver.find_element(By.ID, "address").send_keys("fkhrtkiury") 
time.sleep(2) 

driver.find_element(By.ID, "address2").send_keys("") 
time.sleep(2) 



driver.find_element(By.ID, "country").click()
time.sleep(2)




