import json
import os

file1 = open("./output.lexicon","w")
results = []
with open('earl_api_output.txt') as f:
	for jsonObj in f:
		try:
			resultDict = json.loads(jsonObj)
			results.append(resultDict)
		except:
			print("Error",i)
f.close()

lexeme_count={}
for result in results:
	type=result["ertypes"]
	for i,j in enumerate(result["chunktext"]):
		dict_={}
		for l in result["rerankedlists"][str(i)]:
			dict_["lexeme"]=j["chunk"]
			try:
				if l[1].split('/')[-2]=="property":
					 dict_["formula"]= "dbp:"+l[1].split('/')[-1]
				elif l[1].split('/')[-2]=="ontology":
					dict_["formula"]= "dbo:"+l[1].split('/')[-1]
				else:
					dict_["formula"]= "dbr:"+l[1].split('/')[-1]
				if j["chunk"] not in lexeme_count.keys():
					lexeme_count[j["chunk"]]=0
				if lexeme_count[j["chunk"]]<5: # select number of candidates here
					lexeme_count[j["chunk"]]+=1
					file1.write(json.dumps(dict_))
					file1.write("\n")
			except:
				print(j["chunk"])
				pass