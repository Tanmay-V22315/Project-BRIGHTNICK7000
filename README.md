# Project-BRIGHTNICK7000
## This is a Mozilla-TTS and Vosk+Kaldi based 'Home assistant' as a part of a I.P./C.S. school project for Class 12 (K.D.A.V.)

The entire project is made in python. Made by Tanmay Vemuri. Expect to see the relevant docs and logs soon as this is a work in progress.
Currently works only in debian-based linux distros and is not meant to be shipped out. Will work on that probably.

Anyone can use anything within this project with absolutely no restrictions. This project is and will always remain open-source.

Have a complaint, suggestion or a copyright complaint? Contact me at Tanmay.vemuri85@gmail.com (This email address will probably be changed or removed later so keep your eye out on that).

This entire project is motivated by the principle that if you're going to make something stupid, you might as well go all in, so there'll definitely be traces of that in this project.

There will be a bash install script that will handle the dependencies for you (In a manner of speaking) so stay tuned for that as well, ig.

Target platform is a raspberry pi but this may change based on the performance. I have noticed that installing mozilla tts is a bit different and harder on a raspberry pi, not to mention that the raspberry pi has very constrained hardware so I'll have to see how this goes along.

### What this can do:
- Tells Time
- ASR (offline)
- The Non-Trivial Kind of math using Wolfram engine and its client library.(WIP)(Offline)
- Tells the weather (online (duh, what, do I look like I own a supercomputer that can accurately model and predict the weather at any place?))
- Tells a joke (offline)
- Searches google and tells the results (Online (Again, obvious))
- News (Online)
- Speak (Offline)
- Execute terminal commands (WIP) (Offline)
- Tells a quote (Offline)
- Gives a short description of stuff you ask by looking up Wikipedia (Obviously online)
- Dictionary meanings (Offline)
- Synonyms of words (Offline)
- Antonyms of words (Offline)
- Offline Dictionary (Offline (It's in the name, why am I even telling you)
- Finds a random wikipedia article and gives a 2-3 sentence summary. (Online)
- Gives the meaning of a random legal term (cause why not) (Online)
- Open System monitor (Obvious)
- Saves queries to a log file (I don't even need to say this one)
- Can repeat what you say (....)
- Gives an introduction of itself (Kind of important) (Offline)
- Pause by voice (Obvious)
- Exit by voice (Obvious)
- If your query cannot be handled by available statements and functions, **takes an angry nap** (Just kidding, searches google, tells the results or contents of a table or Opens the first link) (Online)
- Since this project makes use of the Mozilla tts project, This implies that you can train with a dataset to make a custom voice (Maybe even your own). I'll make a Jupyter Notebook so that anyone can make ther own custom voice models.(Or rather make it easier to do so) (Offline, kinda since for training you're better off using Google Colab)
- Tells you random fun facts
And a Whole host of new features coming up in a while. Stay tuned!!
So basically, the point is the Assistant is semi-functional even when offline (Even if it is a bit slower as compared to online versions)


<br>
Demo video: https://www.youtube.com/watch?v=pY1tT1fTJ2Q   (unlisted link) (Old)
</br>

##### References and Credits for Websites:

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
https://kaldi-asr.org/
<br>
https://alphacephei.com/vosk/ and https://alphacephei.com/vosk/models
<br>
https://github.com/alphacep/vosk-api/blob/master/python/example/test_microphone.py (I basically modified this so as to get an input from the user instead of it constantly streaming what you speak.)
<br>
https://stackoverflow.com/ (Obvious, don't need to say anything about it)
<br>
https://colab.research.google.com/ (This is basically the best thing ever. The guys at google provide a virtual machine-esque thing that you can use for anything for 12 hours at a time (30 minutes if you aren't interacting with it/close the browser)
<br>
https://www.moongiant.com/phase/today/ (This is kinda relevant but it is based on time)
(Will update this section as the project progresses.)
<br>
<br>

</br>
## Upcoming

- Music Player
- Physics and maths Calculation using Wolfram
- Config.json
- Conversation.json for referencing responses
- Custom Voice
- Name Change
- Penetration testing (Hacking stuff)



### Notes:

</br>
- Note: I'm switching over to Vosk and Kaldi for ASR since Deepspeech isn't very precise with....my *"kind of english"*. But this is not finalised yet so I haven't updated this readme accordingly.
<br>


</br>
- Another note: I'm moving all of the files to Google Drive due to file size limitations in github. Once I upload the final usable build, I'll update the readme accordingly with the link. The whole thing for distribution itself is like 1 GB and post installation it can take up 26 GB (Mostly because you need to build Kaldi by yourself and it is required by Vosk. Also Vosk+Kaldi can understand English with an Indian accent much better than Deepspeech (Without training it yourself, that is.(As it turns out I'm not made of time....or money or compute power, so......No dice))
<br>


</br>
-Note: The dictionary can now be used offline, complete with meanings, synonyms and antonyms.(9/6/2021 (DD-MM-YYYY))
<br>


</br>
-Uh, New note..No no wait.__Big Note__ Wolfram Engine offline requires (I think) about 19 GB of storage, Point is, required storage for this whole thing will balloon up to 45 GB, which is......quite problematic. 
<br>




<br>
-Scratch that previous Note, It requires 2 gigs to install Wolfram engine, Rejoice!!!!
<br>


</br>
-Note: So....uh It turns out, you can do a lot of stuff with Wolfram, so much that that's what I'm going to be dealing with for the next potential months 
