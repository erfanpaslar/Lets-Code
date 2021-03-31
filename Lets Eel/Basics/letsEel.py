"""
    by Erfan Paslar
    Let's eel
    https://letscode.erfanpaslar.ir/post.php?pId=16
"""

import eel
eel.init('.//webPageFolder')  # path to the web page folder


@eel.expose
def printFromPython(dataFromJs):
    print(dataFromJs)


@eel.expose
def sendDataToJavaScript():
    return "this is some data that returned from python."


eel.start('index.html', block=False)  # html file name


while True:
    eel.sleep(1.0)

    # # This is for part3
    # userTyped = input("type something: ")
    # eel.alertThis(userTyped)()

    # This is for part4
    dataFromJs = eel.getDataFromSecondInput()()
    print(dataFromJs)
