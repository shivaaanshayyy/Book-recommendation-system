from flask import Flask,render_template,request
import pickle
import numpy as np
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

from PIL import Image




popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/top')
def index():
    return render_template('index.html',
                           book_name = list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_rating'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


@app.route('/recommend_books',methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:10]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    print(data)

    return render_template('recommend.html',data=data)

@app.route('/reviews')
def review_ui():
    return render_template('reviews.html')
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

@app.route('/review_books',methods=['GET','post'])
def review():
    
    #user_input = request.form.get('title')
    if request.method=='POST':
        title=request.form.get('title')
        image= w_cloud(title)
    return render_template('reviews.html',image=image)



#@app.route('/summarizer')
#def recommend_ui():
 #   return render_template('summarizer.html')

if __name__ == '__main__':
    app.run(debug=True)