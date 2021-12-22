from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color
import time

service = Service("C:\Program Files (x86)\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(10)
driver.implicitly_wait(5)

webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("o").perform()
save_file = open('exported save.txt', "r")
contents = save_file.read()
save_file.close()

text = driver.find_element(By.XPATH,"//textarea[@id = 'textareaPrompt']")
text_e= ActionChains(driver)
text_e.move_to_element(text)
text_e.click()
text_e.perform()
webdriver.ActionChains(driver).send_keys(contents).perform()

'''
try:
	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID, "cookies"))
	)

except:
	driver.quit()
'''
driver.implicitly_wait(0)
repeat = 100000000
while repeat > 1:
	purchaseable = driver.find_elements(By.XPATH,"//div[@class='product unlocked enabled']")
	for i in purchaseable[::-1]:
		try:
			purchase_item = ActionChains(driver)
			purchase_item.move_to_element(i)
			purchase_item.click()
			purchase_item.perform()

		except:
			time.sleep(1)
			pass

	purchaseable_upgrades = driver.find_elements(By.XPATH,"//div[@class='crate upgrade enabled']")
	for j in purchaseable_upgrades[::-1]:
		try:
			purchase_upgrade = ActionChains(driver)
			purchase_upgrade.move_to_element(j)
			purchase_upgrade.click()
			purchase_upgrade.perform()
		except:
			time.sleep(1)
			pass

	shimmers = driver.find_elements(By.XPATH,"//div[@class='shimmer']")
	for k in shimmers[::-1]:
		try:
			shimmers = ActionChains(driver)
			shimmers.move_to_element(k)
			shimmers.click()
			shimmers.perform()
		except:
			pass
	#cps
	repeat -= 1

print("done")
'''
<div onclick="Game.UpgradesById[152].click(event);" class="crate upgrade enabled" onmouseout="Game.setOnCrate(0);Game.tooltip.shouldHide=1;" onmouseover="if (!Game.mouseDown) {Game.setOnCrate(this);Game.tooltip.dynamic=1;Game.tooltip.draw(this,function(){return function(){return Game.crateTooltip(Game.UpgradesById[152],'store');}();},'store');Game.tooltip.wobble();}" id="upgrade0" style="background-position:-912px -432px;"></div>
'''