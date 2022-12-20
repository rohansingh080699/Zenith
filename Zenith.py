# Zenith is a Personal Virtual Assistant which can
# understand the voice command given to it and is also
# capable of performing other multifarious tasks told
# by the user to it. Combined with a few python libraries,
# Zenith can perform multifarious tasks like playing songs
# in Internet, playing videos in Youtube, searching on
# Google, opening various Apps and even do calculations
# using wolframalpha.

import speech_recognition as sr
import playsound
from gtts import gTTS
import os
import webbrowser
import wolframalpha # to do online calculations
from selenium import webdriver # selenium library is used to access websites
from selenium.webdriver.common.keys import Keys
import time

# function to save and play Zenith's audio

num = 1
def Zenithspeaks(output):
	global num

	# num to rename every audio file 
	num += 1
	print("ZENITH: ", output)

	toSpeak = gTTS(text = output, lang ='en', slow = False)

	file = str(num)+".mp3"
	toSpeak.save(file)

	playsound.playsound(file, True)
	os.remove(file)

# function to get audio from user

def Zenithinputaudio():

	ZenithObject = sr.Recognizer()
	audio = ''

	with sr.Microphone() as source:
		print("Speak...")

		# recording the audio
		audio = ZenithObject.listen(source, phrase_time_limit = 5)
	print("Stop.") # limit 5 secs

	try:

		text = ZenithObject.recognize_google(audio, language ='en-US')
		print("You: ", text)
		return text

	except:

		Zenithspeaks("Could not understand you, Please try again !")
		return 0

# function to search on web with selenium (you need to download chrome or firefox driver to run this function)

def Zenithweb(input):

	driver = webdriver.Chrome(executable_path=r'C:\Users\hp\Desktop\Apps\Chromedriver.exe')#path of the driver file
	driver.implicitly_wait(5)
	driver.maximize_window()

	if 'youtube' in input.lower():

		Zenithspeaks("Opening in youtube")
		indx = input.lower().split().index('youtube')
		query = input.split()[indx + 1:]
		driver.get("http://www.youtube.com")
		driver.find_element_by_name("search_query").send_keys(query) #searching the search bar by name and sending the query
		driver.find_element_by_xpath("//*[@id='search-icon-legacy']/yt-icon").click() # finding the buttuon to click for search
		return


	elif 'wikipedia' in input.lower():

		Zenithspeaks("Opening in Wikipedia")
		indx = input.lower().split().index('wikipedia')
		query = input.split()[indx + 1:]
		driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
		return


	elif 'google' in input.lower():

			indx = input.lower().split().index('google')
			query = input.split()[indx + 1:]
			Zenithspeaks("Opening in Google")
			driver.get("https://www.google.com")
			que=driver.find_element_by_xpath("//input[@name='q']")
			que.send_keys(query)
			time.sleep(2)
			que.send_keys(Keys.RETURN)
			return

	else:

		Zenithspeaks("Opening in Google")
		driver.get("https://www.google.com")
		query = input.lower()
		que = driver.find_element_by_xpath("//input[@name='q']")
		que.send_keys(query)
		time.sleep(2)
		que.send_keys(Keys.RETURN)
		return

# function to open  applications

def Zenithopenapplication(input):

	if "chrome" in input:
		Zenithspeaks("Opening Google Chrome")
		os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
		return

	elif "firefox" in input or "mozilla" in input:
		Zenithspeaks("Opening Mozilla Firefox")
		os.startfile("C:\Program Files (x86)\Mozilla Firefox\Firefox.exe")
		return

	elif "word" in input:
		Zenithspeaks("Opening Microsoft Word")
		os.startfile('C:\Program Files\WindowsApps\Microsoft.Office.Desktop.Word_16051.13001.20384.0_x86__8wekyb3d8bbwe\Office16\WINWORD.exe')
		return

	elif "excel" in input:
		Zenithspeaks("Opening Microsoft Excel")
		os.startfile('C:\Program Files\WindowsApps\Microsoft.Office.Desktop.Excel_16051.13001.20384.0_x86__8wekyb3d8bbwe\Office16\EXCEL.exe')
		return

	else:

		Zenithspeaks("Can not open. You need to add this application in my open application function")
		return

# fumction to sort the input by user 

def Zenithprocess(input):
	try:
		if 'google' in input.lower() or 'youtube' in input.lower() or 'wikipedia' in input.lower():
			Zenithweb(input)
			return

		elif "what can you do" in input.lower() or "tell me something about yourself" in input.lower():
			speak = '''Hello, I am ZENITH, your personal Assistant. I am here to make your life easier. You can command me to perform multifarious tasks such as calculating diffrentials and integrals, opening applications, searching on google, wikipedia something and even to search videos on youtube'''
			Zenithspeaks(speak)
			return

		elif "who made you" in input.lower() or "who created you" in input.lower():
			speak = "I have been created by Rohan Singh."
			Zenithspeaks(speak)
			return

		elif "calculate" in input.lower():

			# using wolframalpha website to do calculations(you need to add your own wolframalpha api key here)
			appid = "**************" # wolframalpha api key
			client = wolframalpha.Client(appid)

			indx = input.lower().split().index('calculate')
			query = input.split()[indx + 1:]
			res = client.query(' '.join(query))
			answer = next(res.results).text
			Zenithspeaks("The answer is " + answer)
			return

		elif 'open' in input:

			# another function to open
			# different application availaible
			Zenithopenapplication(input.lower())
			return

		else:

			Zenithspeaks("I can search the web for you, Do you want to continue?")
			ans = Zenithinputaudio()
			if 'yes' in str(ans) or 'yeah' in str(ans):
				Zenithweb(input)
			else:
				return
	except :

		Zenithspeaks("I don't understand, I can search the web for you, Do you want to continue?")
		ans = Zenithinptaudio()
		if 'yes' in str(ans) or 'yeah' in str(ans):
			Zenithweb(input)

# Driver Code
if __name__ == "__main__":
	Zenithspeaks("What's your name?")

	name = get_audio()
	Zenithspeaks("Hello," +name+ '.')

	while(1):

		Zenithspeaks("What do you want me to do?")
		text = Zenithinputaudio().lower()

		if text == 0:
			continue
        # terminating words
		if "exit" in str(text) or "bye" in str(text) or "terminate" in str(text) or "sleep" in str(text):
			Zenithspeaks("Ok bye, "+ name+'.')
			break

		# process the input given by user.
		Zenithprocess(text)
