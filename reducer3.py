#!/usr/bin/python3.6
import sys

#person to recommend to, this is the key
current_person = None
#your current list of friends which should not be recommended to you
alreadyFriends = []
#a dict of friends of your friends and how many times they've been seen
potentialContacts = dict()

'''
Builds a sorted string of people who might be your friend 
Based on whether they have 2 or 3 mutual friends with you
'''
def findMight():
  might = []
  for contact in potentialContacts:
    numMutuals = potentialContacts[contact]
    if (contact not in alreadyFriends 
      and numMutuals >= 2 and numMutuals <= 3):
      might.append(int(contact))
  
  #nobody fits
  if len(might) == 0:
    return ''
  might.sort() 
  #need to convert between int and string bc str will sort 1, 10, 2, not 1, 2, 10
  might = [str(num) for num in might]
  return "Might(" + ','.join(might) + ')'

'''
Builds a sorted string of people who probably are your friend 
Based on whether they have at least 4 mutual friends with you
'''
def findProbably():
  probably = []
  for contact in potentialContacts:
    numMutuals = potentialContacts[contact]
    if contact not in alreadyFriends and numMutuals >= 4:
      probably.append(int(contact))
  
  if len(probably) == 0:
    return ''
  probably.sort()
  #need to convert between int and string bc str will sort 1, 10, 2, not 1, 2, 10
  probably = [str(num) for num in probably]
  return "Probably(" + ','.join(probably) + ')'

'''
Prints the list of people who are maybe and probably your 
friends to recommend. Expected format example:
2:Might(1, 7) Probably(3)
'''
def findConnections():
  print(current_person + ':' 
    + findMight() + ' ' + findProbably())

'''
Add a person to a map of friends of your friends
to count how many mutual friends you have 
'''
def mapMutuals(person, potentialContact):
  if potentialContact in potentialContacts:
    potentialContacts[potentialContact] = potentialContacts[potentialContact] + 1
  else:
    potentialContacts[potentialContact] = 1

'''
Parse tab separated key of a person (represented as a number)
and value of a friend of a friend who could potentially be 
recommended to connect with
'''
for line in sys.stdin:
  line = line.split('\t') 
  person = line[0]
  contacts = line[1].split()
  #person has changed, so we know we've seen every instance of this key
  #since all of the same key will go to the same reducer
  if (current_person != person):
    if current_person: 
      findConnections()

    current_person = person
    potentialContacts = dict()
  #this is the list of everyone they are already friends with 
  #to ignore
  if len(contacts) > 1:
    alreadyFriends = contacts
  else:
    mapMutuals(person, contacts[0])
  
if current_person == person:
  findConnections()
  