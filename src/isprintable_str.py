#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 10, 2014

@author: anroco

How to know if the characters in a python string is printable?

¿Como saber si los caracteres de un string python son imprimibles?
'''

#create a str
s = 'many years later, 2 persons viewed that event.'
print(s)

#verify if all characters in the string are printable. Return True or
#False. Nonprintable characters are those from category 'Other' or
#'Separator' of the system Unicode, excepting the ASCII space (0x20).
print(s.isprintable())

#create a str
s = '\nmany years later\t'
print(s)

#return False because the string have '\n' and '\t' which are nonprintable
#characters.
print(s.isprintable())
