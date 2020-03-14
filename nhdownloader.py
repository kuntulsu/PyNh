import requests
import sys
import json
from pathlib import Path
import os
import urllib
from colorama import Fore
from colorama import Style
#import signal

if len(sys.argv) <= 1 or len(sys.argv) > 2:
	print("""Usage:\n nhdownloader [nukecode] """)
	sys.exit()
# def keyboardInterruptHandler(signal, frame):
#     print("Keyboard Interrupt. Cleaning up")
#     sys.exit()

# signal.signal(signal.SIGINT, keyboardInterruptHandler)
def download(link,filename):
	
	urllib.request.urlretrieve(link,filename=filename)

	
	# try:
 #    	os.mkdir(str(Path.home())+"/Downloads/nhentai/"+str(self.response["title"]['english']))
 #    except FileExistsError:
 #    	pass
def return_code(link,):
	s = requests.get(link,proxies={"https":"https://178.128.91.34:44344"})
	return s.status_code
try:
	code = int(sys.argv[1])
	print("Connecting to https://nhentai.net...")
	try:
		response = requests.get("https://nhentai.net/api/gallery/"+sys.argv[1],proxies={"https":"https://178.128.91.34:44344"})
	except:
		print(f"{Fore.RED}Cannot Establish Connection to https://nhentai.net{Style.RESET_ALL}\nExiting.")
		sys.exit()
	if response.status_code == 200:
		source = json.loads(response.text)
		print(f"Source OK. Gathering information about : {source['title']['english']} ")
		#compiling the source 
		tags = []
		artist = []
		for x in source['tags']:
			if x['type'] == 'artist':
				artist.append(x['name'])
			if x['type'] == 'tag':
				tags.append(x['name'])
		tags = ", ".join(str(x) for x in tags)
		try:
			source['artist'] = artist[0]
			source['tags'] = tags
		except:
			source['artist'] = 'UNIDENTIFIED'
			source['tags'] = tags
		print(f"""[Title] :
	[English] : {source['title']['english']}
	[Japanese] : {source['title']['japanese']}
	[Pretty] : {source['title']['pretty']}\n
[Artist] : {source['artist']}\n
[Tags] : {source['tags']}\n
[Pages]:
	[Total Pages] : {source['num_pages']}\n
			""")
		imglib = {
			"j" : ".jpg",
			"p" : ".png"
		}
		default_download_path = str(Path.home())+"/Downloads/"
		print(f"{Fore.GREEN}Your Downloaded file will be under \"{default_download_path}{source['title']['english']}\"{Style.RESET_ALL}\n")
		confirm = input(f"{Fore.GREEN}[Ready!]{Style.RESET_ALL}Start Download Now?[y/n]")
		confirm = confirm.lower()
		if not "y" in confirm:
			print("Abort")
			sys.exit()
		if "y" in confirm:
			
				#code executed when the folder already exist
			

			#starting download
			num = 0
			try:
				if "/" in source['title']['english']:
					source['title']['english'] = source['title']['english'].replace("/"," ")
				folder_path = f"{default_download_path}{source['title']['english']}"
				os.mkdir(folder_path)
				print(f"{Fore.BLUE}Creating folder at : {default_download_path}{source['title']['english']}{Style.RESET_ALL}")
			except FileExistsError:
				count_file_resume = len([f for f in os.listdir(f"{default_download_path}{source['title']['english']}")if os.path.isfile(os.path.join(f"{default_download_path}{source['title']['english']}" , f))])	        
				if(count_file_resume == source['num_pages']):
					print(f"{Fore.GREEN}Download Already Complete. There is nothing to do.{Style.RESET_ALL}")
					sys.exit()
				print(f"{Fore.YELLOW}{default_download_path}{source['title']['english']} is exist. resuming...{Style.RESET_ALL}")
				num = count_file_resume

			count_done = source['num_pages']
			if count_file_resume > 1:
				num = num -1
			for x in source['images']['pages']:
				num+=1
				percent = num / count_done * 100
				percent = int(percent)
				try:
					
					proxy = urllib.request.ProxyHandler({'https': 'https://178.128.91.34:44344'})
					# construct a new opener using your proxy settings
					opener = urllib.request.build_opener(proxy)
					# install the openen on the module-level
					urllib.request.install_opener(opener)
					download(f"https://i.nhentai.net/galleries/{source['media_id']}/{num}{imglib[x['t']]}",f"{default_download_path}{source['title']['english']}/{num}{imglib[x['t']]}")
					print(f"https://i.nhentai.net/galleries/{source['media_id']}/{num}{imglib[x['t']]}({num}/{count_done}){Fore.GREEN}[{percent}%]{Style.RESET_ALL}")
					if num == count_done:
						break
				except urllib.error.HTTPError:
					status = return_code(f"https://i.nhentai.net/galleries/{source['media_id']}/{num}{imglib[x['t']]}")
					print(f"{Fore.RED}[Error] https://i.nhentai.net/galleries/{source['media_id']}/{num}{imglib[x['t']]}{Style.RESET_ALL} Returning Error {status}")
		
			print(f"{Fore.GREEN}Download Competed. Your Downloaded file at : \"{default_download_path}{source['title']['english']}\"{Style.RESET_ALL}\n")
		else:
			print("Abort")
			sys.exit()

except ValueError:
	print(f"{Fore.RED}Error Processing The Code : {sys.argv[1]} {Style.RESET_ALL}")
	sys.exit()

