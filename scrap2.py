from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to the Firefox driver executable
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to the Firefox driver executable
driver_path = "/usr/local/bin/geckodriver"

# Create a new Firefox web driver instance
driver = webdriver.Firefox(executable_path=driver_path)

# Navigate to the IMDb top 250 movies list page
driver.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")

# Wait for the page to load
time.sleep(5)

# Find all the movie titles on the page
movie_titles = driver.find_elements_by_xpath("//td[@class='titleColumn']/a")

# Print out the movie titles
for title in movie_titles:
    print(title.text)

# Close the web driver instance
driver.quit()


