#    ██╗
# ██╗╚██╗
# ╚═╝ ██║
# ▄█╗ ██║
# ▀═╝██╔╝
#    ╚═╝
#
# Written by Tanmay Vemuri
from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr
wlsession = WolframLanguageSession() #Look at https://reference.wolfram.com/language/WolframClientForPython/docpages/public_api.html#cloud-api if you don't want to use offline Wolfram engine or storage/processing power is being a bottleneck
outstring = ''
listooperations = {'divided by':'/', 'by':'/','times':'*','into':'*','plus':'+','minus':'-','to the power':'^','to the power of':'^','bracket open':'(','bracket close':')'}
def voicetomath(inpstring):
    for i in listooperations:
        inpstring = inpstring.replace(i,listooperations[i])
    expression = inpstring
    return expression

def simplealgebra(inputstring):
    result = wlsession.evaluate(inputstring)
    return result



#Sample Input text = What is the value of final velocity when initial velocity equals to 5 acceleration is equal to 4

def checkinput(inpstring):
    res = inpstring.replace(" ",'')
    nums = []
    for word in inpstring.split():
       if word.isdigit():
          nums.append(int(word))
    print(nums)
#----------------------------------------------------------------------------------------------------------------------------#
    #Physics
#----------------------------------------------------------------------------------------------------------------------------#
    if 'finalvelocity' in res and 'acceleration' in res and 'initialvelocity' in res:
        valdict = {}
        quantlist = ['finalvelocity','acceleration','initialvelocity']
        for i in ['finalvelocity','acceleration','initialvelocity']:
             valdict[i] = res.find(i)
        valdict = sorted(valdict.items(), key=lambda x: x[1])
        for i in
        print("Caught")
        print(valdict)



checkinput("What is the value of final velocity when initial velocity equals to 5 acceleration is equal to 4")




















wlsession.terminate()
