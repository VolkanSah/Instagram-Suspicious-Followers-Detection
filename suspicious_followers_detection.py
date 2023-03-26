# Copyright Volkan Sah Kücükbudak
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Replace these values with your Instagram credentials
username = 'your_username'
password = 'your_password'

# Login to Instagram
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.instagram.com/')
time.sleep(2)

username_input = driver.find_element_by_name('username')
username_input.send_keys(username)
password_input = driver.find_element_by_name('password')
password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)

time.sleep(4)

# Go to profile
driver.get(f'https://www.instagram.com/{username}/')
time.sleep(2)

# Klick on button "Follower"
followers_button = driver.find_element_by_xpath('//a[contains(@href, "/followers/")]')
followers_button.click()
time.sleep(2)

# Scroll through the followers list to load more followers
for _ in range(15): # Anzahl der Scroll-Vorgänge anpassen, um mehr oder weniger Follower zu laden
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', driver.find_element_by_css_selector('div[role="dialog"] > div:nth-child(2)'))
    time.sleep(1)

# Get Follower-List
follower_elements = driver.find_elements_by_css_selector('div[role="dialog"] ul div li')

# # Identify suspicious followers
suspicious_keywords = ['spam', 'bot', 'fake', 'scam', 'contest', 'followforfollow', 'lfl', 'meme', 'spamsquishy', 'instagood', 'mood', 'dankmemes', 'memesdaily', 'share', 'followback', 'twitter', 'gaintrick', 'cute', 'slime', 'scammers', 'scammer', 'twitterquotes', 'scammersofinstagram', 'selfie', 'polishgirl', 'edits', 'scammeralert', 'relatable', 'likeforlikeback', 'spams', 'twittermemes', 'followtrain', 'views', 'spammers', 'dubaixd', 'dubaixxd', 'dubai', 'youlikehits', 'socialexchange', 'youhavewon', 'win', 'onlyfans', 'manyvid', 'f4f', 's4s', 'l4l', 'follow4follow', 'like4like', 'spamforspam', 'spam4spam', 'shoutout4shoutout', 'fakeaccount', 'fakefollowers', 'getfollowers', 'getlikes']
suspicious_followers = []
for elem in follower_elements:
    user_link = elem.find_element_by_css_selector('a').get_attribute('href')
    username = user_link.split('/')[-2]
    if any(keyword in username.lower() for keyword in suspicious_keywords):
        user_id = user_link.split('/')[-3]
        suspicious_followers.append((username, user_id))

# Save the suspicious followers (username and ID) to a file
with open('suspicious_followers.txt', 'w') as f:
    for follower in suspicious_followers:
        f.write(f'{follower[0]} ({follower[1]})\n')

driver.quit()
