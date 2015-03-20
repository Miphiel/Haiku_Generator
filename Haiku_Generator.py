#!/usr/bin/python
#
#Miphiel

import random
import urllib2

#Access online dictionary
word_site = "https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = urllib2.urlopen(word_site)
txt = response.read()
WORD = txt.splitlines()


#Count syllables
def syllables(word):
	count = 0
	vowels = 'aeiouy'
	word = word.lower()
	if word[0] in vowels:
		count += 1
	for index in range(1,len(word)):
		if word[index] in vowels and word[index-1] not in vowels:
			count += 1
	if word.endswith('e'):
		count -= 1
	if word.endswith('le'):
		count += 1
	if count == 0:
		count += 1
	return count

#Generates the first line of the haiku
def line1():
	syll_count = 0
	word1 = ''
	word2 = ''
	word3 = ''
	while syll_count != 2:
		word1 = random.choice(WORD)
		syll_count = syllables(word1)
	syll_count = 0
	while syll_count != 2:
		word2 = random.choice(WORD)
		syll_count = syllables(word2)
	syll_count = 0
	while syll_count != 1:
		word3 = random.choice(WORD)
		syll_count = syllables(word3)
	print word1 + ' ' + word2 + ' ' + word3

#Generates the second line
def line2():
	syll_count = 0
	word1 = ''
	word2 = ''
	word3 = ''
	word4 = ''
	while syll_count != 2:
		word1 = random.choice(WORD)
		syll_count = syllables(word1)
	syll_count = 0
	while syll_count != 2:
		word2 = random.choice(WORD)
		syll_count = syllables(word2)
	syll_count = 0
	while syll_count != 2:
		word3 = random.choice(WORD)
		syll_count = syllables(word3)
	syll_count = 0
	while syll_count != 1:
		word4 = random.choice(WORD)
		syll_count = syllables(word4)
	print word1 + ' ' + word2 + ' ' + word3 + ' ' + word4

#Generates the third line
def line3():
	syll_count = 0
	word1 = ''
	word2 = ''
	word3 = ''
	while syll_count != 2:
		word1 = random.choice(WORD)
		syll_count = syllables(word1)
	syll_count = 0
	while syll_count != 2:
		word2 = random.choice(WORD)
		syll_count = syllables(word2)
	syll_count = 0
	while syll_count != 1:
		word3 = random.choice(WORD)
		syll_count = syllables(word3)
	print word1 + ' ' + word2 + ' ' + word3

#Generates the haiku by running the 3 line functions
line1()
line2()
line3()
