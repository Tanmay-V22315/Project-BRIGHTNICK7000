# Project-NEUROMANCER
# OutDated, Will post the source once completed
## This is a Coqui-TTS and Vosk+Kaldi based 'Home assistant' as a part of a I.P./C.S. school project for Class 12 (K.D.A.V.)

The entire project is made in python (Well, T&C apply). Made by Tanmay Vemuri. Expect to see the relevant docs and logs soon as this is a work in progress.
Currently works only in debian-based linux distros and is not meant to be shipped out. Will work on that probably.

Anyone can use anything within this project with absolutely no restrictions. This project is and will always remain open-source.

Have a complaint, suggestion or a copyright complaint? Please please Contact me at Tanmay.vemuri85@gmail.com or raise a github issue, I would be more than happy to resolve it.
### No-holds barred
This entire project is motivated by the principle that if you're going to make something stupid, you might as well go all in, so there'll definitely be traces of that in this project.


## Project Info
There will be a bash install script that will handle the dependencies for you (In a manner of speaking) so stay tuned for that as well, ig.

Target platform is a raspberry pi but this may change based on the performance. I have noticed that installing mozilla tts is a bit different and harder on a raspberry pi, not to mention that the raspberry pi has very constrained hardware so I'll have to see how this goes along.

### What this can do (Outdated, more stuff has been added):

- Tells Time | Offline
- Automatic Speech Recognition (offline)
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
- Configure paths, voice, location, whether to autocorrect
- Classify Input into request types using Scikit-learn and its Naive Bayes algorithm if *'primitive'* filters miss.
- Exit by voice (Obvious)
- If your query cannot be handled by available statements and functions, **takes an angry nap** (Just kidding, searches google, tells the results or contents of a table or Opens the first link) (Online)
- Since this project makes use of the Mozilla tts project, This implies that you can train with a dataset to make a custom voice (Maybe even your own). I'll make a Jupyter Notebook so that anyone can make ther own custom voice models.(Or rather make it easier to do so) (Offline, kinda since for training you're better off using Google Colab)
- Tells you random fun facts
And a Whole host of new features coming up in a while. Stay tuned!!
So basically, the point is the Assistant is semi-functional even when offline (Even if it is a bit slower as compared to online versions)


<br>
Demo video: https://www.youtube.com/watch?v=pY1tT1fTJ2Q   (unlisted link) (Old)
</br>

**References and Credits for Websites**:

-https://github.com/nmstoker/SimpleSpeechLoop
<br>
https://www.wolframcloud.com/ (Don't worry, we're using the offline WolframEngine (Don't want it? You guessed it right, Don't worry again, you can configure it to use the cloud, you will have to sign up either way unfortunately))
<br>
https://www.wolfram.com/engine/
<br>
https://reference.wolfram.com/language/
<br>
-https://github.com/coqui-ai/TTS
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
<br>
https://ai.google.com/research/NaturalQuestions/databrowser
<br>
</br>
**https://colab.research.google.com/github/tensorflow/tensorflow/blob/master/tensorflow/lite/g3doc/tutorials/model_maker_question_answer.ipynb** (This one is important)
<br>
<br>
(Will update this section as the project progresses.)
<br>
<br>


## TODO

- Music Player
- Autocorrect user input (can be turned on or off in config)
- Multithreading and stuff in certain places to optimize the assistant (Time-wise)
- Spoken Chess. Will be *cheating* a bit here and use C++ for this for obvious reasons. (Not too sure about this one. I could make use of the stockfish module for python but.....my pride won't allow it.)
- Physics and maths Calculation using Wolfram
- Query queuing (*Working on this one currently*)
- Using AIML to program in some responses (Being done by Adithya Bharadwaj)
- Custom Voice 
- Intrusion, Counter-Intrusion stuff, SIGINT (Hacking stuff) (I might remove this one since it kinda poses a security risk even to the end user)<br>
- Complex math, physics, and chemistry (Ironically, complex salts don't work properly) questions, history economics and whatever the WolframEngine can handle using SemanticInterpretation.
- **SHODAN** (Maybe, someday) (the character from System Shock, not the search engine)
- Read books aloud.
- Port to Cython (Don't hold your breath for this one, there's no guarantee that I'll be doing this.)
- Manually add in resources and code to handle Graph plotting, equation render, vector algebra and other *"special cases"* to make utmost use of WolframEngine.
- Generate a huge dataset (Dataset as in {"An attribute" : "Value of the attribute"}) based on what the user wanted, combining data found from Wikipedia, Google and Wolfram, generate a Dataframe from these and convert that dataframe to HTML which can then be opened using webbrowser module for python.


# Stuff from TODO finished:

- Configuration file
- Name Change (We here kinda don't like the name BRIGHTNICK-7000)
- Based on (haha, based) user input, find wikipedia page or get text from first three web sites for the proper noun mentioned in question and based on the actual text, give answer (*BERT*)
- Input comprehension and thus finding answers to more 'complex' questions (Complex as in difficult to code in) like how many people in a place, When was Halo 2 released (I just love that game) etc. Basically, this will literally learn as you speak.
- Implementing DialoGPT for handling edge cases and and conversational responses we can't program in.
- Classify Input into request types using Scikit-learn and its Naive Bayes algorithm if *'primitive'* filters miss.

# Special Thanks to:
- Adithya Bharadwaj for partnering with me. Thanks Pardner!


# Notes:
## Here you can see me slowly devolving into insanity....and finding some cool stuff along the way.

- Note: I'm switching over to Vosk and Kaldi for ASR since Deepspeech isn't very precise with....my *"kind of english"*. But this is not finalised yet so I haven't updated this readme accordingly.
- Another note: I'm moving all of the files to Google Drive due to file size limitations in github. Once I upload the final usable build, I'll update the readme accordingly with the link. The whole thing for distribution itself is like 1 GB and post installation it can take up 26 GB (Mostly because you need to build Kaldi by yourself and it is required by Vosk. Also Vosk+Kaldi can understand English with an Indian accent much better than Deepspeech (Without training it yourself, that is.(As it turns out I'm not made of time....or money or compute power, so......No dice))
- Note: The dictionary can now be used offline, complete with meanings, synonyms and antonyms.(9/6/2021 (DD-MM-YYYY))
- Uh, New note..No no wait.**"Big Note"** Wolfram Engine offline requires (I think) about 19 GB of storage, Point is, required storage for this whole thing will balloon up to 45 GB, which is......quite problematic. 
- Scratch that previous Note, It requires 2 gigs to install Wolfram engine, Rejoice!!!! (Although it increases as you go along and request (In a manner of speaking) more data)
- Note: So....uh It turns out, you can do a lot of stuff with Wolfram, so much that that's what I'm going to be dealing with for the next potential months 
- Note: So I....uh......I just heard about [DialoGPT](https://github.com/microsoft/DialoGPT). AND IT'S THE COOLEST THING I'VE EVER SEEN. Also, you probably know what this means, right?.....right? (For those that are a bit slow, I'll be implementing this into the project to get edge-case responses)
- Note: Just noticed [AIML](https://iq.opengenus.org/get-started-with-aiml/) exists, will be replacing conversation.json with aiml files
- Note: I'm switching to YAML in place of JSON for user config because it's giving me a lot of trouble.
- Note: Our version of the assistant finally has a name 🎉🎉🎉. We are calling it Bernard, a reference to [Bernard of Chartres's](https://en.wikipedia.org/wiki/Bernard_of_Chartres) phrase: "On the shoulder of giants".
- Note: I'm goin' to be using a 'code signature', not as a way to assert ownership or something like that but just because it looks cool (I mean, just look at that smile ;)) (Also, I won't use this code signature in files which are just modified versions of existing files from other users or files which relied upon articles and stuff since that's.......plagiarism.)

```
    ██╗
 ██╗╚██╗
 ╚═╝ ██║
 ▄█╗ ██║
 ▀═╝██╔╝
    ╚═╝

 Written by Tanmay Vemuri
```
- So I found about NNUEs (Neural Networks updated efficiently) and thanks to that I don't have to deal with making hand-crafted evaluation functions for chess (the thing that, given a state of the chess board, predicts whose side the match is in at that very point) but that's a very small (albeit very essential ) part of the work done, I'll still need to learn C++ and still need to create a gui, create a chess board, define legal moves....blah blah blah cut to my brain blowing up. TL;DR- A lot of work is still left for chess. 
- So I've finally made the decision of going insane and writing up the entire chess board in 3-D using Vulkan, I have quite a bit of prior experience with regards to 3D art anyway so....hopefully I won't have a lot of problem. Also that ray-tracing is going to look sweet **if** I get through with all of it.
- (8/7/2021) Note: The development has come to a stand-still due to lack of time and disorganised code management. Will resume shortly. Also, working on creating a Vulkan Renderer for chess for which I actually have to _learn_ the Vulkan API.....while knowing nothing about Computer Graphics (yeah, on second thought, not my brightest move but I'll pull through). Hopefully, [this](https://vkguide.dev/) will make it easier
- Facing some problems with TTS, Will be dealing with that. (09/07/2021)
- It seems there's this thing called [Cauldron](https://github.com/GPUOpen-LibrariesAndSDKs/Cauldron) which makes working with Vulkan _and_ DirectX 12 so that's a 👍 thing

