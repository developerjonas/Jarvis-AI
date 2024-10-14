from sys import exception
from time import strftime

import speech_recognition as sr
import os
import webbrowser as wb
import openai
import datetime as dt

def say(text):
    os.system(f"say {text}")

say("Hello I am Jarvis A.I")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occoured , Sorry from Jarvis"

while True:
    try:
        print("listening")
        query = take_command()
        sites = [
                    ["YouTube", "https://www.youtube.com"],
                    ["Google", "https://www.google.com"],
                    ["GitHub", "https://www.github.com"],
                    ["Stack Overflow", "https://stackoverflow.com"],
                    ["Reddit", "https://www.reddit.com"],
                    ["Wikipedia", "https://www.wikipedia.org"],
                    ["Twitter", "https://www.twitter.com"],
                    ["LinkedIn", "https://www.linkedin.com"],
                    ["Facebook", "https://www.facebook.com"],
                    ["Amazon", "https://www.amazon.com"],
                    ["Medium", "https://www.medium.com"],
                    ["Netflix", "https://www.netflix.com"],
                    ["Twitch", "https://www.twitch.tv"],
                    ["Quora", "https://www.quora.com"],
                    ["Hacker News", "https://news.ycombinator.com"],
                    ["BBC", "https://www.bbc.com"],
                    ["CNN", "https://www.cnn.com"],
                    ["New York Times", "https://www.nytimes.com"],
                    ["Microsoft", "https://www.microsoft.com"],
                    ["Apple", "https://www.apple.com"],
                    ["Dev.to", "https://dev.to"],
                    ["GitLab", "https://www.gitlab.com"],
                    ["Bitbucket", "https://bitbucket.org"],
                    ["CodePen", "https://codepen.io"],
                    ["Replit", "https://replit.com"],
                    ["Glitch", "https://glitch.com"],
                    ["MDN Web Docs", "https://developer.mozilla.org"],
                    ["W3Schools", "https://www.w3schools.com"],
                    ["GeeksforGeeks", "https://www.geeksforgeeks.org"],
                    ["LeetCode", "https://leetcode.com"],
                    ["HackerRank", "https://www.hackerrank.com"],
                    ["CodeSignal", "https://codesignal.com"],
                    ["Codecademy", "https://www.codecademy.com"],
                    ["FreeCodeCamp", "https://www.freecodecamp.org"],
                    ["Coursera", "https://www.coursera.org"],
                    ["Udemy", "https://www.udemy.com"],
                    ["Khan Academy", "https://www.khanacademy.org"],
                    ["PyPI", "https://pypi.org"],
                    ["npm", "https://www.npmjs.com"],
                    ["Jenkins", "https://www.jenkins.io"],
                    ["Travis CI", "https://travis-ci.com"],
                    ["CircleCI", "https://circleci.com"],
                    ["Docker Hub", "https://hub.docker.com"],
                    ["DigitalOcean", "https://www.digitalocean.com"],
                    ["AWS", "https://aws.amazon.com"],
                    ["Azure", "https://azure.microsoft.com"],
                    ["Google Cloud", "https://cloud.google.com"],
                    ["Vercel", "https://vercel.com"],
                    ["Netlify", "https://www.netlify.com"],
                    ["Heroku", "https://www.heroku.com"],
                    ["JetBrains", "https://www.jetbrains.com"],
                    ["Visual Studio Code", "https://code.visualstudio.com"]
                ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                wb.open(f'{site[1]}')
                say(f"Opening {site[0]} Sir")
            if "time" in query:
                strfTime = dt.datetime.now().strftime("%H:%M:%S")
                say(f"Sir the time is {strfTime}")
            if "contacts" in query.lower():
                os.system(f"open /System/Applications/Contacts.app")
                say("Opening Contacts")

    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting gracefully...")