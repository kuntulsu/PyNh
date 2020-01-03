#! /usr/bin/python3
import json
import requests
from urllib.request import urlopen, Request
import urllib.request
import os

os.system("cls" if os.name == 'nt' else 'clear')
#printing main app
print("nhentai downloader (under development)")
print("Find your doujin in nhentai.net!")
print("***********************************")
print("In This Version you dont need vpn to download doujin , many thanks to nhproxy.glitch.me and nhent.ai for providing api and links")
print("***********************************")
print("input nuke code below!")
print("sst..! 177013 is my recommendation, check it out!")


def inputNumber():
	while True:
		try:
			userinput = int(input("Input The Nuke Code (Code must be numbers): "))  
		except ValueError:
			print("The Code must be numbers! Try again.")
			continue
		else:
			return userinput 
			break 

userinput = inputNumber()
userinput = str(userinput)
print("Connecting to https://nhentai.net ...")
print("Collecting Information",userinput,"...")
book_id = userinput
# getting information about link submitted
link = "https://nhproxy.glitch.me/api/gallery/"+book_id
try:
	response = json.loads(requests.get(link).text)
except requests.exceptions.ConnectionError:
	os.system('cls' if os.name=='nt' else 'clear')
	print("An Error Occured during connecting to the nhentai.net, maybe your internet went down , or nhentai was blocked by your country")
	print("Exiting.")
	quit()
if "error" in response:
	os.system('cls' if os.name=='nt' else 'clear')
	print("404 Not Found")
	quit()

media_id = response["media_id"]
title = response["title"]["english"]

links = len(response["images"]["pages"])
os.system('cls' if os.name=='nt' else 'clear')
#Showing the information about the book
print("***********************************")
print("Title : ",title)
print("Pages : ",links)
print("***********************************")
print("Your Files is Ready to Download  Press Y to Continue or N to Abort!")
decision = input()
if decision == "Y" or decision == "y":
	pass
else:
	print("Abort.")
	quit()

# main action
	#getcwd for pathing material.
cwd = os.getcwd()
try:
	folder = os.mkdir(str(response["id"]))
	print("Folder Created in : "+ str(cwd)+"/"+str(response["id"]))
except:
	folder = response["id"]
	print("Folder Already Created in : "+ str(cwd)+"/"+str(folder))
	print("Continue...")
fullpath = str(cwd)+"/"+str(response["id"])

start = 1
end = links + 1
print("Downloading...")

for x in range(start,end):
	percent = int(x/links* 100)
	download_link = "https://cdn.nhent.ai/galleries/"+str(media_id)+"/"+str(x)+".jpg"
	opener = urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	urllib.request.install_opener(opener)
	urllib.request.urlretrieve(download_link, fullpath+"/"+str(x)+".jpg")
	print(download_link,"[",x,"/",links,"](",percent,"%)")
#end of main action
print("Done, you can find your downloaded doujin in"+fullpath)
