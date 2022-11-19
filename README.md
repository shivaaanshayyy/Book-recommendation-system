# Book-Recommendation-system

## What is a Recommender System?
Recommender systems are the systems that are designed to recommend things to the user based on many different factors. These systems predict the most likely product that the users are most likely to purchase and are of interest to. Companies like Netflix, Amazon, etc. use recommender systems to help their users to identify the correct product or movies for them. 
 
The recommender system deals with a large volume of information present by filtering the most important information based on the data provided by a user and other factors that take care of the user’s preference and interest. It finds out the match between user and item and imputes the similarities between users and items for recommendation. 
 
Both the users and the services provided have benefited from these kinds of systems. The quality and decision-making process has also improved through these kinds of systems.

This project is built with the purpose of recommending books and doing web scraping for book reviews.

## Dataset
The data has been taken from kaggle.
Books are identified by their respective ISBN. Invalid ISBNs have already been removed from the dataset. Moreover, some content-based information is given (Book-Title, Book-Author, Year-Of-Publication, Publisher), obtained from Amazon Web Services. Note that in case of several authors, only the first is provided. URLs linking to cover images are also given, appearing in three different flavours (Image-URL-S, Image-URL-M, Image-URL-L), i.e., small, medium, large. These URLs point to the Amazon web site.
The dataset comprises 3 files.

### Users
Contains the users. Note that user IDs (User-ID) have been anonymized and map to integers. Demographic data is provided (Location, Age) if available. Otherwise, these fields contain NULL-values.

### Books
Books are identified by their respective ISBN. Invalid ISBNs have already been removed from the dataset. Moreover, some content-based information is given (Book-Title, Book-Author, Year-Of-Publication, Publisher), obtained from Amazon Web Services. Note that in case of several authors, only the first is provided. URLs linking to cover images are also given, appearing in three different flavours (Image-URL-S, Image-URL-M, Image-URL-L), i.e., small, medium, large. These URLs point to the Amazon web site.

### Ratings
Contains the book rating information. Ratings (Book-Rating) are either explicit, expressed on a scale from 1-10 (higher values denoting higher appreciation), or implicit, expressed by 0.

## There are 4 Types of recommender systems:
1. Popularity-based
2. Content-based
3. Collaborative-filtering-based
4. Hybrid-based

In this project, We are using:
1. Collaborative-filtering-based recommender system:
Here all the data is taken as multi-dimensional points.
All the books are taken as data points and we use euclidean distance to find the books that are nearest to the one. Then we take those books and display them.
Here users with similar tastes on books are grouped together. So if User A and User B are similar, User A likes book x and book y while User B likes book x, the system recommmends book y to User A.¶

2. Popularity-based recommender system:
With this, we display the top 50 books based on the most-ratings given by the users.
We are only taking the books that have recieved more than 250 ratings and then we calculate the average rating.



