# regular expression in python
# ---------------------------------------
# re.findall() -> returns all non-overlapping matches of a pattern in the string as a list. It scans the string 
# from left to right 


# common Regex Characters 

# . (a.b) matches b ->  matches any single character except a newline 
# ^ (^Hello) -> matches the begining of the string 
# $ (World$) -> matches the end of the string 
# * (hi*) -> matches the zero or more repititions 
# + (hi+) -> matches one or more repititions 
# ? (hi?) -> matches zero or one repititions ("h" or "hi")
# {m, n} -> matches from m to n repititions (a{2, 4} = aa, aaa, aaaa)
# [] -> matches any single character inside the brackets [aeiou] matches any vowel 
# | -> Acts as OR operator cat|dog matches either of them 
# () Groups sub patterns together -> (abc)+ matches abcabc

# Special sequences within Python Regular expressions 

# Special sequences are those whicn provide matching common character sets. 

# "\d": matches any decimal digit (equivalent to [0-9])
# "\D" : Matches any character that is not a digit 
# "\w" : Matches the alphaneumeric character or underscore  
#  "\W" : Matches any non-alphaneumeric character 
# "\s" : Matches any whitespace character (spaces, tabs or newlines)
# "\S": Matches any non-whitespace character 
# "\b": Matches a word with boundary position


import re
string = """Hello, this is network automation number, router IP is 10.10.1.2 and
            switch value is i1.4.32.5"""

regex = '\d+' # find all sequences of one or more digits in the given string
match = re.findall(regex, string)
print(match)

# re.compile() -> compiles the regex into a pattern object which can be reused for matching of substitions. 

import re
p = re.compile('[a-g]')  # print all characters between a to g from a given string 
print(p.findall("This is Python for GNS3 lab, the lab contains routers, ethernets, switches, VPCs"))

# re.split() -> splits the string into a pattern whenever the pattern matches. the remaining characters will be returned 
# as list of elements. 

from re import split

# how to split a string using different patterns like non-word characters (\W+), apos and Digits (\d+)

print(split('\W+', 'words, Words, WORDS'))
print(split('\W+', "Word's words Words"))
print(split('\W+', 'On 1st of June, at 10:23 AM'))
print(split('\d+', 'On 1st of June, at 11 am the Program will end'))

# re.search() -> searches the first occurance of a pattern in a string. It returns the match object if found
# otherwise it'll return none. 

import re

regex = r"([a-zA-Z]+) (\d+)"
match = re.search(regex, "The Python is inventened on June 24")

# searches for the date pattern with a month name (letters) and followed by a day (digit) in a string sentence

if match: 
    print("Match at index %s, %s" % (match.start(), match.end()))
    print("Full match if found:", match.group(0))
    print("Month:", match.group(1))
    print("Day:", match.group(2))
else:
    print("The regex pattern doesn't match")

# in Python's re() module, you can extract the specific parts of a regex value if it's matching 
# by enclosing those parts in parenthesis() to create capturing groups. You can use the .group()
# method on the returned match object to retrieve the specific text captured by the parenthesis. 

# when a regex search is successful, it returns a match object with the following extraction methods. 

# match.group(0) -> return the entire text matched by the regular expression

# match.group(1): -> return the text captured by first set of parenthesis 

# match.group(2) -> return the text captured by the second group of parenthesis 

# match.groups() -> return a tuple containing all captured subgroups starting the group 1.
# 
import re

text = "ID: A-5632"
pattern = r"ID: ([A-Z])-(\d+)"

match = re.search(pattern, text)

if match:
    print(match.group(0)) # output should be full match of input string 
    print(match.group(1)) # output from first parenthesis 
    print(match.group(2)) # output from second parenthesis 
    print(match.groups()) # output from subgroups 
else:
    print("none is matching")
