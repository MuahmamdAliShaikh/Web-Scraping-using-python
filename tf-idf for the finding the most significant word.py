#tf-idf telling us which word is more important and significant in the document
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf=TfidfVectorizer()
doc_1="Ali provide trainings to working professionals"
doc_2="Ali provide trainings to students"
response=tfidf.fit_transform([doc_1,doc_2])
#fit means providing data to the algorithm and transform means transform data into the algorithm 
print(len(tfidf.vocabulary_))#got the length of all unique words present in the documents
print(tfidf.vocabulary_) #numeric values got assigned to vocabulary e.g: Ali got encoded in 0
#print(response) #got tfidf values for whole vocabulary 

#Students is more significant word from doc_2
#Working and professionals are more significant word from doc_1

feature_names =tfidf.get_feature_names_out()
for col in response.nonzero()[1]:
    print(feature_names[col],"-",response[0,col])
