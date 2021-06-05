Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from gtts import gTTS#Import the required module for text to speech conversion
>>> import os #This modul is imported so thate we can play the converted audio
>>> mytext="The authors do not work for, consult, own shares in or receive funding from any company or organisation that would benefit from this article, and have disclosed no relevant affiliations beyond their academic appointment." #The text that you want to convert to audio
>>> language = 'en'#Language in which you want to convert
>>> myobj= gTTS(text=mytext,lang=language,slow=False)#Passing the text and language to the engine
>>> myobj.save("music.mp3")#Saving the converted audio in mp3 file
>>> os.system("sound.mp3")
1
>>> 