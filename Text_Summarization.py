#!/usr/bin/env python
# coding: utf-8

# In[2]:


import spacy
#spacy.download.cli(en_core_web_sm)
nlp=spacy.load('en_core_web_sm')
from spacy.lang.en.stop_words import STOP_WORDS
from heapq import nlargest
stopwords=


# In[3]:


from string import punctuation


# In[32]:


import pandas as pd
import numpy as np
import PyPDF2
import nltk
import ssl
import re
ssl._create_default_https_context = ssl._create_unverified_context


# In[5]:


df=pd.read_excel("Books.xlsx")#,encoding="latin-1")


# In[175]:


#import PyPDF2


def text_transform(sent):
    str1=""

    text=list()
    
    
    # creating a pdf file object
    pdfFileObj = open(sent, 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # printing number of pages in pdf file
    print(pdfReader.numPages)
    
    for i in range(pdfReader.numPages):

        # creating a page object
        pageObj = pdfReader.getPage(i)

        # extracting text from page
        #print(pageObj.extractText())
        x=pageObj.extractText()
        #x = re.sub(r'^https?:\/\/.*[\r\n]*', '', x, flags=re.MULTILINE)
        #x= re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', " ",x)
        #x=x.replace("https://www.gutenberg.org/cache/epub//pg.txt",'')
        x=re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', x)
        x=x.replace("PM",'')
        x=x.replace("PM",'')
        x = ''.join([i for i in x if not i.isdigit()])
        x=x.replace("Page",'')
        text.append(x)
        #print(text)

    

    # closing the pdf file object
    pdfFileObj.close()
    str1=" ".join(text)
    nlp.max_length=len(str1)
    return str1
    #return nltk.sent_tokenize(str1)


# In[202]:


def summarizer(z):
    #nlp.max_length=len(z)
    stopwords=list(STOP_WORDS)
    len(stopwords)
    #nlp=en_core_web_sm.load()
    nlp.max_length=len(z)
    doc=nlp(z)
    tokens=[token.text for token in doc]
    word_freq={}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text]=1
            else:
                word_freq[word.text]+=1
    max_freq=max(word_freq.values())
    for word in word_freq.keys():
        word_freq[word]=word_freq[word]/max_freq
    sent_tokens=[sent for sent in doc.sents]
    sent_scores={}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent]=word_freq[word.text]
                else:
                    sent_scores[sent]+=word_freq[word.text]
    
    select_len=int(len(sent_tokens)*0.3)
    summary=nlargest(select_len,sent_scores,key=sent_scores.get)
    final_summary=[word.text for word in summary]
    summary=" ".join(final_summary)    
    return summary
    


# In[208]:


y=summarizer(text_transform(df['Location'][3]))


# In[209]:


print(y)


# In[210]:


len(y)


# In[ ]:





# In[177]:


len(stopwords)


# In[178]:


nlp=spacy.load('en_core_web_sm')


# In[179]:


doc=nlp(text_transform(df["Location"][3]))


# In[180]:


#print(doc)


# In[181]:


tokens=[token.text for token in doc]


# In[182]:


#print(tokens)


# In[183]:


word_freq={}
for word in doc:
    if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
        if word.text not in word_freq.keys():
            word_freq[word.text]=1
        else:
            word_freq[word.text]+=1
                


# In[184]:


max_freq=max(word_freq.values())


# In[185]:


for word in word_freq.keys():
    word_freq[word]=word_freq[word]/max_freq


# In[186]:


sent_tokens=[sent for sent in doc.sents]


# In[187]:


sent_scores={}
for sent in sent_tokens:
    for word in sent:
        if word.text in word_freq.keys():
            if sent not in sent_scores.keys():
                sent_scores[sent]=word_freq[word.text]
            else:
                sent_scores[sent]+=word_freq[word.text]


# In[188]:


select_len=int(len(sent_tokens)*0.1)


# In[189]:




# In[190]:


summary=nlargest(select_len,sent_scores,key=sent_scores.get)


# In[191]:


#print(summary)


# In[192]:


final_summary=[word.text for word in summary]


# In[193]:


summary=" ".join(final_summary)


# In[206]:


#print(summary)


# In[207]:


len(summary)


# In[212]:


#pip install nbconvert


# In[ ]:




