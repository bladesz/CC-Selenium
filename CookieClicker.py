from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color
from localstorage import LocalStorage
import time

def execute(element, driver):
	purchase_item = ActionChains(driver)\
					.move_to_element(element)\
					.click()\
					.perform()
	return

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

try:
	with open('cookie.txt', 'r') as f:
		contents = f.readlines()
		for i in contents:
			driver.add_cookie(eval(i))
	print("cookies loaded")
	f.close()

	with open('localstorage.txt', 'r') as f:
		contents = f.readlines()
		l = LocalStorage(driver)
		for i in contents:
			entry = tuple(i.strip().split(', '))
			print(entry)
			l[entry[0]] = entry[1]
	print("localstorage loaded")
	f.close()

	driver.refresh()
except:
	print(contents)
	print("no previous cookies")


time.sleep(10)

driver.implicitly_wait(1)

''' Load function for exports
save_file = open('exported save.txt', "r")
contents = save_file.read()
save_file.close()


webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("o").key_up(Keys.CONTROL).perform()
text = driver.find_element(By.XPATH,"//textarea[@id = 'textareaPrompt']")
text.send_keys(contents)
text2 = driver.find_element(By.XPATH,"//textarea[@id = 'textareaPrompt']")
text2.send_keys(contents)
'''

try:
	load = driver.find_element(By.LINK_TEXT,"Load")
	execute(load, driver)
except:
	pass


time.sleep(10)




driver.implicitly_wait(0)
repeat = 100000000
while repeat > 1:

	if repeat % 5000 == 0:
		print("saved")
		webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("s").key_up(Keys.CONTROL).perform()
		with open('cookie.txt', 'w') as f:
			for i in driver.get_cookies():
				print(i, file=f)
		f.close()
		with open('localstorage.txt', 'w') as f:
			storage = (LocalStorage(driver).items())
			for key, value in storage.items():
				print("%s, %s" % (key,value), file=f)
		f.close()


	try:
			shimmers = driver.find_element(By.XPATH,"//div[@class='shimmer'][last()]")
			execute(shimmers, driver)
			print(repeat)

	except:
		pass

	try:
		purchaseable = driver.find_element(By.XPATH,"//div[@class='product unlocked enabled'][last()]")
		
		try:
			purchaseable_upgrade = driver.find_element(By.XPATH,"//div[@class='crate upgrade enabled'][last()]")
			execute(purchaseable_upgrade, driver)
		except:
			pass

		try:
			festive = driver.find_element(By.XPATH,"//div[@class='optionBox']/a/div/div")
			if Color.from_string(festive.value_of_css_property("color")) != "rgba(204, 204, 204, 1)":
				execute(festive, driver)
		except:
			try:
				seasonal = driver.find_element(By.XPATH,"//div[@id='versionNumber']")
				open_seasonal = ActionChains(driver)\
				.move_to_element_with_offset(seasonal,0,-20)\
				.click()\
				.perform()
			except:
				print("F Didn't load in time")
		execute(purchaseable, driver)

	except:
		pass


	#cps
	repeat -= 1

print("done")
'''
<div onclick="Game.UpgradesById[152].click(event);" class="crate upgrade enabled" onmouseout="Game.setOnCrate(0);Game.tooltip.shouldHide=1;" onmouseover="if (!Game.mouseDown) {Game.setOnCrate(this);Game.tooltip.dynamic=1;Game.tooltip.draw(this,function(){return function(){return Game.crateTooltip(Game.UpgradesById[152],'store');}();},'store');Game.tooltip.wobble();}" id="upgrade0" style="background-position:-912px -432px;"></div>
'''