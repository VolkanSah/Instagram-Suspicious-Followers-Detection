# Instagram Suspicious Followers Detection- Copyright Volkan Kücükbudak
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

username = 'your_username'
password = 'your_password'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.instagram.com/')
time.sleep(2)

username_input = driver.find_element_by_name('username')
username_input.send_keys(username)
password_input = driver.find_element_by_name('password')
password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)

time.sleep(4)

driver.get(f'https://www.instagram.com/{username}/')
time.sleep(2)

followers_button = driver.find_element_by_xpath('//a[contains(@href, "/followers/")]')
followers_button.click()
time.sleep(2)

for _ in range(20):
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', driver.find_element_by_css_selector('div[role="dialog"] > div:nth-child(2)'))
    time.sleep(1)

follower_elements = driver.find_elements_by_css_selector('div[role="dialog"] ul div li')

suspicious_keywords = ['spam', 'bot', 'fake', 'scam', 'contest', 'followforfollow', 'lfl', 'meme', 'spamsquishy', 'instagood', 'mood', 'dankmemes', 'memesdaily', 'share', 'followback', 'twitter', 'gaintrick', 'cute', 'slime', 'scammers', 'scammer', 'twitterquotes', 'scammersofinstagram', 'selfie', 'polishgirl', 'edits', 'scammeralert', 'relatable', 'likeforlikeback', 'spams', 'twittermemes', 'followtrain', 'views', 'spammers', 'dubaixd', 'dubaixxd', 'dubai', 'youlikehits', 'socialexchange', 'youhavewon', 'win', 'onlyfans', 'manyvid', 'f4f', 's4s', 'l4l', 'follow4follow', 'like4like', 'spamforspam', 'spam4spam', 'shoutout4shoutout', 'fakeaccount', 'fakefollowers', 'getfollowers', 'getlikes']

suspicious_followers = []

for elem in follower_elements:
    user_link = elem.find_element_by_css_selector('a').get_attribute('href')
    username = user_link.split('/')[-2]
    
    # Navigate to the user's profile
    driver.get(user_link)
    time.sleep(2)

    # Get the user's bio
    try:
        bio_element = driver.find_element_by_css_selector('div.-vDIg > span')
        bio = bio_element.text
    except:
        bio = ""

    # Check for suspicious keywords in the username and bio
    if any(keyword in username.lower() for keyword in suspicious_keywords) or any(keyword in bio.lower() for keyword in suspicious_keywords):
        user_id = user_link.split('/')[-3]
        suspicious_followers.append((username, user_id))

    # Navigate back to your profile
    driver.get(f'https://www.instagram.com/{username}/')
    time.sleep(2)
    followers_button = driver.find_element_by_xpath('//a[contains(@href, "/followers/")]')
    followers_button.click()
    time.sleep(2)

with open('suspicious_followers.txt', 'w') as f:
    for follower in suspicious_followers:
        f.write(f'{follower[0]} ({follower[1]})\n')

driver.quit()
