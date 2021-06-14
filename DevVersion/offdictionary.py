#    ██╗
# ██╗╚██╗
# ╚═╝ ██║
# ▄█╗ ██║
# ▀═╝██╔╝
#    ╚═╝
#
# Written by Tanmay Vemuri
from nltk.corpus import wordnet as wn
def wmeaning(querword):
    meansynset = wn.synsets(querword)
    try:
        meaningw = "The meaning of "+querword+" is "+meansynset[0].definition()
        if meaningw[-1]!='.':
            meaningw=meaningw+'.'
        if (meansynset[0].examples())!=[]:
            meaningw+=". An example is "+str(meansynset[0].examples()).replace("[",'').replace("]",'')+"."
    except:
        meaningw="I couldn't find the meaning of your desired word."
    return meaningw
def wsynonym(queryword):
    synonyms = []

    for syn in wn.synsets(queryword):
    	for l in syn.lemmas():
    		synonyms.append(l.name())

    if len(synonyms)!=0:
        synonymsf=list(set(synonyms))
        outname=''
        counter=0
        for i in synonymsf:
            i=i.replace("_"," ")
            if i not in outname:
                if i!=synonymsf[-1]:
                    outname = outname+i+","
                else:
                    outname = outname+i+"."
        outname="The synonym for "+queryword+" are "+outname+' These might be inaccurate or not what you expect.'
    else:
        outname="I couldn't find any synonyms."


def wantonym(queryword):
    antonyms = []
    for syn in wn.synsets(queryword):
        for l in syn.lemmas():
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())

    if len(antonyms)!=0:
        antonymsf=list(set(antonyms))
        outname=''
        counter=0
        for i in antonymsf:
            i=i.replace("_"," ")
            if i not in outname:
                if i!=antonymsf[-1]:
                    outname = outname+i+","
                else:
                    outname = outname+i+"."




        outname="The antonym is "+outname+' It might be inaccurate or not what you expect.'
    else:
        outname="I couldn't find any antonyms."
    return outname
