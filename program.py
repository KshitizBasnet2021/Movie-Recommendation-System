#Tools needed for the program
from tkinter import *
from tkinter import ttk
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk

    
#initialize tkinter
root=Tk()
root.title('Movie Recommendation System')#set title
root.configure(background='#FFFFFF')#set bg=white

#import csv file
df = pd.read_csv("movie_dataset.csv")

#get all titles and put it in list
listtitles = df.original_title.tolist()
#label for selection UI
text=Label(root,text="Select the movie title: ",font="Times 12",padx=15,pady=10,background='#FFFFFF',foreground="#02294F")
text.grid(row=0, column=0)
#Combobox UI values from list titkes
combotitle =ttk.Combobox(root, values=listtitles,background="#D3D3D3",foreground="#02294F",font="Times 12")
combotitle.grid(column=1, row=0,padx=5)

#functions to display the info of selected movie
def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]

def get_plot_from_index(index):
    return df[df.index== index]["overview"].values[0]

def get_director_from_index(index):
    return df[df.index== index]["director"].values[0]

def get_cast_from_index(index):
    return df[df.index== index]["cast"].values[0]

def get_rating_from_index(index):
    return df[df.index== index]["vote_average"].values[0]

def get_genre_from_index(index):
    return df[df.index== index]["genres"].values[0]

def get_date_from_index(index):
    return df[df.index== index]["release_date"].values[0]

def display_movies():
    if(combotitle.get()==''):
         print("Error: Please select movie from the combo box.")
    else:    
        #first display about the movie at right side
        selected_index=get_index_from_title(combotitle.get())
        selected_title=get_title_from_index(selected_index) 
        selected_plot=get_plot_from_index(selected_index)
        selected_director=get_director_from_index(selected_index)
        selected_cast=get_cast_from_index(selected_index)
        selected_rating=get_rating_from_index(selected_index)
        selected_genres=get_genre_from_index(selected_index)
        selected_date=get_date_from_index(selected_index)
        
        secondrow2=Label(root,text="About this movie",background="#0680F7",foreground="#FFFFFF",font="Times,BOLD, 13",padx=10,pady=10,
                        highlightcolor="#FAFAFA",width=35)
        
        secondrow2.grid(row=3,column=13,columnspan=5)
        secondrow3=tk.Text(root,width=42,height=20,background="#00264B",foreground="#FFFFFF",font="Times 12")
        secondrow3.grid(row=4,column=13,columnspan=5,rowspan=6)
        secondrow3.insert(tk.END, selected_plot)
        
        dire="Director: "+selected_director
        thirdrow=Label(root,text=dire,background="#00264B",foreground="#FFFFFF",font="Times 13",padx=10,pady=10,
                        highlightcolor="#FAFAFA",width=35)
        thirdrow.grid(row=10,column=14,)

        cast="Cast: "+selected_cast
        fifthrow=tk.Text(root,width=42,height=2.5,background="#00264B",foreground="#FFFFFF",)
        fifthrow.insert(tk.END, cast)
        fifthrow.grid(row=11,column=14,)


        rate="Rating: "+str(selected_rating)
        thirdrow=Label(root,text=rate,background="#00264B",foreground="#FFFFFF",font="Times 13",padx=10,pady=10,
                        highlightcolor="#FAFAFA",width=35)
        thirdrow.grid(row=12,column=14,)
        df = pd.read_csv("movie_dataset.csv")

       
        genres="Genres: "+str(selected_genres)
        thirdrow=Label(root,text=genres,background="#00264B",foreground="#FFFFFF",font="Times 13",padx=10,pady=10,
                        highlightcolor="#FAFAFA",width=35)
        thirdrow.grid(row=13,column=14,)
        

        dates="Release Date: "+str(selected_date)
        thirdrow=Label(root,text=dates,background="#00264B",foreground="#FFFFFF",font="Times 13",padx=10,pady=10,
                        highlightcolor="#FAFAFA",width=35)
        thirdrow.grid(row=14,column=14,)

       #implementation of AI in making recommendation system
        display="Similar Movies to "+selected_title
        
        secondrow=Label(root,text=display,background="#0680F7",foreground="#FFFFFF",font="Times,BOLD, 13",padx=10,pady=10,
                        highlightcolor="#FAFAFA",width=110)
        secondrow.grid(row=3,column=0,columnspan=12,)
       
        features = ['keywords','genres','cast','director']

        #replace null values with empty string
        for feature in features:
            df[feature] = df[feature].fillna('')

        #combine all the selected features     
        def combine_features(row):
            
            return row['keywords'] +" "+row['genres']+" "+row["cast"]+" "+row["director"]
        
        #count vectorizer on the combined features
        df["combined_features"] = df.apply(combine_features,axis=1)
        cv = CountVectorizer()
        count_matrix = cv.fit_transform(df["combined_features"])
        #cosine similarity
        cosine_sim = cosine_similarity(count_matrix) 
        
        #list of similar Movies
        similar_movies =  list(enumerate(cosine_sim[selected_index]))
        #list of sorted simmular movies
        sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)
       
        
        #loop through to display 50 similar movies
        i=0  
        row=4
        col=0
        for element in sorted_similar_movies:
                 
            title= get_title_from_index(element[0])
            title_label=Label(root,text=title,background="#FFFFFF",foreground="#000000",font="Times 11",padx=15,pady=5,
                        highlightcolor="#FAFAFA",width=20, borderwidth=2, relief="groove",justify=tk.LEFT)
            title_label.grid(row=row,column=col, padx=5, pady=5,)

            col=col+1
            i=i+1
            if col==5:
                row=row+1
                col=0
            if i>49:
                break

#recommend movies button
btn=Button(root,text='Recommend Similar Movies',command=display_movies,background="#000099",foreground="#FFFFFF", borderwidth=2, relief="groove",)
btn.grid(column=2, row=0)

#loop
root.mainloop()

