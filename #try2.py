#try2.py
from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import  time
from time import sleep
import pandas as pd

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

for x in range(1,7):
	print(x)

	driver.get("https://www.sodimac.cl/sodimac-cl/category/scat922339/Ceramicas?currentpage="+ str(x))
	print(driver.title)

	Ceramicas = driver.find_elements_by_xpath('//div[@itemprop="offers"]')

	Ceramicas_list = []

	for Ceramicas in Ceramicas:

		precio = Ceramicas.find_elements_by_xpath('.//span[@class="jsx-4135487716"]')[1].text
		descripcion = Ceramicas.find_elements_by_xpath('.//h2[@class="jsx-411745769 product-title"]')[0].text
		marca = Ceramicas.find_elements_by_xpath('.//div[@class="jsx-411745769 product-brand"]')[0].text
		info_item = {
				'precio': precio,
				'descripcion': descripcion,
				'marca': marca
		}	

		Ceramicas_list.append(info_item)
	
	time.sleep(2)	
	df = pd.DataFrame(Ceramicas_list)
	print(df)
	
	df.to_csv('Ceramicas_list.csv')
	