import string
import re
import io
import random
import string # to process standard python strings
import warnings
import warnings
warnings.filterwarnings('ignore')



GREETING_INPUTS = ("How are you","hello", "hi", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "Give me a name and I will tell you all about that person", "hi there enter a query and I will give you a description", "hello", "I am glad! You are talking to me", "Say something you want to learning about"]



def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)






