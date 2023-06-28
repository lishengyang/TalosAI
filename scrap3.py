from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to the Firefox driver executable
driver_path = "/usr/local/bin/geckodriver"

# Create a new Firefox web driver instance
driver = webdriver.Firefox(executable_path=driver_path)

# Navigate to the IMDb top 250 movies list page
driver.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")

# Wait for the title to appear before proceeding
title_present = EC.presence_of_element_located((By.TAG_NAME, "title"))
WebDriverWait(driver, 10).until(title_present)

# Wait for the movie titles to appear before scraping them
movie_titles_present = EC.presence_of_all_elements_located((By.XPATH, "//td[@class='titleColumn']/a"))
WebDriverWait(driver, 10).until(movie_titles_present)

# Find all the movie titles on the page
movie_titles = driver.find_elements_by_xpath("//td[@class='titleColumn']/a")

# Print out the movie titles
for title in movie_titles:
    print(title.text)

# Close the web driver instance
driver.quit()

