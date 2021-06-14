import time


def get_time():
    localtime = time.localtime(time.time())
    hour=localtime[3:4]
    for i in hour:
        global hourf
        hourf=(i)
    minute = localtime[4:5]
    for i in minute:
        global minutef
        minutef = (i)

    if hourf > 5 and hourf < 7:
        stat = " at dawn."
    elif hourf > 19 and hourf < 6:
        stat = " at night."
    elif hourf > 7 and hourf < 12:
        stat = " in the morning."
    elif hourf >11 and hourf < 3:
        stat = " in the afternoon."
    else:
        stat = " in the evening."

    if hourf > 12:
        hourf = hourf-12


    if minutef == 0:
        global outext
        outext = "It is "+str(hourf) +"O'clock" +stat
        print(outext)
        outext = outext.replace("O'","O")
    else:
        outext = "It is "+str(hourf)+ ":"+str(minutef)+stat
        print(outext)
        outext = outext.replace(":"," ")
