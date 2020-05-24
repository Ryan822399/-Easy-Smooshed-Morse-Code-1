#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 17:18:59 2020

For the purpose of this challenge, Morse code represents every letter as a sequence of 1-4 characters, each of which is either . (dot) or - (dash). The code for the letter a is .-, for b is -..., etc. The codes for each letter a through z are:

.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..
Normally, you would indicate where one letter ends and the next begins, for instance with a space between the letters' codes, but for this challenge, just smoosh all the coded letters together into a single string consisting of only dashes and dots.

Examples
smorse("sos") => "...---..."
smorse("daily") => "-...-...-..-.--"
smorse("programmer") => ".--..-.-----..-..-----..-."
smorse("bits") => "-.....-..."
smorse("three") => "-.....-..."
An obvious problem with this system is that decoding is ambiguous. For instance, both bits and three encode to the same string, so you can't tell which one you would decode to without more information.

@author: ryanhennes
"""

#Base Solution
def smorse(str):
    
    #storing both the english and morse alphabets to use for encoding
    morseAlphabet = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.."
    englishAlphabet = "abcdefghijklmnopqrstuvwxyz"
    
    #breaking the morse alphabet into an array list to mirror the english alphabet
    alphabetList = morseAlphabet.split(" ")
    
    
    encodedMessage = ""
    for i in str:
        #building the encoded message by grabbing the morse code from the list based on the letter from the english alphabet
        encodedMessage = encodedMessage + alphabetList[englishAlphabet.index(i)]

    return encodedMessage

print(smorse("sos"))
print(smorse("daily"))
print(smorse("programmer"))
print(smorse("bits"))
print(smorse("three"))