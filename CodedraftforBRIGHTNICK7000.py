#Importing necessary modules
import os
import subprocess
import threading
from playsound import playsound
import colorama
from colorama import Fore, Back, Style
import time
from halo import Halo
import wikipedia
import platform
import pandas as pd
pd.set_option('display.max_colwidth', 255)
import re
from pathlib import Path
import sys
import random
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore')
from deepspeech import Model
import numpy as np
import speech_recognition as sr

sample_rate = 16000
beam_width = 500
lm_alpha = 0.75
lm_beta = 1.85
n_features = 26
n_context = 9


def main():
    subprocess.run("clear")
     #main() can be used at anytime to loopback to the beginning and start over.
    #These 3 lines specify those spinners and designs that you see during the execution
    bufferspinner = Halo(text="Analyzing", spinner='dots')
    donespinner = Halo(text="Logging Query, please wait. Saving to query.log in output directory.",text_color='green', spinner='line', color='green', animation="marquee")
    speakingspinner=Halo(text="Speaking",text_color='blue', spinner='dots', color='blue')
    searchingspinner=Halo(text="Searching",text_color='yellow', spinner='dots', color='yellow')
    #User input
    intext=input("Ask me anything: ")
    outdir="Code/"
    wordir=subprocess.run("pwd",stdout=subprocess.PIPE, text=True)
    audcache1dir= "/"+outdir+"audcache1"
    #colorama is used to change the color of the output text or stdout. This line tells it to reset the color once the line where this module is called is finished
    colorama.init(autoreset=True)
    #checks if audcache1 directory exists, kind of useless currently. Audcache1 is supposed to be the directory where the temporary wav files are stored along with the 'cached respones'.
    warnings.filterwarnings("ignore", module='bs4')
    def audcache1_check():
        if os.path.exists("/home/randomaccessvemuri/Code/audcache1")==True:
            print(Fore.GREEN+"audcache1 exists, continuing normally. Comment out the relevent print() line to prevent seeing this message.")
        if os.path.exists("/home/randomaccessvemuri/Code/audcache1")==False:
            print("please create a audcache1 directory in audio output directory")
            return()
    #audcache1_check()


    #if intext!='' and outdir!='':
    #    print("Input text not null, Directory also exists, continuing normally")
    #    elif outdir=='':
    #    print("Please set correct output directory")



    def joke_shuf():
        subprocess.run(["shuf","-n", "1", "/home/randomaccessvemuri/Code/shortjokes.csv", "-o", "/home/randomaccessvemuri/Code/shuffledjoke.csv"])
    def say_joke():
        joke_shuf()
        df = pd.read_csv("/home/randomaccessvemuri/Code/shuffledjoke.csv", usecols =[1], header = None, quotechar='"')
        df = df.astype('string')
        print(df)

    def gen_soundf(outext):
        if intext!='' and outdir!='':
            bufferspinner.start()
            subprocess.run(["tts","--text",outext,"--model_path","Models/Cortana-Test/ljspeech-ddc-May-03-2021_07+28PM-0000000/checkpoint_140000.pth.tar","--config_path", "Models/Cortana-Test/ljspeech-ddc-May-03-2021_07+28PM-0000000/config.json","--out_path",outdir], stdout=subprocess.PIPE, text=True)
            bufferspinner.stop()
            speakingspinner.start()
            playsound("/home/randomaccessvemuri/Code/output.wav")
            speakingspinner.stop()
        else:
            print(Back.RED+"FATAL:Invalid inputs, please give proper inputs")
            return()

    def audio_buffer():
        playsound("/home/randomaccessvemuri/Code/Analyzing.wav")

    def clear_terminal():
        subprocess.run("clear")

    def check_input():
        global outext
        substring="Tell me about"
        if intext in (['Who are you', 'Who are you?','introduce yourself', 'Introduce yourself.','Introduce yourself','Please introduce yourself', 'Tell me about yourself', 'Tell me about yourself.','Tell me about you', "Can you introduce yourself?","Can you introduce yourself", "can you introduce yourself", "Tell me a bit about yourself"]):
            speakingspinner.start()
            playsound("/home/randomaccessvemuri/Code/intro.wav")
            speakingspinner.stop()
            main()


        elif intext.lower().startswith('tell me about'):
            playsound("/home/randomaccessvemuri/Code/Analyzing.wav")
            wikitext = re.sub(substring, '', intext)
            searchingspinner.start()
            try:
                outext= wikipedia.summary(wikitext,sentences=3)
            except wikipedia.exceptions.DisambiguationError as e:
                outext="There are multiple pages with similar topics. Try being a bit more specific. "
                print(e.options)
            searchingspinner.stop()
            print(Fore.CYAN+Back.BLACK+outext)


        elif intext.lower().startswith('execute'):
            outext="commencing console execution, take extra care of what you speak.Enter your command and I'll pass it through to the terminal, say help to know more about preset commands. speak or type exit to exit."
            gen_soundf(outext)
            print(outext)
            command=input("Enter your command and I'll pass it through to the terminal, say help to know more about preset commands")
            if command=="update":
                subprocess.run(["sudo", "apt",'update', '&&', 'sudo', 'apt','upgrade'])
            if command=='help':
                print("update - sudo apt update && sudo apt upgrade; runs the classic update for linux")
                print("help - prints this help message")
                print("browser - opens the browser set in config.json.")
                print("python - opens python3, set the required python through source code (either python which uses python 2 or python3)")
                print("fullpower - elevates terminal and consequently your permissions to the super user or root level. NOTE: TAKE EXTRA EXTRA CARE ABOUT WHAT YOU SPEAK OR TYPE AT THIS STAGE, THERE'S A GOOD CHANCE YOU'LL SCREW UP YOUR INSTALLATION.")

        elif intext.lower() in (['tell me a joke','tell me a joke.','tell me another joke', 'tell me another joke.']):
            joke_shuf()
            df = pd.read_csv("/home/randomaccessvemuri/Code/shuffledjoke.csv", usecols =[1], header = None, quotechar='"')
            outext = df._get_value(0, 1)
            print(Fore.YELLOW+Back.BLACK+outext)

        elif intext.lower() in (['i want to know about something random', "tell me something i don't know","i want to know something new today", "tell me something random"]):
            speakingspinner.start()
            playsound("/home/randomaccessvemuri/Code/comup.wav")
            speakingspinner.stop()
            searchingspinner.start()
            para=wikipedia.random(pages=1)
            outext=wikipedia.summary(para,sentences=2)
            searchingspinner.stop()
            print(Fore.CYAN+Back.BLACK+para)
            print(Fore.CYAN+Back.BLACK+outext)




        elif intext.lower().startswith("monitor"):
            print('opening system monitor')
            outaud="Opening system monitor."
            gen_soundf(outaud)
            subprocess.run("gnome-system-monitor")
            main()
        elif intext.lower().startswith('stop'):
            exsound="Hope you come back!"
            gen_soundf(exsound)
            exit()


    def loop_input():
        global loopin
        print("Query has been saved to query.log for future reference.")
        speakingspinner.start()
        playsound("/home/randomaccessvemuri/Code/Log.wav")
        speakingspinner.stop()
        loopin=input('Anything else?')
        if loopin.lower() in (['true', 'yes', 'Yes', 'obviously', 'duh', 'Absolutely', 'I wanted to ask this one thing', 'I want ask something else', 'I want to ask something']):
            looprxn=(random.choice(["Okay.", "Go ahead.", "Alright.", "I'm listening.", "Glad to help.", "Nice talking to a curious person every once in a while!", "Splendid!"]))
            gen_soundf(looprxn)
            main()
        elif loopin in (['No.',"I think that's enough", "Nope",'no', 'No','Done']):
            looprxn=(random.choice(["Nice talking to you.", "Well, Goodbye.", "Thanks for talking.", "Hope you come back."]))
            gen_soundf(looprxn)
            print(looprxn)
            exit()
        else:
            looprxn="I'll take that as a yes."
            gen_soundf(looprxn)
            main()


    def logging(q, a):
        global f
        f=open("/home/randomaccessvemuri/Code/query.log", "a")
        f.write(q+" "+":"+" "+a+"\n")
        f.close()


    check_input()
    gen_soundf(outext)
    donespinner.start()
    time.sleep(2)
    donespinner.succeed('Done!!!')
    logging(intext,outext)
    time.sleep(1)
    clear_terminal()
    loop_input()
main()
