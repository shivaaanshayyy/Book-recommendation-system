#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install requests


# In[2]:


#pip install bs4


# In[178]:


#print(soup.prettify())


# In[179]:


#soup=bs(page.content,'html.parser')
#review=soup.find_all('div',class_='reviewText')


# In[180]:


#review


# In[194]:

from bs4 import BeautifulSoup as bs
import requests
from bs4 import BeautifulSoup, NavigableString
import matplotlib.pyplot as plt
import nltk
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
nltk.download("stopwords")
nltk.download("punkt")
from wordcloud import WordCloud
from textblob import TextBlob
from isbntools.app import *

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import string

def get_reviews(title):
    isbn=isbn_from_words(title)
    print(isbn)
    title=title.replace(" ", "_")
    title=title.replace("'", "_")
    
    #link="https://www.goodreads.com/book/show/"+"72193."+title #+ "?ac=1&from_search=true" + "&qid=%E2%9C%93"+"&rank=1"
    try:
        page=requests.get("https://www.goodreads.com/book/isbn/"+isbn)
    except:
        print("could not connect to goodreads")
        
    print(page)
    soup=bs(page.content,'html.parser')
    review=soup.find_all('div',class_='reviewText')
    reviews=[]
    for i in range(0,len(review)):
        reviews.append(review[i].get_text())
    text="".join(reviews)
    text=text.lower()
    
    y=list()
    #Tokenizing
    text=nltk.word_tokenize(text)
    #print(text)
    
    #Removing Special Characters
    for i in text:
        if i.isalnum():
            #y.concat(i)
            y=y+[i]
    text=y[:]
    y.clear()
    
    #Removing Stopwords
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text=y[:]
    y.clear()
    
    #Lemmatization
    
    for i in text:
        y.append(lemmatizer.lemmatize(i))
    
        
        
    return " ".join(y)




# In[195]:


from wordcloud import WordCloud
from textblob import TextBlob
from PIL import Image

#reviews1=transform_text("".join(reviews))
def w_cloud(xyz):
    reviews1=get_reviews(xyz)
    blob = TextBlob(reviews1)
    x=[ word for (word,tag) in blob.tags if tag.startswith("JJ")]
#print(x)
    reviews1=" ".join(x)

#df['adjectives'] = df['reviews'].apply(get_adjectives)

#spam_texts = " ".join(text for text in spam_messages['transformed_text'])

    spam_cloud = WordCloud(background_color = 'white', max_words=200, collocations = False).generate(reviews1)
    plt.figure(figsize= (20,10))
    plt.imshow(spam_cloud,interpolation= 'bilinear')
    plt.axis("off")
    image=plt.show()
    spam_cloud.to_file("image/wordcloud.png")
    return "image/wordcloud.png"
    #spam_cloud.to_file("image/wordcloud.png")


#title=input("Enter a title")
#w_cloud(title)




# In[93]:
#import pickle
#pickle.dump(reviews1,open('reviews.pkl','wb'))

#type(x)


# In[181]:


#reviews1


# In[ ]:




