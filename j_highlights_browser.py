from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import sys
import time
from yt_dlp import YoutubeDL
import re

TIME_TO_WAIT = 0.1
TIME_TO_WAIT_LONG = 3
TIME_TO_WAIT_WATCH_MOVIE = 200

driver = webdriver.Chrome()

url = "https://www.youtube.com/@jleaguehighlightschannel/videos"
driver.get(url)
time.sleep(TIME_TO_WAIT)

zenkaku = {1: '１', 2: '２', 3: '３', 4: '４', 5: '５', 6: '６', 7: '７', 8: '８', 9: '９'}

argv1 = int(sys.argv[1])
category = zenkaku[argv1]

links = driver.find_elements(By.ID, "video-title-link")

if len(sys.argv) > 2:
    argv2 = int(sys.argv[2])
    if (argv2 in zenkaku.keys()):
        matchday = zenkaku[argv2]
    else:
        matchday = argv2
else:
    for link in links:
        try:
            link_text = link.text
            if "Ｊ" + category + "リーグ" in link_text:
                matchday = re.search(r'第([0-9０-９]+)節', link_text).group(1)
                break
        except:
            pass

links_to_watch = []
for link in links:
    try:
        link_text = link.text
        if "Ｊ" + category + "リーグ" in link_text and "第" + str(matchday) + "節" in link_text:
            links_to_watch.append(link.get_attribute("href"))
    except:
        pass

for link in links_to_watch:
    driver.get(link)
    time.sleep(TIME_TO_WAIT_WATCH_MOVIE)