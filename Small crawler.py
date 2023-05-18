from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk import WordNetLemmatizer
stop_words=stopwords.words('english')
f=open("G:\\New folder\\New folder\lib.txt","r")
ftext=f.read()
#ftext="Welcome to the programming knowledge. Lets start with our first tutorial on NLTK. We shall learn the basis of NLTK here."
wn=WordNetLemmatizer()
tokenize_words=word_tokenize(ftext)
tokenize_words_without_stop_words = []
for i in tokenize_words:
    lemma_words=wn.lemmatize(i,pos='v')
    for word in [lemma_words]:
        if word not in stop_words:
            tokenize_words_without_stop_words.append(word)
            appendFile = open('filteredtext.txt','a')
            appendFile.write(" "+word)
##print("Stops words which got remove",set(tokenize_words)-set(tokenize_words_without_stop_words))
print("Tokenize words including stop words",tokenize_words)
print("Tokenize words without stop words and lemmitization",tokenize_words_without_stop_words)
