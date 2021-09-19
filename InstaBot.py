from random import random
from myigbot import MyIGBot
from datetime import datetime
from time import sleep
import requests
import urllib.request
import random

class InstaBot:

    def __init__(self, username, password):
        proxies = {}
        self.API_URL = "https://api.nasa.gov/planetary/apod?api_key=dDCSS2m4IyfoDeNw9ODgFz8e8sUrEJfxJkDekWOr"
        self.username = username
        self.password = password
        self.bot = MyIGBot(username, password)

    def follow_people(self):
        accounts_list = ['nasa', 'nasa_es', 'spacex', 'iss']
        count = self.bot.user_followers_count(self.username)
        my_followers = self.bot.user_followers(self.username, limit=count)

        for account in accounts_list:
            user_followers = self.bot.user_followers(account, limit=20)
            for user_follower in user_followers:
                self.bot.follow(user_follower)
                print('[+] Siguiendo a: @{}'.format(user_follower))
                sleep(random.uniform(60, 600))
                        
    
    def post_image(self):
        new_date = datetime.date
        old_date = 0
        
        req = requests.get(url = self.API_URL)
        data = req.json()

        img_url = data['hdurl']
        urllib.request.urlretrieve(img_url, "imageToPost.png")

        if new_date is not old_date :
            self.bot.upload_post(
                "imageToPost.png",
                caption = '{} ( {} )\n{}'.format(
                    data['title'], 
                    data['date'], 
                    data['explanation']
                )
            )
            old_date = new_date
            print('[+] Post image')