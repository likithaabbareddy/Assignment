# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 10:27:21 2017

@author: likitha
The regular expression methods are used in this program to remove the junk characters from the given string. 
Findall method is used to find a particular pattern that iterates over lines, it returns all the matches in a single step.
"""

import re # A module in python for String matching/operations  
a = "msdjdgf(^&%*(Aroha Technologies&^$^&*^CHJdjg"
stuff = re.findall('\W(\w+\s\w+)\W', a)
print(stuff[0]) 

