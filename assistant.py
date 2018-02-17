import speech_recognition as sr
from pyowm import OWM # impoting the weather module
import pyowm
import os

r = sr.Recognizer()
with sr.Microphone() as source:  # use the default microphone as the audio source
    audio = r.listen(source)  # listen for the first phrase and extract it into audio data

try:
    stringout = r.recognize_google(audio)
    print(stringout.lower())  # recognize speech using Google Speech Recognition
except LookupError:  # speech is unintelligible
    print("Could not understand audio")

stringout = stringout.lower()
os.system("say " + stringout)
if stringout == 'take a picture': # take a picture input from the google voice recognition
    os.system(" imagesnap -w 1 snapshot.png")

if stringout == 'youtube': #open youtube.com
    os.system("open http://youtube.com")

elif stringout == 'take a note':   #takes note
        os.system("say what you want to note")

        with sr.Microphone() as source:  # use the default microphone as the audio source
            audio = r.listen(source)  # listen for the first phrase and extract it into audio data

        try:
            note = r.recognize_google(audio)
            print(note.lower())  # recognize speech using Google Speech Recognition
        except LookupError:  # speech is unintelligible
            print("Could not understand audio")
        with open("notefile.txt", "w") as notefile:
            notefile.write(note)
        os.system("say hey amit the note has been saved")
elif stringout == 'open itunes':
    os.system("open /Applications/iTunes.app")

elif stringout =='what is the weather':

    owm = pyowm.OWM('a7879553cd0fd5d1d69afc52c11fec69')  # You MUST provide a valid API key
# Will it be sunny tomorrow at this time in kalyani (india) ?
    forecast = owm.daily_forecast("Kalyani,India")
    tomorrow = pyowm.timeutils.tomorrow()
    forecast.will_be_sunny_at(tomorrow)  # Always True in Italy, right? ;-)

    # Search for current weather in kalyani (india)
    observation = owm.weather_at_place('Kalyani,India')
    w = observation.get_weather()
    print(w)  # <Weather - reference time=2013-12-18 09:20,
    # Weather details
    print(w.get_wind(), w.get_humidity(), w.get_temperature('celsius'))