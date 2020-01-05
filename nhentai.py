#! /usr/bin/python3
import json
import requests
from urllib.request import urlopen, Request
import urllib.request
import os


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
#once you didnt get any error after this , youre able to get data like this:

nh_media_id = response['media_id'] #getting media id
nh_id = response['id'] #getting book id
nh_title_eng = response['title']['english'] #getting name of doujin on english version
nh_title_jp = response['title']['japanese'] #getting name of doujin on japanese (if exist)
=========================================
"""
class Error(Exception):
	pass
class Error404(Error):
	pass

api_link = "http://nhproxy.glitch.me/api/gallery/" 
page_link = "https://cdn.nhent.ai/galleries/"

default_download_path = str(os.getenv("HOME"))+"/Downloads/"
try:
	os.mkdir(default_download_path+"nhentai")
	default_download_path = str(os.getenv("HOME"))+"/Downloads/nhentai/"
except FileExistsError:
	default_download_path = str(os.getenv("HOME"))+"/Downloads/nhentai/"


def get(code = ""): #getting stuff like doujin name,page count , or error
	code = int(code)
	if not isinstance(code, int):
		raise ValueError("Code Must be Numbers")
	code  = str(code)
	if len(code) > 0 :
		#main code must be executed
		try:
			response = json.loads(requests.get(api_link+code).text)
			if "error" in response:
				raise Error404("The Code You Entered ... Seems cannot be found (404)")
			else:
				return response
		except requests.exceptions.ConnectionError:
			raise requests.exceptions.ConnectionError("Error Connecting to: "+api_link+str(code))
def download(response):
	links = len(response["images"]["pages"])
	end = links + 1
	start = 1

	#excepting for existing downloadable book and been resumed
	if os.path.isdir(os.path.join(default_download_path+str(response['id']))):
		num_files = len([f for f in os.listdir(default_download_path+str(response["id"]) )if os.path.isfile(os.path.join(default_download_path+str(response["id"]) , f))])
		if num_files > 0 :
			start = num_files
			os.unlink(default_download_path+str(response["id"])+"/"+str(num_files)+".jpg")
		else:
			pass
		try:
			for x in range(start,end):
				percent = int(x/links* 100)
				download_link = page_link+str(response["media_id"])+"/"+str(x)+".jpg"
				opener = urllib.request.build_opener()
				opener.addheaders = [('User-agent', 'Mozilla/5.0')]
				urllib.request.install_opener(opener)
				urllib.request.urlretrieve(download_link, default_download_path+"/"+str(response["id"])+"/"+str(x)+".jpg")
				print(download_link,"["+str(x)+"/"+str(links)+"]("+str(percent)+"%)")
		except ConnectionResetError:
			download(response)
	else:
		#start new download
		try:
			for x in range(start,end):
				percent = int(x/links* 100)
				download_link = page_link+str(response["media_id"])+"/"+str(x)+".jpg"
				opener = urllib.request.build_opener()
				opener.addheaders = [('User-agent', 'Mozilla/5.0')]
				urllib.request.install_opener(opener)
				urllib.request.urlretrieve(download_link, default_download_path+"/"+str(response["id"])+"/"+str(x)+".jpg")
				print(download_link,"["+str(x)+"/"+str(links)+"]("+str(percent)+"%)")
		except ConnectionResetError:
			#resume() in the future
			pass
