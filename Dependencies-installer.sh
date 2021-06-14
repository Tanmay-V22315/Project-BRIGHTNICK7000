#!/bin/sh
clear
RED='\033[1;31m'
NC='\033[0m'
GR='\033[1;32m'
corenuma=$(nproc --all)
let compcores=$corenuma/2
compcores=$corenuma | awk '{print ($0-int($0)>0)?int($0)+1:int($0)}'
echo -e "${RED}The script will assume you have $corenuma CPU cores.${NC}"
echo -e "${RED} using $compcores CPU cores for Compilations (To prevent OOM errors) ${NC}"
sleep 0.5
echo "From here, there is no stopping the script (Well, no stopping without some minor consequences anyway). By the end of the script, the available disk space will reduce by about 25GB (Mostly due to kaldi) and this will take a long time with high memory usage so I would suggest watching the script for a few minutes and then going to sleep. Let the script do its thing and hopefully with some more work, you should be able to run the python script, to be greeted by your very own BRIGHTNICK7000"
echo
echo
echo -e "${RED} This script will not work on a Raspberry Pi due to its use of an ARM CPU. Some packages or libraries are not available or compiled for an ARM cpu or the repository for Raspbian may not have the necessary packages so you are bound to run into errors somewhere down the road.${NC}"
echo
echo
echo "You will get a prompt regarding the Intel Math Kernel library describing the closed-source nature of the library. You can say no to that and it will proceed just fine. There is no difference in the process for AMD cpu users, the installation will continue all the same.(I can confirm this since I am using an AMD cpu.)"
echo
echo -e "${GR}If at any point you encounter an error or have a doubt, do send me a mail on Tanmay.vemuri85@gmail.com, and hopefully, I'll help you deal with the problem.(Or, hunt me down on Artstation since I'm there as well ;))${NC}"
echo
echo -e "${RED} THIS PART IS VERY IMPORTANT SO READ THE FOLLOWING TEXT CAREFULLY. In a few minutes (Depending upon your internet connection), you will see a script run called check_dependencies.sh, this is regarding kaldi's dependencies. If you see a statement saying 'The following packages were not found, install them using this command' with a command printed below, copy that (Using ctrl+shift+c) and then paste it below in the terminal (Using ctrl+shift+v) if this script stops. If this script doesn't stop, press ctrl+c right when you see that statement and then execute the given command and then run this script again using the same command. Don't worry, this script has been programmed to wait for you to check this. If you see a printed message stating that the 'script will continue normally' even though errors were found, the script will sleep for 2 seconds during which time you can cancel the script. If you only see the error that means this script will have stopped and you can execute the error's command in peace. ${NC}"
echo
echo "NOTE: For using the dictionary, After this script finishes, open the selected python installation (default is python3), type 'import nltk' then 'nltk.download('wordnet')'. It's a small download but is essential for the functioning of the dictionary. "
echo
echo -e "${RED}Would you like to proceed or stop. For proceeding, type yes. Anything else will be considered as no. (Case-Sensitive)${NC}"
read consent
if [ "$consent" == "yes" ]
then
  clear
  cd ~
  mkdir git
  cd git/
  git clone https://github.com/kaldi-asr/kaldi.git --origin upstream
  cd kaldi/tools/extras/
  sudo chmod +x ./check_dependencies
  sudo bash ./check_dependencies
  echo "All good, continuing normally. if the script is continuing regardless of the above error, press Ctrl+C now"
  sleep 2
  cd ~
  sudo apt update && sudo apt upgrade
  sudo apt install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 intel-mkl autoconf automake git libtool svn wget zlib make espeak-ng
  sudo pip3 install pyaudio playsound colorama halo wikipedia pandas bs4 SpeechRecognition deepspeech numpy sounddevice vosk weathercom requests html5lib beatifulsoup4 lxml requests_html python-vlc nltk spacy fastpunct
  python3 -m spacy download en_core_web_sm
  pip3 install pyppeteer
  pyppeteer-install
  sudo apt update
  echo "using $compcores for Compilations"
  cd git/kaldi/tools
  make -j $compcores
  cd ..
  cd src/
  ./configure --use-cuda=no #If you have an Nvidia gpu and have installed the CUDA toolkit and CUdnn package and you have done so properly, just remove the "--use-cuda=no" flag entirely (If you are using Pop!OS, don't install CUDA from their repositories even if the process seems simple)
  make -j $compcores
  sudo apt update && sudo apt upgrade
  git clone https://github.com/mozilla/TTS
  pip install -e .
else
  echo
  echo
  echo
  echo "Understood, Have a great day!"
fi
