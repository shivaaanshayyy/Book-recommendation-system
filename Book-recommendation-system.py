#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd


# In[ ]:


books = pd.read_csv('books.csv')
users = pd.read_csv('users.csv')
ratings = pd.read_csv('ratings.csv')


# In[ ]:


books['Image-URL-M'][1]


# In[ ]:


users.head()


# In[ ]:


ratings.head()


# In[ ]:


print(books.shape)
print(ratings.shape)
print(users.shape)


# In[ ]:


books.isnull().sum()


# In[ ]:


users.isnull().sum()


# In[ ]:


ratings_with_name = ratings.merge(books,on='ISBN')


# In[ ]:


num_rating_df = ratings_with_name.groupby('Book-Title').count()['Book-Rating'].reset_index()
num_rating_df.rename(columns={'Book-Rating':'num_ratings'},inplace=True)
num_rating_df


# In[ ]:


avg_rating_df = ratings_with_name.groupby('Book-Title').mean()['Book-Rating'].reset_index()
avg_rating_df.rename(columns={'Book-Rating':'avg_rating'},inplace=True)
avg_rating_df


# In[ ]:


popular_df = num_rating_df.merge(avg_rating_df,on='Book-Title')
popular_df


# In[ ]:


popular_df = popular_df[popular_df['num_ratings']>=250].sort_values('avg_rating',ascending=False).head(50)


# In[ ]:


popular_df = popular_df.merge(books,on='Book-Title').drop_duplicates('Book-Title')[['Book-Title','Book-Author','Image-URL-M','num_ratings','avg_rating']]


# In[ ]:


popular_df['Image-URL-M'][0]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


x = ratings_with_name.groupby('User-ID').count()['Book-Rating'] > 200
padhe_likhe_users = x[x].index


# In[ ]:


filtered_rating = ratings_with_name[ratings_with_name['User-ID'].isin(padhe_likhe_users)]


# In[ ]:


y = filtered_rating.groupby('Book-Title').count()['Book-Rating']>=50
famous_books = y[y].index


# In[ ]:


final_ratings = filtered_rating[filtered_rating['Book-Title'].isin(famous_books)]


# In[ ]:


pt = final_ratings.pivot_table(index='Book-Title',columns='User-ID',values='Book-Rating')


# In[ ]:


pt.fillna(0,inplace=True)


# In[ ]:


from sklearn.metrics.pairwise import cosine_similarity


# In[ ]:


similarity_scores = cosine_similarity(pt)


# In[ ]:


similarity_scores.shape


# In[ ]:


def recommend(book_name):
    # index fetch
    index = np.where(pt.index==book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:11]
    
    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        
        data.append(item)
    
    return data


# In[ ]:


import pickle
pickle.dump(popular_df,open('popular.pkl','wb'))


# In[ ]:


books.drop_duplicates('Book-Title')


# In[ ]:


pickle.dump(pt,open('pt.pkl','wb'))
pickle.dump(books,open('books.pkl','wb'))
pickle.dump(similarity_scores,open('similarity_scores.pkl','wb'))

