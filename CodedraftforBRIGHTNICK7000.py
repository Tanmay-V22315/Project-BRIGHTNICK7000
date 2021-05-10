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
import re
from pathlib import Path
import sys
import random

def main():

    bufferspinner = Halo(text="Analyzing", spinner='dots')
    donespinner = Halo(text="Done!!",text_color='green', spinner='dots', color='green')
    speakingspinner=Halo(text="Speaking",text_color='blue', spinner='dots', color='blue')

    intext=input("Ask me anything: ")
    outdir="Code/"
    wordir=subprocess.run("pwd",stdout=subprocess.PIPE, text=True)
    audcache1dir= "/"+outdir+"audcache1"

    colorama.init(autoreset=True)

    def audcache1_check():
        if os.path.exists("/home/randomaccessvemuri/Code/audcache1")==True:
            print(Fore.GREEN+"audcache1 exists, continuing normally. Comment out the relevent print() line to prevent seeing this message.")
        if os.path.exists("/home/randomaccessvemuri/Code/audcache1")==False:
            print("please create a audcache1 directory in audio output directory")
            return()
    audcache1_check()


    if intext!='' and outdir!='':
        print("Input text not null, Directory also exists, continuing normally")
    elif outdir=='':
        print("Please set correct output directory")


    def gen_soundf(outext):
        if intext!='' and outdir!='':
            bufferspinner.start()
            subprocess.run(["tts","--text",outext,"--model_path","Models/Cortana-Test/ljspeech-ddc-May-03-2021_07+28PM-0000000/checkpoint_140000.pth.tar","--config_path", "Models/Cortana-Test/ljspeech-ddc-May-03-2021_07+28PM-0000000/config.json","--out_path", outdir ], stdout=subprocess.PIPE, text=True)
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
            playsound("/home/randomaccessvemuri/Code/intro.wav")
            main()
        elif intext.lower().startswith('tell me about'):
            wikitext = re.sub(substring, '', intext)
            outext= wikipedia.summary(wikitext,sentences=2)
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
        elif intext.lower().startswith('System monitor'):
            print('opening ')
        elif intext.lower().startswith('stop'):
            exsound="Hope you comeback!"
            gen_soundf(exsound)
            exit()
        else:
            print("echoing input")
            outext="echoing input."+" "+intext

    def loop_input():
        global loopin
        loopin=input('Anything else? Query has been saved to relevant logs.')
        if loopin in (['true', 'yes', 'Yes', 'obviously', 'duh', 'Absolutely', 'I wanted to ask this one thing', 'I want ask something else', 'I want to ask something']):
            looprxn=(random.choice(["Okay.", "Go ahead.", "Alright.", "I'm listening.", "Glad to help.", "Nice talking to a curious person every once in a while!", "Splendid!"]))
            gen_soundf(looprxn)
            main()
        if loopin in (['No.',"I think that's enough", "Nope",'no', 'No','Done']):
            looprxn=(random.choice(["Nice talking to you.", "Well, Goodbye.", "Thanks for talking.", "Hope you come back."]))
            gen_soundf(looprxn)
            print(looprxn)
            exit()

    check_input()
    gen_soundf(outext)
    donespinner.start()
    time.sleep(2)
    donespinner.succeed('Done!!!')
    time.sleep(1)
    clear_terminal()
    loop_input()
main()
