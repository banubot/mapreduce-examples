#!/usr/bin/python3.6
import sys

'''
Count the number of times a set of vowels has been seen
'''
current_word = None 
current_count = 0
word = None
for line in sys.stdin:
  line = line.strip()
  line = line.split('\t')
  if len(line) > 1:
    word = line[0]
    count = line[1]
  else:
    word = ' ' #placeholder for no vowels
    count = line[0]
  count = int(count)
  if current_word == word:
    current_count += count
  else:
    if current_word: 
      print(current_word.strip() + ':' + str(current_count))
    current_count = count
    current_word = word
if current_word == word:
  print(current_word.strip() + ':' + str(current_count))