#!/usr/bin/python3.6
import sys 

'''
Map the set of vowels in a word, sorted and a count value of 1
To see how many words have the same vowels
example: 'elementary'
aeee\t1
'''
line = sys.stdin.readline()
vowels = "aeiouy"
while line:
  line = line.split()
  for word in line:
    theseVowels = []
    for letter in word.strip().lower(): 
      if letter in vowels:
        theseVowels.append(letter)
    theseVowels.sort()
    print(''.join(theseVowels)+"\t"+"1")
  line = sys.stdin.readline()