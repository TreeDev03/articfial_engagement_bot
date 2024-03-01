import time


from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


chrome_options = Options()

nameCoin = "Mini SORA"
   # input("Enter the coin token of your choice: "))

chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")


driver = webdriver.Chrome(options=chrome_options)



action = ActionChains(driver)
driver.get("https://cntoken.io/coins")

time.sleep(1)


driver.execute_script("window.scrollBy(0, 2000);")




time.sleep(1)


# Search for Coin
search = driver.find_element(By.XPATH, """/html/body/div[1]/div/div[2]/div[1]/div/div[4]/div[1]/div[2]/div[1]/input""")


time.sleep(2)
search.click()
search.send_keys(nameCoin)
time.sleep(1)
search.send_keys(Keys.RETURN)

time.sleep(3)

# UpVote
info = driver.find_element(By.XPATH, """//*[@id="app"]/div/div[2]/div[1]/div/div[4]/div[2]/div[3]/table/tbody/tr[1]/td[1]/div/div""")
info.click()


time.sleep(1)


driver.execute_script("window.scrollBy(0, -25);")


vote = driver.find_element(By.XPATH, """//*[@id="app"]/div/div[2]/div[1]/div/div[3]/div[2]/button/span""")
vote.click()







time.sleep(60)








