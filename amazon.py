from selenium import webdriver

driver= webdriver.Chrome(r"C:\Users\gkush\Downloads\chromedriver.exe")

driver.get("https://www.amazon.in/mobile-phones/b/?ie=UTF8&node=1389401031&ref_=nav_cs_mobiles")

links=driver.find_elements_by_xpath("//a[@class='a-link-normal']")
for link in links:
	print(link.get_attribute('href'))