#    ██╗
# ██╗╚██╗
# ╚═╝ ██║
# ▄█╗ ██║
# ▀═╝██╔╝
#    ╚═╝
#
# Written by Tanmay Vemuri
filenameinp = input("Enter the directory of JSON file (Recommended: keep this editor in the same folder as the JSON file and just enter the name of the file): ")
import json
print("You can't have duplicate Key Elements (So no same inputs). take care of Case, punctuation and other stuff as I have already told you before. Don't add in quotes, that is being handled for you.")
upddict = {}
dec = input("Recovery or Editing: Type 1 for recovery and 2 for Editing. Anything else will be considered as Editing")
if dec == 1:
    upddict=input("Enter the dictionary (!!EXPERIMENTAL!!)")
else:
    while 1>0: #You'll unfortunately lose the ability to comment the file but it's fine anyway
        try:
            x = input("Input: ")
            y = input("Output: ")
            appelem = {x:y}
            print()
            print("This will be appended: ")
            print(appelem)
            print()
            movdec = input("Type 'y' to move ahead, 'n' to repeat")
            print()
            print()
            if movdec=='y':
                upddict.update(appelem)
            elif movdec=='n':
                pass
            else:
                print("I'll take that as a 'No'")

        except KeyboardInterrupt:
            print()
            print("Stopping Editor")
            break
print(upddict)
try:
    try:
        edcon = input("would you like to save the file (Type 'yes for....yes and anything else will be considered as no'): ")
        if edcon=='yes':
            print("Writing to JSON")
            with open(filenameinp, "r+") as file:
                data = json.load(file)
                data.update(upddict)
                file.seek(0)
                json.dump(data, file)
                print("Done! Have nice day.")
        else:
            print("Are you sure? Changes will not be changed")
            edn = input("Type y to save, anything else will be considered as no")
            if edn=='y':
                print("Writing to main JSON file.")
                file_data = json.load(file)
                file_data.update(upddict)
                # Sets file's current position at offset.
                file.seek(0)
                # convert back to json.
                json.dump(upddict, file, indent = 4)
                print("Done! Have nice day.")
    except KeyboardInterrupt:
        print("Are you sure? Changes will not be changed")
        edn = input("Type y to save, anything else will be considered as no")
        if edn=='y':
            print("Writing to main JSON file.")
            file_data = json.load(file)
            file_data.update(upddict)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(upddict, file, indent = 4)
            print("Done! Have nice day.")
except:
    print("Oh no! Something went wrong. Send me a message (Tanmay) and I'll figure something out. As for now, here's your changes :")
    print(upddict)
