from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time

keyword = "제로웨이스트"
url = 'https://www.youtube.com/results?search_query={}'.format(keyword)

driver = webdriver.Chrome('/Users/jinameliachoi/Documents/chromedriver')
driver.get(url)
soup = bs(driver.page_source, 'html.parser')
last_page_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(3.0)
    new_page_height = driver.execute_script("return document.documentElement.scrollHeight")

    if new_page_height == last_page_height:
        break

    last_page_height = new_page_height

html_source = driver.page_source
driver.quit()
soup = bs(html_source, 'lxml')

name = soup.select('a#video-title')
video_url = soup.select('a#video-title')
view = soup.select('a#video-title')

name_list = []
url_list = []
view_list = []

for i in range(len(name)):
    name_list.append(name[i].text.strip())
    view_list.append(view[i].get('aria-label').split()[-1])
for i in video_url:
    url_list.append('{}{}'.format('https://www.youtube.com', i.get('href')))

youtubeDic = {
    '제목': name_list,
    '주소': url_list,
    '조회수': view_list
}

youtubeDf = pd.DataFrame(youtubeDic)

youtubeDf.to_csv('zero_waste_youtube.csv', encoding='', index=False)