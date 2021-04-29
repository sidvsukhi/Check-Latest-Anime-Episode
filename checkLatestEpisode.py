from selenium import webdriver
import time

try:
	driver = webdriver.Chrome("/home/asus/Siddhant/bot/chromedriver")
	animeName = 'boku no hero academia 5th season'

	driver.set_page_load_timeout(5)
	driver.get("https://www1.gogoanime.ai/")
	print('Website opened!')
	time.sleep(3)
	driver.maximize_window()

	searchText = driver.find_element_by_css_selector('#keyword')
	searchText.send_keys(animeName)
	print('Entered search text')
	time.sleep(2)
	driver.find_element_by_css_selector('#search-form div.row input.btngui').click()
	print('Searching!')
	time.sleep(2)
	driver.find_element_by_css_selector('#wrapper_bg section section.content_left div div.last_episodes ul li:nth-child(1) div').click()
	print("Opening Anime!")
	time.sleep(2)
	episodeCount = driver.find_element_by_css_selector('#episode_page li a').text
	print('Present available episodes are: {}'.format(episodeCount))
	driver.close()
	print('Job done successfully!')
except Exception as ex:
	print('Caught exception {}'.format(ex))