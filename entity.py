from textrazor import *
from SPARQLWrapper import SPARQLWrapper, JSON
import json

def words_c(A):
	if isinstance(A, list):
		a=[]
		for l in A:
			a.append(repr(l))
		return " ".join(a)
	else:
		return str(A)

def output(response): # look at textrazor's tutorial for adding entity, relations, etc.
	phrases=[]
	for x in response.noun_phrases():
		# print(x)
		phrases.append(words_c(x._words))
	return phrases

text="Iron Man is Robert Downey Jr. Barack Obama is the president of America."
client = TextRazor('a02e9cce51c6c087f150269a4eab62812057696716b70eb1f2e0a8fd', extractors=["entities","phrases"])
response = client.analyze(text)
print(output(response))