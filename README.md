# Instagram Suspicious Followers Detection (2023)

This script helps you to identify suspicious followers on your Instagram account based on specific keywords present in their usernames. The purpose of this script is to help users detect and manage spam or fake accounts among their followers.

## Requirements

- Python 3
- Selenium
- Webdriver Manager

Install the required Python packages with the following command:
```python
pip install selenium webdriver-manager
```

## Usage

1. Replace the `username` and `password` variables in the script with your Instagram account credentials.
2. Adjust the number of scroll operations in the script depending on the number of followers you want to load.
3. Run the script with the following command:
```python
python suspicious_followers_detection.py
```
The script will log in to your Instagram account, load the specified number of followers, and identify suspicious followers based on the defined keywords. It will then save the suspicious followers' usernames and IDs to a file named `suspicious_followers.txt`.

## Suspicious Hastags:
    'spam', 'bot', 'fake', 'scam', 'contest', 'followforfollow', 'lfl', 'meme', 'spamsquishy', 'instagood', 'mood', 'dankmemes', 'memesdaily', 'share', 'followback', 'twitter', 'gaintrick', 'cute', 'slime', 'scammers', 'scammer', 'twitterquotes', 'scammersofinstagram', 'selfie', 'polishgirl', 'edits', 'scammeralert', 'relatable', 'likeforlikeback', 'spams', 'twittermemes', 'followtrain', 'views', 'spammers', 'dubaixd', 'dubaixxd', 'dubai', 'youlikehits', 'socialexchange', 'youhavewon', 'win', 'onlyfans', 'manyvid', 'f4f', 's4s', 'l4l', 'follow4follow', 'like4like', 'spamforspam', 'spam4spam', 'shoutout4shoutout', 'fakeaccount', 'fakefollowers', 'getfollowers', 'getlikes'

## Warnings

1. Use this script with caution. Excessive scrolling and loading a large number of followers may cause Instagram to flag your account as suspicious, potentially resulting in temporary or permanent restrictions.
2. Be mindful of the frequency of running this script to avoid potential issues with Instagram. Limit the usage of the script and monitor your account for any unusual activity.
3. The filtering of followers based on keywords may not always be accurate, as some legitimate users might also use the specified hashtags. It is essential to manually review the results before taking any action.

## Disclaimer

This script is for educational purposes and personal use only. The user is responsible for complying with Instagram's terms of service and any applicable laws. The author of this script is not responsible for any consequences resulting from the use or misuse of this script.

## Copyright
Volkan `Sah Kücükbudak
