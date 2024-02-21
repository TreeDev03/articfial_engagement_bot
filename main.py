import time


from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


chrome_options = Options()
nameCoin = "OpSec"
   # input("Enter the coin token of your choice: "))
driver = webdriver.Chrome(options=chrome_options)




action = ActionChains(driver)
driver.get("https://cntoken.io/coins")
driver.maximize_window()
time.sleep(1)


driver.execute_script("window.scrollBy(0, 2000);")




time.sleep(1)


# Search for Coin
search = driver.find_element(By.XPATH, """/html/body/div[1]/div/div[2]/div[1]/div/div[4]/div[1]/div[2]/div[1]/input""")


time.sleep(1)
search.click()
search.send_keys(nameCoin)
time.sleep(1)
search.send_keys(Keys.RETURN)





time.sleep(60)
