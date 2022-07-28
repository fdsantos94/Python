#!pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
#navegador.get("https://www.google.com.br/")
#navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dolar')

navegador.get("https://github.com/")
navegador.find_element(By.XPATH,'/html/body/div[1]/header/div/div[2]/div[2]/div[2]/a').click()
navegador.find_element(By.XPATH,'//*[@id="login_field"]').send_keys('fdsantos94')
navegador.find_element(By.XPATH,'//*[@id="password"]').send_keys('Jbqwelax22')
navegador.find_element(By.XPATH,'//*[@id="login"]/div[4]/form/div/input[12]').click()
navegador.find_element(By.XPATH,'/html/body/div[1]/header/div[7]/details/summary/img').click()
navegador.find_element(By.XPATH,'/html/body/div[1]/header/div[7]/details/details-menu/div[1]/a').click()

#/html/body/div[1]/header/div[7]/details/details-menu/a[1]
#/html/body/div[1]/header/div[7]/details/details-menu/div[1]/a/strong
#/html/body/div[1]/header/div[7]/details/details-menu/a[1]
#/html/body/div[1]/header/div[7]/details/details-menu/div[1]/a