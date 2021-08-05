import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")

    else:
        speak("Good evening!")

    speak("I am Crane  please tell me how may i help you?")


def takeCommand():
    # it takes microphone from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("recoginizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please....")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('np01cp4s200026@islingtoncollege.edu.np',
                 'manisha@9864459297')
    server.sendEmail('np01cp4s200026@islingtoncollege.edu.np', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()

    while True:
        # if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverFlow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'F:\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" Dear Manisha, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Manisha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "marsi.regmi@gmail.com"
                sendEmail(to, content)
                speak("Emali has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Manisha . I am not able to send email at this moment")

        elif 'exit' in query:
            exit
