#    ██╗
# ██╗╚██╗
# ╚═╝ ██║
# ▄█╗ ██║
# ▀═╝██╔╝
#    ╚═╝
#
# Written by Tanmay Vemuri
#This currently won't work on its own, it requires other python files (And a lot of dependencies as well)
#Importing necessary modules
print("Importing Modules...")
import time
import hjson
import json
f = open('Code/config.json',) #Write the directory of your config.json
data = hjson.load(f)
if data["showconfig"]==True:
    print("Using the following configuration, change config.json file that comes with this project to change the values, if in case you encounter an error or want to change something to your preferences.")
    for i in data:
        print(str(i)+' : '+str(data[i]))
time.sleep(2)
import os
import subprocess
from playsound import playsound
import colorama
from colorama import Fore, Back, Style
from halo import Halo
import pandas as pd
pd.set_option('display.max_colwidth', 255)
import random
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore')
import vosk
import sys
import voskTest as inp
import argparse
import offdictionary as offdict
import GoogleSearch as searchg
import weather
import gettime as gt
print("Done!!")
time.sleep(1)
initspinner = Halo(text="Initializing: ", spinner='dots', color='green', text_color = 'green')
print(Fore.GREEN+'''
██████╗░██████╗░██╗░██████╗░██╗░░██╗████████╗███╗░░██╗██╗░█████╗░██╗░░██╗░░░░░░███████╗░█████╗░░█████╗░░█████╗░
██╔══██╗██╔══██╗██║██╔════╝░██║░░██║╚══██╔══╝████╗░██║██║██╔══██╗██║░██╔╝░░░░░░╚════██║██╔══██╗██╔══██╗██╔══██╗
██████╦╝██████╔╝██║██║░░██╗░███████║░░░██║░░░██╔██╗██║██║██║░░╚═╝█████═╝░█████╗░░░░██╔╝██║░░██║██║░░██║██║░░██║
██╔══██╗██╔══██╗██║██║░░╚██╗██╔══██║░░░██║░░░██║╚████║██║██║░░██╗██╔═██╗░╚════╝░░░██╔╝░██║░░██║██║░░██║██║░░██║
██████╦╝██║░░██║██║╚██████╔╝██║░░██║░░░██║░░░██║░╚███║██║╚█████╔╝██║░╚██╗░░░░░░░░██╔╝░░╚█████╔╝╚█████╔╝╚█████╔╝
╚═════╝░╚═╝░░╚═╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚══╝╚═╝░╚════╝░╚═╝░░╚═╝░░░░░░░░╚═╝░░░░╚════╝░░╚════╝░░╚════╝░

Initializing, Please wait. Until then, check out what I can do for you, here:''')
print(Back.BLACK+Fore.CYAN+"https://github.com/Tanmay-V22315/Project-BRIGHTNICK7000/blob/main/README.md")
print()
print()
def systemscheck():
    initspinner.start()
    print()
    print("Initializing Text-To-Speech")
    subprocess.run(["tts","--text","Random text for Primer.","--model_path",data['ttsmodeldir'],"--config_path", "Models/Cortana-Test/ljspeech-ddc-May-03-2021_07+28PM-0000000/config.json","--out_path",data['dir']], stdout=subprocess.PIPE, text=True)
    print("Done!")
    print("Initializing Automatic-Speech-Recognition: ")
    inp.test_input()
    print("Done!")
    print("Initializing WolframEngine: ")
    try:
        from wolframclient.evaluation import WolframLanguageSession
        from wolframclient.language import wl, wlexpr
        wlsession = WolframLanguageSession()
        wlsession.evaluate(wlexpr('SemanticInterpretation["Dataset for Earth"]'))
    except:
        print("You will have to be online in order to make full use of SemanticInterpretation in Wolfram. You can still input the commands in Wolfram Language vocally.")
    print("Done!")
    print("Initializing NLP modules: ")
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    import nltk
    from nltk.corpus import stopwords
    from word2number import w2n
    import spacy
    import en_core_web_sm
    from pprint import pprint
    from spacy import displacy
    import regex
    nlp = en_core_web_sm.load()
    initspinner.stop()
systemscheck()

def main():
    bufferspinner = Halo(text="Analyzing", spinner='dots')
    donespinner = Halo(text="Logging Query, please wait. Saving to query.log in output directory.",text_color='green', spinner='line', color='green', animation="marquee")
    speakingspinner=Halo(text="Speaking",text_color='blue', spinner='dots', color='blue')
    searchingspinner=Halo(text="Searching",text_color='yellow', spinner='dots', color='yellow')
    listenspinner=Halo(text="Listening, Go ahead", text_color='cyan',spinner='dots',color='cyan')
    waitspinner=Halo(text="Wait", text_color='grey', spinner='line', color="grey")

    subprocess.run("clear")
    def openinputstream():
        listenspinner.start()
        inp.take_input()
        inp.conv_to_usable()
        print(inp.inputst['text'])
        listenspinner.stop()
    openinputstream()
    if inp.inputst['text']=='':
        print("Sorry, Didn't quite catch that, try again. try emphasizing on your query by talking slower and with longer pauses.")
        time.sleep(1)
        main()
    else:
        global intext
        intext=inp.inputst['text']+"."
        intext=intext.lower()
    outdir=data['dir']
    audcache1dir= "/"+outdir+"audcache1"
    colorama.init(autoreset=True)
    warnings.filterwarnings("ignore", module='bs4')
    def joke_shuf():
        subprocess.run(["shuf","-n", "1", "/home/randomaccessvemuri/Code/shortjokes.csv", "-o", "/home/randomaccessvemuri/Code/shuffledjoke.csv"])
    def quote_fin():
        subprocess.run(["shuf","-n", "1", "/home/randomaccessvemuri/Code/Quotes.csv", "-o", "/home/randomaccessvemuri/Code/shuffledquote.csv"])
        global outext
        outext = pd.read_csv("/home/randomaccessvemuri/Code/shuffledquote.csv", usecols =[0,1], header = None, quotechar='"',delimiter=';')
        outext = outext.astype('string')
        outext = outext._get_value(0,0)+" "+outext._get_value(0,1)
        print(outext)
    def say_joke():
        joke_shuf()
        df = pd.read_csv("/home/randomaccessvemuri/Code/shuffledjoke.csv", usecols =[1], header = None, quotechar='"')
        df = df.astype('string')
        print(df)

    def gen_soundf(outext):
        if intext!='' and outdir!='':
            bufferspinner.start()
            subprocess.run(["tts","--text",outext,"--model_path",data['ttsmodeldir'],"--config_path", "Models/Cortana-Test/ljspeech-ddc-May-03-2021_07+28PM-0000000/config.json","--out_path",outdir], stdout=subprocess.PIPE, text=True)
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
        if intext=="stop." or 'stop' in intext:
            print("pausing for 10 seconds")
            outext="pausing for 10 seconds."
            gen_soundf(outext)
            time.sleep(data['sleeptime'])
            main()


        elif intext in (['who are you', 'who are you.', 'introduce yourself.','introduce yourself','please introduce yourself', 'tell me about yourself.','tell me about you.', "can you introduce yourself.", "tell me a bit about yourself", "Tell me something about yourself"]):
            print(Back.BLACK+Fore.CYAN+"I am BrightNick, part of project BRIGHTNICK7000, I'll be your home assistant and the guide for this tour. I'm based on the now popular science fiction super computer and am supposed to be considered as a predecessor to one of the most popular and beloved fictional super computer, HAL 9000. HAL 9000 itself is a successor of ILLIAC, so I sit somewhere in between them as an intermiediate. My name comes from the fusion of the names Daniel Slotnick, the person who pioneered the ILLIAC machine and Kevan brighting, whose voice was used for this model. There's also a cortana version but all of them fall under the umbrella of Project BRIGHTNICK 7000.")
            speakingspinner.start()
            playsound("/home/randomaccessvemuri/Code/intro.wav")
            speakingspinner.stop()
            main()



        elif "weather" in intext.lower():
            searchingspinner.start()
            weather.check_weather(data['cityName'])
            searchingspinner.stop()
            outext=weather.outext
            print(Fore.CYAN+Back.BLACK+outext)


        elif "fun fact" in intext or intext=="tell me something fun." or intext=="tell me a fact." or "interesting fact" in intext:
            searchg.facts_search()
            outext = searchg.outext

        elif intext.lower().startswith('tell me about'):
            playsound("/home/randomaccessvemuri/Code/Analyzing.wav")
            newtext = intext.lower()
            repltext = newtext.replace('tell me about','').replace('.','')
            wikitext=repltext.lstrip()
            # try:
            searchingspinner.start
            print()
            outext = searchg.wiki_search(wikitext)
            print(Fore.CYAN+Back.BLACK+outext)
            searchingspinner.stop()
            # except:
            #     outext = "Something went wrong. Change your search term or try again."
            #     print(outext)


        elif intext.lower().startswith('tell me something about'):
            playsound("/home/randomaccessvemuri/Code/Analyzing.wav")
            newtext = intext.lower()
            repltext = newtext.replace('tell me something about','')
            wikitext=repltext.title()
            # try:
            searchingspinner.start
            print()
            print(wikitext)
            outext = searchg.wiki_search(wikitext)
            print(Fore.CYAN+Back.BLACK+outext)
            searchingspinner.stop()
            # except:
            #     outext = "Something went wrong. Change your search term or try again."
            #     print(outext)

        elif intext=='can you repeat what i say.':
            gen_soundf("Do you really like my voice that much? For you, anything.")
            inptest=input("What should I say?")
            outext=inptest

        elif "news" in intext:
            searchg.news_search()
            outext=searchg.outext

        elif intext.lower().startswith('execute'):
            try:
                outext = searchg.wiki_search(wikitext)
                print(outext)
            except:
                outext = "Something went wrong. Change your search term or try again."
                print(outext)
            outext="commencing console execution, take extra care of what you speak.Enter your command and I'll pass it through to the terminal, say help to know more about preset commands. speak or type exit to exit."
            gen_soundf(outext)
            print(outext)
            command=input("Enter your command and I'll pass it through to the terminal, say help to know more about preset commands")
            if command=="update":
                subprocess.run(["sudo", "apt",'update', '&&', 'sudo', 'apt','upgrade'])
            if command=="exit":
                main()
            if command=='help':
                print("update - sudo apt update && sudo apt upgrade; runs the classic update for linux")
                print("help - prints this help message")
                print("browser - opens the browser set in config.json.")
                print("python - opens python3, set the required python through source code (either python which uses python 2 or python3)")
                print("unlimitedpower - elevates terminal and consequently your permissions to the super user or root level. NOTE: TAKE EXTRA EXTRA CARE ABOUT WHAT YOU SPEAK OR TYPE AT THIS STAGE, THERE'S A GOOD CHANCE YOU'LL SCREW UP YOUR INSTALLATION.(Also, Star wars Meme)")

        elif intext.lower() in (['tell me a joke','tell me a joke.','tell me another joke', 'tell me another joke.']):
            joke_shuf()
            df = pd.read_csv("/home/randomaccessvemuri/Code/shuffledjoke.csv", usecols =[1], header = None, quotechar='"')
            outext = df._get_value(0, 1)
            print(Fore.YELLOW+Back.BLACK+outext)



        elif intext.lower() in (['i want to know about something random.', "tell me something i don't know.","i want to know something new today.", "tell me something random.","tell me something random."]):
            speakingspinner.start()
            playsound("/home/randomaccessvemuri/Code/comup.wav")
            speakingspinner.stop()
            searchingspinner.start()
            outext = searchg.wiki_random()
            searchingspinner.stop()
            print(Fore.CYAN+Back.BLACK+outext)




        elif intext.lower().startswith("what is the meaning of"):
            global inpquer
            global inpuquera
            global inpquerf
            inpquera=intext.lower()
            inpquer=inpquera.replace('.','')
            inpquerf=inpquer.replace("what is the meaning of",'').lstrip()
            outext =offdict.wmeaning(inpquerf)
            if '..' in outext:
                outext=outext.replace("..",'.')
            print(Fore.YELLOW+Back.BLACK+outext)
            if "'" in outext:
                outext = outext.replace("'",'')


        elif "what" in intext.lower() and "time" in intext.lower():
            gt.get_time()
            outext = gt.outext


        elif intext.lower() in (["i don't feel very motivated today.","tell me a quote.", 'i want some inspiration today.', 'i want to be inspired.', 'i want to know something profound.',"i don't feel motivated today."]):
            quote_fin()
            outext=outext.replace("...",".")
            outext=outext.replace(";",",")


        elif "legal term" in intext or "legal word" in intext:
            searchg.legal_term()
            outext = searchg.outext


        elif 'word' in intext and 'similar to' in intext:
            global synquer
            global synquera
            global synquerf
            synquera=intext.lower()
            synquer=synquera.replace('.','')
            synquerf = synquer.split()[-1]
            print(synquerf)
            outext = offdict.wsynonym(synquerf)
            print(Fore.YELLOW+Back.BLACK+outext)

        elif intext.lower().startswith("which word is opposite of"):
            global anquer
            global anquera
            global anquerf
            anquera=intext.lower()
            anquer=anquera.replace('.','')
            anquerf=anquer.replace("which word is opposite of",'').lstrip()
            print(anquerf)
            offdict.wantonym(anquerf)
            outext=offdict.wantonym(anquerf)
            print(Fore.YELLOW+Back.BLACK+outext)


        elif "system monitor" in intext or "task manager" in intext:
            print('Opening system monitor for 10 seconds')
            outaud="Opening system monitor."
            gen_soundf(outaud)
            #subprocess.run("bpytop")
            #subprocess.run(["sleep","10"])
            pid = _job_pid(bashtop)
            print(pid)
            exit()
            os.kill("bashtop")
            subprocess.run(["kill","-2",])
            main()

        elif intext.lower().startswith('exit'):
            exsound="Hope you come back!"
            gen_soundf(exsound)
            exit()

        else:
            searchg.goog_query(intext)
            outext=searchg.outext


    def loop_input():
        global loopin
        print("Query has been saved to query.log for future reference.")
        speakingspinner.start()
        playsound("/home/randomaccessvemuri/Code/Log.wav")
        speakingspinner.stop()
        loopinputext = openinputstream()
        if loopinputext['text']=='':
            print("Sorry, Didn't quite catch that, Try speaking a little louder and with some pauses.")
            time.sleep(1)
            loop_input()
        else:
            global intext2
            intext2=loopinputext

        loopin=intext2
        if loopin.lower() in (['true.', 'yes.', 'obviously.', 'duh.', 'absolutely.', 'i wanted to ask this one thing.', 'i want to ask something else.', 'i want to ask something.']):
            looprxn=(random.choice(["Okay.", "Go ahead.", "Alright.", "I'm listening.", "Glad to help.", "Nice talking to a curious person every once in a while!", "Splendid!", "Go on."]))
            gen_soundf(looprxn)
            main()
        elif loopin.lower() in (['no.',"i think that's enough", "nope",'no','done',"that's all","false", "enough"]):
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

    try:
        check_input()
        gen_soundf(outext)
        donespinner.start()
        time.sleep(2)
        donespinner.succeed('Done!!!')
        logging(intext,outext)
        time.sleep(1)
        clear_terminal()
        main()
    except KeyboardInterrupt:
        print()
        print(Fore.RED+Back.BLACK+"Wow, Okay! Kinda rude.")
        exit()
try:
    main()
except:
    wlsession.terminate()
