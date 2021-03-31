"""
    by Erfan Paslar
    Let's eel
    https://letscode.erfanpaslar.ir/post.php?pId=16
"""

import eel
import random
eel.init('.//web')

####1####
# if you try to this it will first take some time load and then prints "None" -_-
# randomNumberFromJs = eel.js_random()()
# print(randomNumberFromJs)
# so what you should do is:
# and this works fine and we call this called callback function.
eel.js_random()(lambda n: print(n))


def printRandom(number):
    print(number)


eel.js_random()(printRandom)


#####2#####
@ eel.expose
def py_random():
    return random.randint(0, 100)


eel.start('index.html')
