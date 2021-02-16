#!/usr/bin/python3.6
import sys 
'''
Mapper for a set of contacts
for friendship recommendation
Each line is a person and a lest of their friends in
the format 
1 : 2 3 4 5
Map each friend to every other friend as having mutual
friends to recommend they connect
Also map a person with their current friend list to
ignore someone if they are already your friend 
'''
line = sys.stdin.readline()
while line:
  line = line.strip()
  person, friends = line.split(':')
  person = person.strip()
  friends = friends.strip()
  #map a person with their current friend
  #this is distinguished as the friends list by its length > 1
  print(person + '\t' + friends)
  friends = friends.split()
  #map friend with each other, 1 at a time
  for friend in friends:
    for otherFriend in friends:
      if otherFriend != friend:
        print(friend + '\t' + otherFriend)
  line = sys.stdin.readline()