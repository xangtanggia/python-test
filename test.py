print('hello')
import speech_recognitionp
robotear=speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    audio = robotear.record(mic, duration=5)
luutru = robotear.recognize_google(audio,language='vi-VN')
print(luutru)
