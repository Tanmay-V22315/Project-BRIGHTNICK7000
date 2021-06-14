#    ██╗
# ██╗╚██╗
# ╚═╝ ██║
# ▄█╗ ██║
# ▀═╝██╔╝
#    ╚═╝
#
# Written by Tanmay Vemuri
# Handler 1:
#     Get input
#     Clean input
#     Get answer from SemanticInterpretation (Wolfram)
#       If not possible: Ask if question is math or science related
#           Yes: Proceed with Next Handler
#           No: Search for proper noun using nltk tokenization and spacy and find information in wikipedia or on Google.
#               #Ask "is this what you wanted to know about?":
#                   If yes:
#                       loopback to main() in main BRIGHTNICK7000 file
#                   If No:
#                       ask user to specify term and search for that term in wikipedia and google
#       If possible:
#           proceed forward
#     Get type of Entity
#     Ask if detailed report to be generated
#     If yes:
#         Based on Entity name and type, search wikipedia and google and obtain all the info, obtain dataset using Wolfram SemanticInterpretation.
#           1. Obtain data from wolfram, clean it and export in the form of .xlsx
#              1. Remove images
#              2. Remove Lines (Plotted lines)
#              3. Remove Figures
#              4. Remove data that is too long
#           2. Convert generated xlsx into a dataframe using pandas
#           3. Remove Elements towards the end based on getrep from config.json
#           3. Get information from Google search and append it to dataframe
#           4. Get info from wikipedia, summarise it using summarizer, append it to dataframe
#           5. create a tempfile, convert dataframe to html and write to tempfile
#           6. Display HTML file using webbrowser
#     If no:
#         Proceed with looping Main() in main BRIGHTNICK7000 file
#         Break Handler 1
# Handler 2:
#     For Mathematics and Physics (Involving solvation of numerical data):
#     Check if math or physics or economics related:
#        1.Detect presence of operators in words (Like 'plus','minus','divided by' or simply 'by' or variables like 'x' or words like solve. )
#        2. Check for quantities like Acceleration, ampere, metres per second etc.
#        3. Based on input to 3.1 in Handler 1, init Handler 2.
#     Specify whether physics or math or economics:
#       If physics:
#           1. Get quantities from user, individually (Special case: Vectors, Plotting)
#           2. Ask which one to be derived.
#           3. If User wants to know about Formulas itself:
#                use mathtostring() to convert input form of required formula from wolfram to human readable form.
#           4. For vectors, during input for quantities, make the user mention vectors in some form or other for example: "I would like to work with vectors"
#     WIP (I'm still working from here on)


import os

from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr
wlsession = WolframLanguageSession()
import nltk
from nltk.corpus import stopwords
from word2number import w2n
import spacy
import en_core_web_sm
from pprint import pprint
from spacy import displacy
import regex

nlp = en_core_web_sm.load()
# semantics =
#Sample Question: "What is the final velocity of an object with acceleration 45 metres per second squared time of 4 seconds and initial velocity of 0 metres per second"
# def xlsxtotable
stopwords = stopwords.words('english')
def inputcleanup(somstring):
    finstring = somstring
    xlist = finstring.split()
    for i in xlist:
        try:
            i = w2n.word_to_num(i)
        except:
            pass
    print(xlist)
    finstring = " ".join(xlist)
    finstring = str(finstring)
    finnline = regex.sub(r'\([^()]*+(?:(?R)[^()]*)*+\)' , '', finstring)
    finnline = regex.sub('[\(\[].*?[\)\]]' , '', finnline)
    finoutext = finnline.replace("  "," ").replace(":",'').split(".")
    finoutext = '.'.join(finoutext[0:])
    finstring = finoutext.strip()
    finstring = nltk.word_tokenize(finstring)
    finanslist = []
    for i in finstring:
        if i not in stopwords:
            finanslist.append(i)
    finanslist = ' '.join(finanslist)
    print(finanslist)
    return finanslist


def getwolfram(cleanedtext):
        query = 'SemanticInterpretation['+'"'+str(cleanedtext)+'"'+']'
        x = wlsession.evaluate_wrap(wlexpr(query))
        print(x.name)
        print(type(x))


print(getwolfram(inputcleanup(input("What do you want to ask?: "))))

wlsession.terminate()


# def typechecker(question):
