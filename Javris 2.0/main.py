import pyttsx3  # For The Sound Of Jarvis
import datetime  # So Jarvis Can Wish Me
import speech_recognition as sr  # So Jarvis Can Listen My Voice
import wikipedia  # To Search WikiPidia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning')
        print('Jarvis : Good Morning')
    elif hour >= 12 and hour < 18:
        speak('Good AfterNoon')
        print('Jarvis : Good AfterNoon')
    else:
        speak('Good Evening')
        print('Jarvis : Good Evening')

    speak('I am Jarvis Sir. Please Tell Me How May I Help You!!')


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kkhalid53c@gmail.com', 'zeeshanlhr')
    server.sendmail('kkhalid53c@gmail.com', to, content)
    server.close()
if __name__ == "__main__":
    WishMe()
    while True:
     query = takeCommand().lower()
     if 'wikipidia' in query or 'search' in query or 'look' in query or 'find' in query:
         speak('Searching WikiPidia')
         query = query.replace("wikipedia", "")
         results = wikipedia.summary(query, sentences=2)
         speak("According to Wikipedia")
         print(results)
         speak(results)

     elif 'youtube' in query:
            speak('Opening Youtube')
            webbrowser.open("http://youtube.com")
     elif 'google'in query:
         webbrowser.open("http://google.com")

     elif 'play music'in query or 'play boobahyah'in query or 'music that i like'in query:
         webbrowser.open('https://www.youtube.com/watch?v=bwmSjveL3Lc')
     elif 'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")    
         speak(f"Sir, the time is {strTime}")
   
     elif 'open code' in query:
      codePath = "C:\\Users\\kkpc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
      os.startfile(codePath)

     elif 'sleep' in query:
          speak('Thanks For Your Time Sir . Sweet Dreams') 
     elif 'make me happy' in query:
          speak('I Have A Song To Make You  Happy')
          webbrowser.open('https://www.youtube.com/watch?v=9iYT3L3SqkA')
     

     
     elif 'bye' in query or 'quit' in query:
         speak('Bye Sir . Thanks For Your Time')
         exit()



     elif 'email to zeeshan' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "kkhalid53c@gmail.com"    
            sendEmail(to, content)
            speak("Mail has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry my friend harry bhai. I am not able to send this email")                            