# Movie-Recommendation-System using Python [Desktop App]

**Introduction**
Tools and Libraries used

a) Programming Language: Python

b) Dataset: IMDB movie dataset 

c) Libraries/Packages: 

    i.   TKinter(For GUI)
    ii.  Pandas
    iii. Numpy
    iv.  CountVectorizer
    v.   cosine_similarity
    
**Flow of the solution**

    1. A data frame is created by reading from the comma separated values
       (csv) file of the dataset.
    2. The features from the dataset are selected which are columns of the
       data frame like movie name, genre, cast, director etc. for the program.
    3. The null values in the columns are transferred to empty values.
    4. A new column in data frame is created which combines all the features
       in step 3.
    5. A count matrix is created from the newly combined column using count
       vectorizer which converts text into vector of token counts.
    6. The cosine similarity is implemented on those vectors on whole data
       frame.
    7. The movie input is taken from user.
    8. The index of the input movie form the dataset is taken into account and
       all the similar movies are to be generated in ascending order.
    9. The user is shown the list of similar movies.
