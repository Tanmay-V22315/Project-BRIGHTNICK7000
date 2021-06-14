#    ██╗
# ██╗╚██╗
# ╚═╝ ██║
# ▄█╗ ██║
# ▀═╝██╔╝
#    ╚═╝
#
# Written by Tanmay Vemuri
import spacy
from spacy import displacy
from collections import Counter
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from pprint import pprint
import warnings
import en_core_web_sm
import sys
import regex
from summarizer import summarizer
nlp = en_core_web_sm.load()
session = HTMLSession()
warnings.filterwarnings('ignore')
# f=open("/home/randomaccessvemuri/Code/query.log", "a")
# f.write("\n Hello")
# f.close()
print()
print()
print()
try:
    input("Warning: During training, the CPU usage will be pretty high as well as memory usage, and network usage and also possibly storage. Take heed of what you're doing. Press CTRL+C to cancel. If you want to begin training from a certain topic,A Function call has been commented appropriately, change that to start from you preferred topic. Press ENTER to continue ")
except KeyboardInterrupt:
    print()
    print()
    print()
    sys.exit("Understood, Have a great day!")

Question = []

doc = 'The People’s Alliance for Gupkar Declaration (PAGD) has not changed its position on the abrogation of Article 370 and bifurcation of the erstwhile state.'
maxterm = input("Maximum number of terms? (Recommended: 50), if not specified, will check for all possible ones.(Can reach upto 1000)")

listent = []
def initlayergen(somstring):
    somstring = nlp(somstring)
    print("Proper nouns and relevant entities found: ")
    pprint([(X.text, X.label_) for X in somstring.ents])
    initlist = ([(X.text, X.label_) for X in somstring.ents])
    return initlist
def layergen(somstring):
    somstring = nlp(somstring)
    pprint([(X.text, X.label_) for X in somstring.ents])
    for abc in ([(X.text, X.label_) for X in somstring.ents]):
        listent.append(abc)
    return listent


def wiki_search(inpquery):
    wikisearchw=session.get("https://en.wikipedia.org/w/index.php?search="+inpquery+"&go=Go&ns0=1&searchToken=83nh28uz3xgazomjm31ow4gzl").text
    soup = BeautifulSoup(wikisearchw,'lxml')
    links = soup.find('a',title="View the content page [c]")
    links = links.get('href')
    finnan = session.get("https://en.wikipedia.org"+links).text
    soupf = BeautifulSoup(finnan,'lxml')
    texts = soupf.find_all('p')
    textfin = ''
    for i in texts:
        textfin+=i.text
    finnline = regex.sub(r'\([^()]*+(?:(?R)[^()]*)*+\)' , '', textfin)
    finnline = regex.sub('[\(\[].*?[\)\]]' , '', finnline)
    finoutext = finnline.replace("  "," ").replace(":",'').split(".")
    finoutext = '.'.join(finoutext[0:])
    finoutext = finoutext.strip()
    return finoutext

initlayer = initlayergen(wiki_search("DOOM 2016")) #Use Special:Random for beginning from random topic. Change this to start from a specific topic.
if maxterm!='':
    initlayer = initlayer[0:int(maxterm)]

finlist = []
alltexts = []
counter = 0
searched = []
for i in initlayer:
    finlist.append(i)
    QuestionsList = ["Who is", "What is","What is the","Who is the","How is"]
    if i[1] not in ["DATE","ORDINAL","MONEY","CARDINAL", "QUANTITY","PERCENT"]:
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Exploring: "+str(i[0]))
        try:
            if i[0] not in searched:
                searched.append(i[0])
                fulltext = wiki_search(i[0])
                finnline = regex.sub(r'\([^()]*+(?:(?R)[^()]*)*+\)' , '', fulltext)
                finnline = regex.sub('[\(\[].*?[\)\]]' , '', finnline)
                finoutext = finnline.replace("  "," ").replace(":",'').split(".")
                finoutext = '.'.join(finoutext[0:])
                finoutext = finoutext.strip()
                finoutext.encode("ascii", "ignore")
                print("Length of Text Before Summarizing: "+str(len(finoutext)))
                print("Summarizing")
                finoutext = summarizer(finoutext)
                print("Length of Text After Summarizing: "+str(len(finoutext)))
                print("Deducing Proper Nouns and entities from Text.")
                layergen(finoutext)
                alltexts.append(fulltext)
                print("Done")
            else:
                print("Already Checked, Moving on.")
        except KeyboardInterrupt:
            print("Okay!")
            break
        except:
            print("Failed. Moving On.")
            pass
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
import time

print("Initial Dataset Formed")
finlist = list(set(listent))

for i in finlist:
    if i[1] in ["DATE","ORDINAL","MONEY","CARDINAL", "QUANTITY","PERCENT"]:
        del finlist[finlist.index(i)]
fincomp = []
for i in alltexts:
    i=i.replace("\n"," . ")
    fincomp.append(i.rstrip("\n"))
