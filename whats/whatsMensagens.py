from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging
import time
import sys

class Whats:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=options)

    def send(self, message, groups):
        try:
            for group in groups:
                campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='{group}']")
                time.sleep(3)
                campo_grupo.click()
                chat_box = self.driver.find_element_by_xpath("//div[@class='_2S1VP copyable-text selectable-text' and @data-tab='1']")
                time.sleep(3)
                chat_box.click()
                chat_box.send_keys(message)
                botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                time.sleep(3)
                botao_enviar.click()
                time.sleep(5)
                logging.info('WhatsApp Message sended to '+group)
                return True
        except:

            logging.info('WhatsApp Message Fail to '+group)
            logging.info("Unexpected Error: "+str(sys.exc_info()[0]))

            return False
    def open(self):
        self.driver.get('https://web.whatsapp.com')
        logging.info('WhatsApp opens')
        time.sleep(5)
        logado = False
        while not logado:
            try:
                campo_intrucao = self.driver.find_element_by_xpath("//div[@class='landing-title xZ93f']")
                logging.info("Not Loged")
            except:
                logging.info("Loged")
                logado = True
            time.sleep(3)

    def close(self):
        self.driver.close()



