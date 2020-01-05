# pyhentai

Python Module for Downloading Nhentai Doujin


>IF THIS APPLICATION ALWAYS RETURNING AN ERROR CONTINOUSLY KINDLY CHECK :
>http://nhproxy.glitch.me and
>https://nhent.ai
>AS THIS FAR, WE DOES NOT USE ANY VPN / PROXIES EMBEDDED IN THIS APP SO NEED THOSE WEBSITE RUNNING
>VPN/PROXIES FEATURE MAY BE INTRODUCED IN THE FUTURE UPDATE AND WE'LL USE https://nhentai.net INSTEAD 
>THANK YOU

example of use :
=====================
```python
import nhentai
code = input("Insert Code Here:")
response = index.get(code)
```

"response" will return data like this:

```python
nh_media_id = response['media_id'] #getting media id
nh_id = response['id'] #getting book id
nh_title_eng = response['title']['english'] #getting name of doujin on english version
```
if you want to download it use this function

```python
index.download(response)
```
