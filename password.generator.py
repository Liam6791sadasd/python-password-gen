#importing needed imports
import math
import random
import os
import time
import re
from datetime import datetime
import os.path

#dont touch
dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S)")


#config. messages and whatnot.
possible_letters = "abcdefghijklmnopqrstuvwxyz123456789-_=+/?!@#$%&ABCDEFHIJKLMNOPQRSTUVWXYZ" #possible characterss to be used in password.
message = "\nDone. I've generated your password. Here it is: " #obvious
message_2 = "\nYou want a password to be generated? Okay. It can contain: A-Z, a-z, 1-9 and -_=+/?!@#$%&." # obvious
message_generating = "\nGenerating password. Please wait." #obvious
length = input("How many characters would you like there to be in your password? (1-16): ") #gets user input asking the amt of characters to be generated.
ifnotnumber = "\nYou didn't enter a valid number/character" #obvious 
strongpasswordmessage = "\nThis is a strong password. A password with an uppercase letter, lowercase letter, number(s) and special character(s) is considered a strong password, as long as it is over 8 characters long." #strong password message
weakpasswordmessage = "\nThis is a medium/weak password. A password with an uppercase letter, lowercase letter, number(s) and special character(s) is considered a strong password, as long as it is over 8 characters long." #weak password message

#dont touch, unless you want to change the name of the file and location it is stored at. make sure to include the \\ in the path, or else will brokey
save_path = 'C:\\Users\\liam6\\Desktop'
name_of_file = "saved_passwords"
completeName = os.path.join(save_path, name_of_file+".txt")       

#dont touch, it grabs input and does stuff
if length == ("1"):
    length = 1
elif length == ("2"):
    length = 2
elif length == ("3"):
    length = 3
elif length == ("4"):
    length = 4
elif length == ("5"):
    length = 5
elif length == ("6"):
    length = 6
elif length == ("7"):
    length = 7
elif length == ("8"):
    length = 8
elif length == ("9"):
    length = 9
elif length == ("10"):
    length = 10
elif length == ("11"):
    length = 11
elif length == ("12"):
    length = 12
elif length == ("13"):
    length = 13
elif length == ("14"):
    length = 14
elif length == ("15"):
    length = 15
elif length == ("16"):
    length = 16
else:
    print(ifnotnumber)
    time.sleep(5 * 90)


#don't touch
generated_password = "".join(random.choice(possible_letters) for i in range(length)) #generates password from string of possible letters and length that user made


#generating password
print(message_2)
print(message_generating)

#sending the generated password
time.sleep(5)
print(message + generated_password)

#password strength checker
rexes = ('[A-Z]', '[a-z]', '[0-9]', '[-_=+/?!@#$%&]') #has at least 1 uppercase/lowercase letter, at least 1 number and at least one special character.

if len(generated_password) >= 8 and all(re.search(r, generated_password) for r in rexes): #checks if password that has been generated has met all 5 requirements
    print(strongpasswordmessage)
    savetofile = input("\nWould you like to save this password to a .txt file? (Saves to desktop) (Y/N): ") #do u want to save the password to a text file?
else:
    print(weakpasswordmessage)
    print("\nYour password is weak/medium strength, don't bother saving it, generate a stronger one!")


# if user inputs y/Y, then it will create a file and save the password + timestamp that it was generated at.
if savetofile == ("y" or "Y"):
    f = open(completeName, "a")
    f.write("\nPassword generated: " +  str(generated_password) + "\nAt: " + str(timestampStr) + "\n\n")
    f.close()
    print("\nI have saved your your file to your desktop. If you use the generator again, your passwords will not be overwritten, just added to the bottom of the last password. You're welcome.")
else: #doesnt create file
    print("\nI won't save it then. Have fun.")

time.sleep(5 * 90) #yes

#time.sleep(5 * 90) was added to make it so that the console doesn't close every time you finish with your passwords. I'm sure that there was a more efficent way, but whatever.
