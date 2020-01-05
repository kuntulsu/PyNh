# pyhentai

Python Module for Downloading Nhentai Doujin

"""
IF THIS APPLICATION ALWAYS RETURNING AN ERROR CONTINOUSLY KINDLY CHECK :
http://nhproxy.glitch.me and
https://nhent.ai
AS THIS FAR, WE DOES NOT USE ANY VPN / PROXIES EMBEDDED IN THIS APP SO NEED THOSE WEBSITE RUNNING
VPN/PROXIES FEATURE MAY BE INTRODUCED IN THE FUTURE UPDATE AND WE'LL USE https://nhentai.net INSTEAD 
THANK YOU

example of use :
====================

import nhentai
code = input("Insert Code Here:")
response = index.get(code)
index.download(response)

#once you didnt get any error after this , youre able to get data like this:

nh_media_id = response['media_id'] #getting media id
nh_id = response['id'] #getting book id
nh_title_eng = response['title']['english'] #getting name of doujin on english version
