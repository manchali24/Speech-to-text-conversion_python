# Speech-to-text-conversion_python

Speech to text conversion in python in GUI Window

Speech to text conversion in Python (Pytalk)
Description: 

Speech recognition involves recording spoken words using either a microphone or telephone.

The audio is then converted into a set of words stored digitally.

Speech Recognition is a process in which a computer or device record the speech of humans and convert it into text format.
Voice recognition works by scanning the aspects of speech that differ between individuals.

Requirements:
1. Install Python 2.7 

2. Import Tkinter, Speech Recognition, PyAudio python libraries.

You can use any software to run this project like PyCharm, IDLE, etc.
Here, I have used PyCharm.

Analysis:
•	We have analysed, we have to convert the speech or audio in to text.

•	As we execute the Python file, the message will come to Say Something.

•	The audio or speech will be listen using PyAudio library.

•	We have to speak and wait for a time then what ever you have spoken will be displayed on GUI Screen as well as on Console window.

•	This is how the Speech recognition works.


Implementation Phase:
The entire part of the code executes at the background for respective GUI.

Module 1- Import libraries
Import the required libraries of Python needed to execute the Speech Recognition.
	import speech_recognition as sr
  	from Tkinter import *

Module 2 - Create a Blank screen
 		root = Tk()
 		root.geometry("1000x400")

Module 3 - Create the recognize and mic instances
r = sr.Recognizer()
with sr.Microphone() as source:

Module 4 - Reads the Audio or Speech File and listen
		audio = r.listen(source)

Module 5 - Recognizing the Speech
		text = r.recognize_google(audio)
		print('You said : {}'.format(text))


