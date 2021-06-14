from PyDictionary import PyDictionary
dictionary=PyDictionary()



def dict_search(dictquery):
    try:
        global repla
        global dictodict
        global listodict
        global outext
        global outext1
        dictodict=(dictionary.meaning(dictquery))
        listodict=list(dictodict.items())[0][1]
        repla='. '
        outext=repla.join(listodict)
    except AttributeError:
        outext="that word is not in my dictionary or something went wrong, try avoiding certain proper nouns like Logitech or Lenovo or make sure your query doesn't have a period at the end."
        print(outext)


def dict_synonym(synquery):
    global repla
    global listo
    global outext
    listo=(dictionary.synonym(synquery))
    repla='. '
    outext=repla.join(listo)+"."

def dict_antonym(anquery):
    global repla
    global listo
    global outext
    listo=(dictionary.antonym(anquery))
    repla='. '
    outext=repla.join(listo)+"."
