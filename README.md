# Project-BRIGHTNICK7000
## This is a Mozilla-TTS and Vosk+Kaldi based 'Home assistant' as a part of a I.P./C.S. school project for Class 12 (K.D.A.V.)

The entire project is made in python. Made by Tanmay Vemuri. Expect to see the relevant docs and logs soon as this is a work in progress.
Currently works only in linux and is not meant to be shipped out. Will work on that probably.

Anyone can use anything within this project with absolutely no restrictions. This project is and will always remain open-source.

Have a complaint, suggestion or a copyright complaint? Contact us at Tanmay.vemuri85@gmail.com (This email address will probably be changed or removed later so keep your eye out on that).

This entire project is motivated by the principle that if you're going to make something stupid, you might as well go all in, so there'll definitely be traces of that in this project.

There will be a bash install script that will handle the dependencies for you (In a manner of speaking) so stay tuned for that as well, ig.

Target platform is a raspberry pi but this may change based on the performance. We have noticed that installing mozilla tts is a bit different and harder on a raspberry pi, not to mention that the raspberry pi has very constrained hardware so we'll have to see how this goes along.

### What this can do:
- ASR
- Tells the weather
- Tells a joke
- Searches google and tells the results
- News
- Speak
- Execute terminal commands (WIP)
- Tells a quote
- gives a short description of stuff you ask by looking up Wikipedia
- Dictionary meanings
- Synonyms of words
- Antonyms of words
- Offline Dictionary
- Finds a random wikipedia article and gives a 2-3 sentence summary.
- Gives the meaning of a random legal term (cause why not)
- Open System monitor
- Saves queries to a log file
- Can repeat what you say
- Gives an introduction of itself (Kind of important)
- Pause by voice 
- Exit by voice
- If your query cannot be handled by available statements and functions, takes an angry nap (Just kidding, searches google, tells the results or contents of a table or Opens the first link) 



<br>
Demo video: https://www.youtube.com/watch?v=pY1tT1fTJ2Q   (unlisted link) (Old)
</br>

##### References:

-https://github.com/nmstoker/SimpleSpeechLoop
<br>
-https://github.com/mozilla/TTS
<br>
-https://github.com/mozilla/DeepSpeech
<br>
-https://pypi.org/project/deepspeech/ or https://deepspeech.readthedocs.io/en/r0.9/
<br>
https://github.com/jurgenarias/Portfolio/tree/master/Voice%20Classification
<br>
https://realpython.com/python-speech-recognition/#working-with-microphones
<br>
(Will update this section as the project progresses.)
<br>



</br>
- Note: I'm switching over to Vosk and Kaldi for ASR since Deepspeech isn't very precise with....my "kind of english". But this is not finalised yet so I haven't updated this readme accordingly.
<br>


</br>
- Another note: I'm moving all of the files to Google Drive due to file size limitations in github. Once I upload the final usable build, I'll update the readme accordingly with the link. The whole thing for distribution itself is like 1 GB and post installation it can take up 26 GB (Mostly because you need to build Kaldi by yourself and it is required by Vosk. Also Vosk+Kaldi can understand English with an Indian accent much better than Deepspeech (Without training it yourself, that is.)
