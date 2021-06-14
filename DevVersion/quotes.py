#    ██╗
# ██╗╚██╗
# ╚═╝ ██║
# ▄█╗ ██║
# ▀═╝██╔╝
#    ╚═╝
#
# Written by Tanmay Vemuri
import csv
import pandas as pd
import subprocess


def main():
    subprocess.run(["shuf","-n", "1", "/home/randomaccessvemuri/Code/Quotes.csv", "-o", "/home/randomaccessvemuri/Code/shuffledquote.csv"])
    global outext
    outext = pd.read_csv("/home/randomaccessvemuri/Code/shuffledquote.csv", usecols =[0,1], header = None, quotechar='"',delimiter=';')
    outext = outext.astype('string')
    outext = outext._get_value(0,0)+" "+outext._get_value(0,1)
    print(outext)

main()
