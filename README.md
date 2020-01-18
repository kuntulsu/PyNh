# pyhentai

Python Module for Downloading Nhentai Doujin

>If this application always returning an error continously kindly check:
>http://nhproxy.glitch.me and
>https://nhent.ai
>as this far, we does not use any VPN/Proxies embedded in this app, so we need those website running,
>VPN/Proxies feature may be introduced in the future update and we will use https://nhentai.net instead


## example of use :
```python
#!/usr/bin/python3
#python3 and linux is required to run this program

import nhentai
code = input("Insert Code Here:")
response = index.get(code)

#if you want to download it use this function
nhentai.download(response)
```

"response" will return data like this:

```python
response['media_id'] #getting media id
response['id'] #getting book id
response['title']['english'] #getting name of doujin on english version
```

