import gtts
import os

text = input("Enter text: ")

sound = gtts.gTTS(text, lang="en")

sound.save("welcome.mp3")

os.system("welcome.mp3")
