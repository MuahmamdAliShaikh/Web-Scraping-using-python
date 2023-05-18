import nltk
wn=nltk.WordNetLemmatizer()
ps=nltk.PorterStemmer()
'''print("The Examples of Lemmatization")
print(ps.stem("goose"))
print(ps.stem("geese"))

print(ps.stem("cactus"))
print(ps.stem('cacti'))
print("The Examples of Stemming")
print(wn.lemmatize("goose"))
print(wn.lemmatize('geese'))

print(wn.lemmatize("cactus"))
print(wn.lemmatize('cacti'))

a=['studying','studies','studied','study','was']
b=["program", "programs", "programmer", "programming", "programmers"]

for word in b:
    print("The Stem of",word,'is',ps.stem(word))

for word in a:
    print("The Lemma of",word,'is',wn.lemmatize(word,pos='v')) #this will convert word into a base form\root form

# a denotes adjective in "pos"
print("The Lema of better is",wn.lemmatize("better", pos ="a"))
print("The Lema of mice is",wn.lemmatize('mice'))
tokens=nltk.word_tokenize("Can you please buy me an Arizona Ice Tea? It's $0.99.")
print("Tokens: ",tokens)
print("Parts of Speech: ",nltk.pos_tag(tokens))'''

import os,re
class Search:
    def _init_(self,path):
        self.path = path
        self.lists =[]
        self.cleandata=[]
        self.files(self.path)
    def files(self,path):
        a = os.scandir(path)
        for i in a:
            if i.is_file():
                f = re.findall(".txt",str(i))
                if f:
                    h = open(i,"r")
                    x = re.split(r'\s+',h.read())
                    for j in x:
                        self.lists.append(j.lower())
            else:
                self.files(i.path)
        return(self.lists)
    def stopwords(self):
        f = open("G:\\New folder\\New folder\lib.txt","r")
        x = re.split("\n",f.read())
        for i in self.lists:
            if i not in x:
                self.cleandata.append(i)
        return(self.cleandata)
a=Search()
a.files("G:\\New folder\\New folder\lib.txt")
print(a.stopwords())
