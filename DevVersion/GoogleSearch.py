from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
from colorama import Fore, Back, Style
import webbrowser
import os
import random
import string
import time


session = HTMLSession()
def goog_query(inptext):
    global source2
    global soup2
    weblink = "https://www.google.com/search?q="+inptext
    source2 = session.get("https://www.google.com/search?q="+inptext).text
    soup2 = BeautifulSoup(source2, 'lxml')
    try:
        global outext
        desc2 = soup2.find('div', class_="kno-rdesc").text
        desc2 = desc2.replace("Description",'')
        desc2 = desc2.replace('Wikipedia','')
        reqkey = "rVusze"
        noofinfo=source2.count(reqkey)
        d={}
        for i in range(noofinfo):
            d[((soup2.findAll('div', class_="rVusze")[i]).text)] = i
        x = '. '.join(d)
        outext=desc2+str(x)
        outext=outext.replace(":",".")
        outext=outext.replace("Inc.","Incorporated.")
        outext=outext.replace("Pvt.","Private")
        outext=outext.replace(","," ")+"."
        outext = outext.replace("...", "")
        print(Fore.CYAN+Back.BLACK+Style.BRIGHT+desc2)
        if x!='':
            print(Fore.YELLOW+Back.BLACK+Style.BRIGHT+x+".")
        else:
            pass
    except:
        try:
            global definition
            definition=soup2.find('div', style="display:inline").text
            print(definition)
        except:
            try:
                global sometext
                sometext=soup2.find('div',class_="LGOjhe").text
                print(sometext)
            except:
                if "<table>" in soup2.text:
                    texttable = soup2.find('table')
                    textfs = texttable.find('tr')
                    textf = texttable.find('tr').text
                    textf2 = texttable.find('td').text
                    text2fs = texttable.find('td')
                    text3 = text2fs.next_sibling.text
                    text4 = text2fs.next_sibling.text
                    print(textf)
                    print(textf2+". "+str(text3))
                    print(text4)
                else:
                    global someothertext
                    someothertext = soup2.find('div', class_="IsZvec").text
                    someothertext = someothertext.replace("·",",")
                    if "..." in someothertext:
                        someothertext=someothertext.replace("...",". Learn more on their website. Opening Now. Close the browser to comeback here.")
                        soupfallback = BeautifulSoup(source2,'lxml')
                        hrefdiv = soupfallback.find("div",class_="yuRUbf")
                        hrefit = hrefdiv.find('a')['href']
                    if someothertext!='':
                        print("This is the description. "+someothertext)
                    else:
                        print("No results found, opening browser to display search results.")
                        outext="No results found. opening web browser to display search results."
                        webbrowser.open(weblink)

                    time.sleep(3)
                    try:
                        webbrowser.open(hrefit)
                    except UnboundLocalError:
                        print("Whoops, something went wrong, try again.")
import urllib.request
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False


def moon_phase():
    global source3
    global soup2
    global moonphasefinn
    global luminossityfinn
    source3 = session.get("https://www.moongiant.com/phase/").text
    soup3 = BeautifulSoup(source3, 'lxml')
    moonphase = soup3.find('td', id="today_")
    moonphasenm = moonphase.find('b')
    moonphasefin = moonphasenm.next_sibling
    moonphasefinn = moonphasefin.next_sibling
    br = moonphasefinn.next_sibling
    br1 = br.next_sibling
    br2 = br1.next_sibling.text
    luminosity = br1 + str(br2)
    luminossityfinn = luminosity.replace(":", " at")
def legal_term():
    try:
        global outext
        lower_upper_alphabet = string.ascii_letters
        random_letter = random.choice(lower_upper_alphabet)
        sourceleg = session.get("https://www.law.cornell.edu/wex/all/"+random_letter).text
        soupleg = BeautifulSoup(sourceleg, "lxml")
        randletconsq = soupleg.find('a', href='/wex/all/'+random_letter.lower())
        numberoterms = randletconsq.next_sibling
        numberoterms = numberoterms.replace(" ","")
        numberoterms = numberoterms.replace("(","")
        numberoterms = numberoterms.replace(")","")
        numberoterms = numberoterms.replace("\n","")
        numberoterms = int(numberoterms)
        termnum = random.randint(1,numberoterms-1)
        if (termnum % 2) == 0:
            classf="views-row views-row-"+str(termnum)+" views-row-even"
        if (termnum % 2) !=0:
            classf="views-row views-row-"+str(termnum)+" views-row-odd"
        terms = soupleg.find('li', class_=classf).text
        finnterm = terms.lstrip()
        finnterm = finnterm.replace(" ","_")
        sourcelegf = session.get("https://www.law.cornell.edu/wex/"+finnterm).text
        souplegf = BeautifulSoup(sourcelegf,'lxml')
        titleleg = souplegf.find('h1', class_="title").text
        desclegf = souplegf.find('div', class_="field-items").text
        desclegf=desclegf.replace("\n", '')
        desclegf = desclegf.replace("Definition from Nolo’s Plain-English Law Dictionary","Definition from Nolo’s Plain-English Law Dictionary. It means ")
        if desclegf.startswith("Definition"):
            desclegf = desclegf.replace("Definition", '')
        outext = titleleg+"\n"+desclegf
        print(Fore.CYAN+Back.BLACK+Style.BRIGHT+outext)
        outext = outext.replace(":", ".")
        outext = outext.replace("e.g.","example")
    except AttributeError:
        legal_term()
def news_search():
    global outext
    sourcenews = session.get("https://news.google.com/").text
    newssoup = BeautifulSoup(sourcenews,'lxml')
    newsline1 = newssoup.findAll('h3', class_="ipQwMb ekueJc RD0gLb")
    topheadline = newsline1[0].text
    headline1 = newsline1[1].text
    headline2 = newsline1[2].text
    headline3 = newsline1[3].text
    headline4 = newsline1[4].text
    headline5 = newsline1[5].text
    outext = (topheadline+". In other news, "+headline1+". Moving on. "+headline3+". In other breaking news, "+headline4+". Here's another headline, "+headline5+". These headlines were from Google News, for further elaboration and the full articles, visit their website.")
    outext = outext.replace(";",".")
    outext = outext.replace(":",".")
    outext = outext.replace("..",".")
    outext = outext.replace("...",".")
    outext = outext.replace("govt.","government")
    outext = outext.replace("govt","government")
    print(Fore.YELLOW+Back.BLACK+Style.BRIGHT+topheadline+"\n"+"\n"+headline1+"\n"+"\n"+headline2+"\n"+"\n"+headline3+"\n"+"\n"+headline4+"\n"+"\n"+headline5)
def facts_search():
    global outext
    randfactweb = session.get("http://randomfactgenerator.net/").text
    soup = BeautifulSoup(randfactweb, 'lxml')
    textres = soup.find('div', id='z').text
    textres = textres.replace("Tweet","")
    textres = textres.replace("\n",'')
    textres = textres.replace("...",".")
    textres = textres.replace("..",".")
    print(textres)
    outext=textres
def wiki_search(inpquery):
    print(inpquery)
    wikisearchw=session.get("https://en.wikipedia.org/w/index.php?search="+inpquery+"&go=Go&ns0=1&searchToken=83nh28uz3xgazomjm31ow4gzl").text
    soup = BeautifulSoup(wikisearchw,'lxml')
    try:
        links = soup.find('a',title="View the content page [c]")
        links = links.get('href')
        finnan = session.get("https://en.wikipedia.org"+links).text
        soupf = BeautifulSoup(finnan,'lxml')
        allofit = soup.find('div',class_="mw-parser-output")
        texts = allofit.find_all('p')
    except:
        wikisearchwn = session.get("https://en.wikipedia.org/wiki/"+inpquery).text
        soupn = BeautifulSoup(wikisearchwn,'lxml')
        allofitn = soupn.find('div',class_="mw-parser-output")
        print(allofitn)
        texts = allofitn.find_all('p')
    if any('generally refers to' in sub.text for sub in texts)==True or any('may refer to:' in sub.text for sub in texts)==True or any('may also refer to:' in sub.text for sub in texts)==True:
            print("There's multiple results for your query. here's a list of similar topics.")
            counter=0
            for i in soup.find_all('a'):
                if counter<10:
                        if i.get('title')==None:
                            pass
                        else:
                            if 'wiktionary' not in i.get('title') and 'Wikipedia' not in i.get('title'):
                                print(i.get('title'))
                                counter+=1
            finoutext="There's multiple results for your query. here's a list of similar topics."
    else:
        try:
            import regex
            outext = texts[1].text
            finnline = regex.sub(r'\([^()]*+(?:(?R)[^()]*)*+\)' , '', outext)
            finnline = regex.sub('[\(\[].*?[\)\]]' , '', finnline)
            finoutext = finnline.replace("  "," ").replace(":",'').split(".")
            finoutext = '.'.join(finoutext[0:3])
            if finoutext[-1]!='.':
                finoutext+='.'
            finoutext = finoutext.strip()
        except:
            finoutext = "Something went wrong."
    return finoutext
def wiki_random():
    randwikisource = session.get("https://en.wikipedia.org/wiki/Special:Random").text
    soup = BeautifulSoup(randwikisource,'lxml')
    texts = soup.find_all('p')
    try:
        import regex
        outext = texts[0].text+texts[1].text+texts[2].text
        finnline = regex.sub(r'\([^()]*+(?:(?R)[^()]*)*+\)' , '', outext)
        finnline = regex.sub('[\(\[].*?[\)\]]' , '', finnline)
        finoutext = finnline.replace("  "," ").replace(":",'').split(".")
        finoutext = '.'.join(finoutext[0:4])
        finoutext = finoutext.strip()
        if finoutext=='':
            wiki_random()
        if finoutext[-1]!='.':
            finoutext+='.'
        print(Fore.CYAN+Back.BLACK+finoutext)
        return finoutext
    except:
        if connect()==True:
            wiki_random()
