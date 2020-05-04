from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys


options = webdriver.ChromeOptions()
options.add_argument('lang=pt-br')
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=options)
time.sleep(5)

driver.get('https://web.whatsapp.com')

time.sleep(20)

find_box = driver.find_element_by_xpath("//div[@class='_2S1VP copyable-text selectable-text' and @data-tab='3']")
time.sleep(3)
find_box.click()
find_box.send_keys("Angelica")
time.sleep(3)

campo_grupo = driver.find_element_by_xpath(f"//span[@title='Angelica']")
time.sleep(3)
campo_grupo.click()
chat_box = driver.find_element_by_xpath("//div[@class='_2S1VP copyable-text selectable-text' and @data-tab='1']")
time.sleep(3)
chat_box.click()
chat_box.send_keys("message")
botao_enviar = driver.find_element_by_xpath("//span[@data-icon='send']")
time.sleep(3)
botao_enviar.click()
time.sleep(5)