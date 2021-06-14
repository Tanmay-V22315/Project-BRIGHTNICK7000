import weathercom
import json
import time
import GoogleSearch

def check_weather(location):
    localtime = time.localtime(time.time())
    hour=localtime[3:4]
    for i in hour:
        global hourf
        hourf=(i)


    minute=localtime[4:5]
    for i in minute:
        global minutef
        minutef=(i)


    weather = weathercom.getCityWeatherDetails(location)
    weatherjson=json.loads(weather)

    cityn = (weatherjson['city'])

    temp=(weatherjson["vt1observation"]["temperature"])

    felttemp=(weatherjson["vt1observation"]["feelsLike"])

    status=(weatherjson["vt1observation"]["phrase"])

    uvindex=(weatherjson["vt1observation"]["uvIndex"])

    if (weatherjson["vt1observation"]["windSpeed"]) <= 5:
        windspeed="The air is quite still with wind speeds of about "+str((weatherjson["vt1observation"]["windSpeed"]))+" kilometres per hour."
    elif (weatherjson["vt1observation"]["windSpeed"]) > 5 and (weatherjson["vt1observation"]["windSpeed"]) <= 11:
        windspeed="There's a light breeze with wind speeds about "+str((weatherjson["vt1observation"]["windSpeed"]))+" kilometres per hour."
    elif (weatherjson["vt1observation"]["windSpeed"]) > 11 and (weatherjson["vt1observation"]["windSpeed"]) <=19:
        windspeed="There's a gentle breeze with wind speeds about "+str((weatherjson["vt1observation"]["windSpeed"]))+" kilometres per hour."
    elif (weatherjson["vt1observation"]["windSpeed"]) > 20 and (weatherjson["vt1observation"]["windSpeed"]) <= 29:
        windspeed="There's a moderate breeze with wind speeds about "+str((weatherjson["vt1observation"]["windSpeed"]))+" kilometres per hour."
    elif (weatherjson["vt1observation"]["windSpeed"]) > 30 and (weatherjson["vt1observation"]["windSpeed"]) <= 39:
        windspeed="There's a strong breeze with wind speeds about "+str((weatherjson["vt1observation"]["windSpeed"]))+" kilometres per hour."
    elif (weatherjson["vt1observation"]["windSpeed"]) > 40 and (weatherjson["vt1observation"]["windSpeed"]) <= 50:
            windspeed="There's a moderate gale with wind speeds about "+str((weatherjson["vt1observation"]["windSpeed"]))+" kilometres per hour."
    elif (weatherjson["vt1observation"]["windSpeed"]) > 51 and (weatherjson["vt1observation"]["windSpeed"]) <= 61:
            windspeed="There's a fresh gale with wind speeds about "+str((weatherjson["vt1observation"]["windSpeed"]))+" kilometres per hour."
    elif (weatherjson["vt1observation"]["windSpeed"]) > 62 and (weatherjson["vt1observation"]["windSpeed"]) <= 74:
            windspeed="There's a strong gale with wind speeds about "+str((weatherjson["vt1observation"]["windSpeed"]))+" kilometres per hour."
    elif (weatherjson["vt1observation"]["windSpeed"]) > 75 and (weatherjson["vt1observation"]["windSpeed"]) <= 87:
            windspeed="There's a whole gale with wind speeds about "+str((weatherjson["vt1observation"]["windSpeed"]))+" kilometres per hour."
    elif (weatherjson["vt1observation"]["windSpeed"]) > 75 and (weatherjson["vt1observation"]["windSpeed"]) <= 87:
            windspeed="Just look out of the window! You have been sleeping through wind speeds about"+weatherjson["vt1observation"]["windSpeed"]+"! Maybe you should start to work on your habits once you get out of this storm!"

    if uvindex >= 0 and uvindex <= 2 and hourf >= 6 and hourf <= 18:
        uvindmes="The sun is quite peaceful today. The UV index is "+str(uvindex)+"."
    elif uvindex >= 3 and uvindex <= 5 and hourf >= 6 and hourf <= 18:
        uvindmes="The sun feels quite brisk and cozy today. The UV index is "+str(uvindex)+"."
    elif uvindex >= 6 and uvindex <= 8 and hourf >= 6 and hourf <= 18:
        uvindmes="The sun is starting to get a bit angry now. Put on some low SPF sunscreen, you'll be fine. The UV index is "+str(uvindex)+"."
    elif uvindex >= 9 and uvindex <= 11 and hourf >= 6 and hourf <= 18:
        uvindmes="The sun is really angry now. Don't go out unless you absolutely have to. Put on some sunscreen if you do. The UV index is "+str(uvindex)+"."
    elif uvindex >= 11 and hourf >= 6 and hourf <= 18:
        uvindmes="just don't go out! There's a very high chance you'll develop skin cancer or other diseases. The UV index is "+str(uvindex)+"."
    elif hourf <= 6:
        uvindmes="It's dawn or around midnight. the UV index is "+str(uvindex)+"."
    elif hourf >= 18:
        uvindmes="It's night time or dusk. The UV index is "+str(uvindex)+"."

    skystat="The sky is "+status+"."


    if status=="Sunny" and hourf > 18 or hourf < 7:
        skystat = "The sky is clear and pleasant."

    if hourf > 18 or hourf < 7:
        if hourf > 12:
            hourf = hourf-12
        GoogleSearch.moon_phase()
        skystat = skystat+"It is night time at "+str(hourf)+". "+str(minutef)+". The moon phase is " +(GoogleSearch.moonphasefinn)+"with "+GoogleSearch.luminossityfinn+"."
    else:
        skystat+". The time is "+str(hourf)+"."
    if status.lower()=="thunderstorm":
        skystat = "There's  a thunderstorm going on. Don't go out unless you absolutely have to. Make sure your cars and vehicles aren't under trees and take other such precautions."

    tempstat="The temperature is "+str(temp)+" degree celsius. Feels like "+str(felttemp)+" degree celsius."
    global outext
    outext = "If my databases are correct, In "+cityn+", "+tempstat+windspeed+uvindmes+skystat
