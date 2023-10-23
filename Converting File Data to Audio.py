from gtts import gTTS
import os
text=open('demo.txt','r',encoding='utf-8').read()
output=gTTS(text=text,lang="ml",slow=False)
output.save("output.mp3")
os.system("start output.mp3")