import speech_recognition as sr
import PyAudio
from Tkinter import *

root = Tk()
root.geometry("1000x400")
root.title("Speech to text")

r = sr.Recognizer()

with sr.Microphone() as source:
    #w = Label(root, text="Say Something", font="Consolas 24")
    print("Say Something:")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        w = Label(root, text=text, font="Consolas 24")
        print('You said : {}'.format(text))
    except:
        print("Sorry couldn't recognize your voice")

w.pack()
root.mainloop()