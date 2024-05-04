import contextlib
import random
import pyttsx3
import datetime
import speech_recognition as sr
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import openai
import os
import requests
import clipboard
import pyjokes
import time as tt
import requests
from PIL import Image
from io import BytesIO
import requests
import ctypes
import vlc
import subprocess
from pocketsphinx import LiveSpeech
import nltk

def speak(audio):
 engine.say(audio)
 engine.runAndWait()
 
def time():
  Time = datetime.datetime.now().strftime("%I hour %Mminutes %Sseconds")
  speak("the current time is")
  speak(Time)

def date():
  year = int(datetime.datetime.now().year)
  month = int(datetime.datetime.now().month)
  day = int(datetime.datetime.now().day)
  speak("the current date is")
  speak(day)
  speak(month)
  speak(year)

def wishme():
 text= ["Hello!","Hi!","Good to see you!","Your voice always makes me happy","I am happy to be here."]
 ran_txt=random.choice(text)
 speak(ran_txt)
 speak("How can Yumi help you?")
 query = "first"
 return query


def greeting():
  hour = datetime.datetime.now().hour
  if hour >= 6 and hour < 12 :
    speak("Good Morning sir.")
  elif hour >= 12 and hour < 16 :
    speak("Good Afternoon sir.")
  elif hour >= 16 and hour < 24 :
    speak("Good Evening sir.")
  else :
    speak("Good Night sir.")
  query = wishme()
  return query

def commandtxt():
  query = input("\n")
  return query

def commandmic():
  r = sr.Recognizer()
  attempt = 0
  while True:
   with sr.Microphone() as source :
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)
   try :
    print("Recognising...") 
    with open(os.devnull, 'w') as devnull:
     with contextlib.redirect_stdout(devnull):
      query = r.recognize_google(audio,show_all=False)  
    return query
   except Exception as e :
    attempt+=1
    if attempt == 1:
     print(e)
     speak("Yumi couldn't understand that.")
     speak("Could you repeat it again!")
    else:
     return "mute"   
   

def weather():
  speak("Tell me the city you want to know the weather of")
  city = commandmic().lower()
  try:
   url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID=49c8c44d9ea44c1426d049705949e512'
   res = requests.get(url)
   data = res.json()
   wea = data['weather'] [0] ['main']
   temp = data['main']['temp']
   desc = data['weather'] [0] ['description']
   wind = data['wind']['speed']
   hum = data['main']['humidity']
   temp = round(temp/10)
   speak(f'The weather in {city} city is: ')
   speak(wea)
   speak('The current temperature is: {} degree celsius'.format(temp))
   speak("You will be seeing {} today".format(desc))
   speak("You will be experiencing wind of speed {} km per hour".format(wind))
   speak("Humidity will be {} percent".format(hum))
  except Exception as e:
    speak("Please be more specific of the city sir.")
    speak("I couldn't find a city with that specification.")

def wiki():
      speak("Can you be specific what you want to know about sir?")
      about = commandmic()
      result = wikipedia.summary(about, sentences=2)
      print(result)
      speak(result)
      speak("Should i repeat that again?")
      com = commandmic()
      if com == "yes":
        speak(result)
      elif com == "no":
        speak("Okay sir")     
      else:
        speak("Sorry I couldn't understand that.")

def news():
  while True: 
   url = "https://real-time-news-data.p.rapidapi.com/topic-headlines"
   arra = [
     "WORLD",
     "NATIONAL",
     "BUSINESS",
     "TECHNOLOGY",
     "ENTERTAINMENT",
     "SPORTS",
     "SCIENCE",
     "HEALTH"
   ]
   speak(f"Choose the topic from {arra}?")
   topic = commandmic().upper()
   if topic in arra:
    speak("Which country sir?") 
    coun = commandmic()
    coun_abb = {"India": "IN", "United States": "US", "Japan": "JP", "United Kingdom": "UK", "Russia": "RU" }
    if coun in coun_abb:
     country = coun_abb[coun]
     querystring = {"topic": topic,"country": country,"lang":"en"}
     headers = {
	   "X-RapidAPI-Key": "your api key",
	   "X-RapidAPI-Host": "real-time-news-data.p.rapidapi.com"
     }
     response = requests.request("GET", url, headers=headers, params=querystring)
     if "title" in response.json(): 
       for i in range(6):
        if i < len(response.json()['data']):
         inp = int(i)
         if len(response.json()['data']) == 0:
          break
         else:
          track_name = response.json()['data'][inp]['title']
          speak(track_name)
          count = 0
          for j in range(3):
           jup = int(j)
           if j < len(response.json()['data'][inp]['sub_articles']):
             if "sub_articles" not in response.json():
               break
             else:
                track_sub = response.json()['data'][inp]['sub_articles'][jup]['title']

                if count == 0:
                 speak("Sub articles suggest:")
                 count +=1
                else:
                  listof = ["With that,","Also,","Furthermore,","Additionally,"]
                  ran = random.choice(listof)
                  speak(ran)
                speak(track_sub)
           else:
             print("...")
     
        else:
           print("...")      
     else: 
       speak(f"I didn't find anything relating to the topic {topic} in {coun}!")

     speak("That's it for now, I'll update more later sir!")
     speak("Do you want to hear about any other topic?")
     choic = commandmic().lower()
     if "yes" in choic:
      speak("Okay")
     elif "no" in choic:
       speak("Okay,just tell me when you want to hear some news")
       break
     else:
      speak("I couldn't understand that, sir!")
      break
    else:
     speak("Please mention the country again!")
    
   elif 'NO'in arra:
     speak("Okay,  ")
   else:
     speak('Invalid Option!')
  
def t2speech():
  text = clipboard.paste()
  speak(text)

def open1():
  speak("Sir, what do you want me to open?")
  try:
   op_ap = commandmic().lower()
   codepath = f"E:\Applications\{op_ap}"
   os.startfile(codepath)
   speak("Done sir!")
  except Exception as e:
    speak(f"I couldn't fine any {op_ap} in your PC")

def open2(query):
    if "alpha" in query:
     os.startfile("C:\\")
     speak("Done sir!")
    elif "beta" in query:
     os.startfile("D:\\")
     speak("Done sir!")
    elif "sigma" in query:
     os.startfile("E:\\")
     speak("Done sir!")
    else:
     query = query.replace("open my ", "")
     path = query.capitalize()

     try:
        os.startfile(os.path.expanduser(f'~\\{path}'))
        speak("Done sir!")  
     except Exception as e:
        speak("The specified file is not in your PC sir!")

def whatsapp():
  user_name = {
        'mom':'***',
        'dad':'***'
        }     
  try:
        speak("Who should i send message to?")
        name = commandmic()
        phone_no = user_name[name]
        speak("What is the message?")
        message = commandmic()
        Message = message
        wb.open('https://web.whatsapp.com/send?phone=' +phone_no+ '&text=' +Message)
        sleep(10)
        pyautogui.press('enter')
        speak("Message has been sent sir.")
  except Exception as e:
        print(e)
        speak("Unable to send message.")

def screenshot(query):
  while True:
   if "no" in query:
     speak("If you want to take more screenshots, let me know")
     break
   else:  
    name_img=tt.time()
    name_img='E:\\My Practises\\Yume\\screenshots\\{}.png'.format(name_img)
    speak("Waiting 5 seconds")
    tt.sleep(5)
    speak("Taking screenshot!")
    img=pyautogui.screenshot(name_img)
    img.show()
    speak("Done sir!")
    speak("Shall i continue?")
    query=commandmic().lower()

def rememberthat(query):
  data1 = query.replace("remember that ","")
  data = data1.capitalize()
  while True: 
   speak("You have told me to remember that" +data)
   rem_data=open("E:\\My Practises\\Yume\\Notes.txt","a")
   rem_data.write(data + "." + "\n")
   rem_data.close()
   speak("Is this enough sir?")
   ans=commandmic().lower()
   if "yes" in ans:
     speak("Okay noted!")
     break
   else:
     speak("What should i remember sir!")
     data = commandmic().capitalize()

def toremember():
  with open('E:\\My Practises\\Yume\\Notes.txt', "r") as rem_data:
    data = rem_data.read()
  token = nltk.word_tokenize(data)
  print(token)
  
  speak("You have told be to remember that" +data)
  speak("That's it sir!")
  rem_data.close()

def playaudio():
  player = vlc.MediaPlayer()
  media = vlc.Media("E:\My Practises\Yume\yawn.mp3")
  player.set_media(media)
  player.play()
  while player.get_state() != vlc.State.Ended:
    pass
  player.release()

def flip():
  speak("Okay!")
  while True:
   speak("Heads or Tails?")
   choice_inp = commandmic().lower()
   alter = ['tales','tails']
   if choice_inp in alter:
     choice_inp = "tails"
   coin = ["heads", "tails"] 
   flip = random.choice(coin)
   if choice_inp in coin:
    if choice_inp == flip:
      speak("Hurray! You won the toss. It's a {}".format(flip))
      break
    else:
      speak("Ouch!, You lost the toss. It's a {}".format(flip))
      break
   else:
    speak("Did you pick the correct choice?")
    speak("Wanna try again?")
    choic = commandmic().lower()
    if "yes" in choic:
     speak("Okay, let's go again.")
    elif "no" in choic:
     speak("Okay")
     break
    else:
     speak("I couldn't understand that, sir!")
     break

def name():
   speak("My name is Yumi.")

def music():
 while True: 
  url = "https://spotify-web2.p.rapidapi.com/search/"
  speak("What do you want to hear? (track, album or artist)")
  lis = ['track','album','artist']
  opt = commandmic().lower()
  if opt in lis:
   speak("Which {} do you want to hear?".format(opt))
   que = commandmic()
   querystring = {"q": que,"type": opt,"limit":"5"}
   headers = {
	 "X-RapidAPI-Key": "your api",
	 "X-RapidAPI-Host": "spotify-web2.p.rapidapi.com"
   }
   response = requests.request("GET", url, headers=headers, params=querystring)
   opt2 = opt + "s"
   opt3 = str(opt2)
   for i in range(6):
     if i < len(response.json()[opt3]['items']):
      if opt3 == 'tracks' or opt3 == 'albums':
       track_name = response.json()[opt3]['items'][i]['data']['name']
       speak(track_name)
      elif opt3 == 'artists':
       track_name = response.json()[opt3]['items'][i]['data']['profile']['name']
       speak(track_name) 
     else:
      print("...")
   speak("Please choose one from below.")
   inp = commandmic().lower()
   arra = {"first": 0,"second": 1,"third": 2,"fourth": 3,"fifth": 4}
   if inp in arra:
    num = arra[inp]
    inte = int(num) 
    track_url = response.json()[opt3]['items'][inte]['data']['uri']
    if opt3 == 'artists':
      track_name = response.json()[opt3]['items'][inte]['data']['profile']['name']
    else:
     track_name = response.json()[opt3]['items'][inte]['data']['name']
    if opt3 in ['artists','albums']:
     wb.open(track_url)
     tt.sleep(5)
     speak(f"Playing the {opt} {track_name}")
     quit()
    else:
     track_dur = int((response.json()[opt3]['items'][inte]['data']['duration']['totalMilliseconds'])/1000)
     wb.open(track_url)
     tt.sleep(5)
     speak(f"Playing the song {track_name}")
     tt.sleep(track_dur)
   elif "none" in inp :
    speak("okay.")
    break
   else:
     speak("You have selected invalid option")

   speak("Do you want to hear another music?")
   ans = commandmic().lower()
   if "yes" in ans:
     speak("Okay, sir")
   elif "no" in ans:
     speak("Whenever you want to hear music, just say the command.")
     break
   else:
     speak("Invalid command.")
     break
  elif "none" in opt:
    speak("okay, sir")
    break
  elif "my playlist" in opt:
    speak("What do you want me to open in your playlist?")
    an = commandmic().lower()
    if "mood" in an:
     uri = "spotify:playlist:76kkI5eSwqcfeYU4Z4aV9T?si=95a7a054bb1b4db6"
     wb.open(uri)
    elif "profile" in an:
     uri = "spotify:user:95k1dds3thokvnotokjeq0bmt?si=26434178afd549ad"
     wb.open(uri)
    else:
      speak(f"Sorry i couldn't find {an}")
      break
  else:
    speak("Please speak clearly.")

def ChatGPT1():
  speak("Informational Yumi is here")
  count = 0
  if count == 0:
    speak("hello!")
  while True:
   QA = commandmic().lower()
   if "exit" in QA:
     speak("Thank you for spending time with me.")
     break
   response = openai.Completion.create(
   engine="text-davinci-003",
   prompt = QA,
   max_tokens=100,
   n=1,
   stop=None,
   temperature=0
  )
   message = response.choices[0].text.strip()
   if count == 0:
    text=["Sir","According to me!","In my knowledge"]
    ran_txt=random.choice(text)
    speak(ran_txt)
    print(message)
    speak(message)
    count+=1
   else: 
    print(message)
    speak(message)
    
def ChatGPT2():
  speak("Conversational Yumi is here")
  count = 0
  if count == 0:
    speak("hello!")
  while True:
   QA = commandmic().lower()
   if "exit" in QA:
     speak("Thank you for spending time with me.")
     break
   response = openai.Completion.create(
   model="gpt-3.5-turbo",
   messages = [
     {"role": "user", "content": QA}
   ]
  )
   message = response.choices[0].text.strip()
   if count == 0:
    text=["Sir","According to me!","In my knowledge"]
    ran_txt=random.choice(text)
    speak(ran_txt)
    print(message)
    speak(message)
    count+=1
   else: 
    print(message)
    speak(message)


def ChatGPTImage():
 while True:
  speak("What do you want to create sir?")
  to_get = commandmic().lower()
  response = openai.Image.create(
  prompt= to_get,
  n=1,
  size="1024x1024"
  )
  speak("Processing.")
  image_url = response['data'][0]['url']
  img_get = requests.get(image_url)
  img = Image.open(BytesIO(img_get.content))
  speak("Processing Completed.")
  speak("Do you want to see the image?")
  ans = commandmic().lower()
  if "yes" in ans:
    img.show()
  speak("Shall i save the image?")
  ans = commandmic().lower()
  if "yes" in ans:
    speak("JPG or PNG")
    res = commandmic().lower()
    name_img=tt.time()
    if "jpg" in res:
     img.save('E:\\My Practises\\Yume\\AI images generated\\{}.jpg'.format(name_img), 'JPEG')
     speak("Image saved sir.")
    elif "png" in res:
     img.save('E:\\My Practises\\Yume\\AI images generated\\{}.png'.format(name_img), 'PNG')
     speak("Image saved sir.")
    else:
      speak("The response is invalid sir.")
  
  elif "no" in ans:
    speak("Okay sir.")
  else:
    speak("Invalid response sir.")
  speak("Do you want to try again?")
  ans = commandmic().lower()
  if "yes" in ans:
    speak("Okay.")
  elif "no" in ans:
    speak("Closing Generator.")
    break
  else:
    speak("Invalid Response sir.")
    speak("Closing Generator.")
    break

def features():
  feature = ["have a conversation with you", "tell you the time and date", "send message for you", "search for anything on the wikipedia", "tell the weather update", 
             "tell the news for you", "open any application or file directory", "create a joke for you", "take a screenshot", "read anything you highlight"
             , "remember notes for you", "toss a coin", "generate an image with the help of artificial intelligence", "sleep,reboot or shutdown your PC", "play music for you"]
  speak(f"I can,{feature}.")
  speak("That is the things I can do.")
  speak("Do you want me to do something?")
  return "feature"

def silent():
  WAKE_WORDS = ["speak"]
  speak("Okay, being silent.")
  while True:
    speech = LiveSpeech(
        verbose=False,
        sampling_rate=16000,
        buffer_size=2048,
        no_search=False,
        full_utt=True,
        lm=False,
        keyphrase=" | ".join(WAKE_WORDS),
        kws_threshold=7,
    )
    print("Waiting...")
    for phrase in speech:
        speak("I am back!")
        break
    break

def initiation(quo, query, count):
   if "knowledge" in query:
     ChatGPT1()
   elif "chat" in query:
     ChatGPT2()
   elif quo in query:
     query = greeting()
   elif query == "yumi":
     query = wishme()
   elif "time" in query:
     time()
   elif "date today" in query:
     date()
   elif "no" in query:  
     if_no = ["Okay, if you need any help just ask me!", "Okay, maybe later", "Yup!", "Bye-bye", "Okay, see you soon"]
     no = random.choice(if_no)
     speak(no)
     quit()
   elif "message" in query:
      whatsapp()
   elif "search" in query:
      wiki()
   elif "offline" in query:
      quit()
   elif "weather" in query:
      weather()
   elif "news" in query:
      news()  
   elif "read" in query:
      t2speech()  
   elif "open an application" in query:
      open1()
   elif "open my" in query:
      open2(query)
   elif "thank" in query:
      text = ["I am always happy to do anything for you, no need to thank me sir!","You are too polite sir!","Your wish is always my command, happy to assist you sir!","you are welcome"]
      ran_txt = random.choice(text)
      speak(ran_txt)
      speak("sayonara")
      quit()
   elif "joke" in query:
      joke = pyjokes.get_joke(language="en", category = "all")
      print(joke)
      speak(joke)
   elif "screenshot" in query:
      screenshot(query)
   elif "remember that" in query:
      rememberthat(query)
   elif "to remember" in query:
      toremember()
   elif "coin" in query:
      flip()
   elif "mute" in query:
      speak("You haven't said anything sir!")
      quit()
   elif "your name" in query:
      name()
   elif "image" in query:
      ChatGPTImage()
   elif "music" in query:
      music()
   elif "you do" in query:
      query = features()
   elif "shutdown" in query:
     speak("Shutting down PC!")
     os.system("shutdown /s /t 0")
   elif "reboot" in query:
     speak("Rebooting PC!")
     os.system("shutdown /r /t 0")  
   elif "sleep" in query:
     playaudio()
     speak("Good night sir")
     ctypes.windll.PowrProf.SetSuspendState(1, 0, 0)
   elif "silent" in query:
     silent()
   else:
     speak("Sorry, it is not in my commands!")
  
   if query == "first":
     count+=1
   elif query == "feature":
     count+=1
   else:  
    speak("Is there something else?")  
    count+=1
   return count
 
api_key = "api key"
openai.api_key = "your api key"  
engine = pyttsx3.init()

if __name__ == "__main__":
 speak("Yumi is here")
 speak("How can i help you?")
 data = datetime.datetime.now().hour
 if data >= 6 and data < 12 :
    quo ="good morning"
 elif data >= 12 and data < 16 :
    quo ="good afternoon"
 elif data >= 16 and data < 24 :
    quo ="good evening"
 else :
     quo ="good night"
 wakeword = "yumi"
 count = 0    
 while True:
  query = commandmic().lower()
  alt=["you me", "you may", "give me", "give may"]
  for a in alt:
   if a in query:
    query = query.replace(a,"yumi")
    break
  # if count == 0:
  #  if wakeword in query:
    #  count = initiation(quo, query, count)
  #  else:
    #  speak("Who are you speaking to?, did you forget to call my name?")
    #  quit()
  # else:
  count = initiation(quo, query, count) 
