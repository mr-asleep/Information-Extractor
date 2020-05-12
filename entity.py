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
	dic={}
	for x in response.entities():
		try:
			dic['Entity'].append(words_c(x.id))
		except:
			dic['Entity']=[]
			dic['Entity'].append(words_c(x.id))

	for x in response.relations():
	    try:
	    	dic['Relation'].append(words_c(x.predicate_words))
	    except:
	    	dic['Relation']=[]
	    	dic['Relation'].append(words_c(x.predicate_words))

	for x in response.noun_phrases():
	    try:
	    	dic['Noun Phrase'].append(words_c(x._words))
	    except:
	    	dic['Noun Phrase']=[]
	    	dic['Noun Phrase'].append(words_c(x._words))

	for x in response.properties():
		try:
			dic['Property'].append(words_c(x.predicate_words))
		except:
			dic['Property']=[]
			dic['Property'].append(words_c(x.predicate_words))
	return dic

text="Iron Man is Robert Downey Jr. Barack Obama is the president of America."
client = TextRazor('a02e9cce51c6c087f150269a4eab62812057696716b70eb1f2e0a8fd', extractors=["entities","phrases"])
response = client.analyze(text)
print(output(response))
