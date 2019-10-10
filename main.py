# import nltk
# from nltk.corpus import stopwords

# stopw=set(stopwords.words('english'))
# # print("\n\n Stopwords=",stopw,end="\n\n\n")

# def readFile(file):
#     f=open(file,'r',encoding='utf-8')
#     text=f.read()
#     sentences = nltk.sent_tokenize(text)
#     # print(len(sentences))
#     data=[]
#     for sent in sentences:
#       words=nltk.word_tokenize(sent)
#       words=[w.lower() for w in words if len(w)>2 and w not in stopw]
#       data.append(words)
#     # print(data)
#     return data

# text = readFile("News.txt")
# print(text)

def readFile(file):
  f=open(file,'r',encoding="utf-8")
  text=f.read()
  return text

text = readFile("spam_words.txt")
for i in text:
  


  

