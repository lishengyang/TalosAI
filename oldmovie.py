from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


# Set up the Selenium driver (in this case, using Firefox)
driver = webdriver.Firefox()

# Navigate to the IMDb top 250 movies page
driver.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')

# Find the table of top movies on the page
table = driver.find_element_by_xpath('//*[@id="main"]/div/span/div/div/div[3]/table')

# Extract the links to each movie's page
links = [row.find_element_by_tag_name('a').get_attribute('href') for row in table.find_elements_by_xpath('.//tr')]

# Print the links
for link in links:
    print(link)

# Quit the driver
driver.quit()

