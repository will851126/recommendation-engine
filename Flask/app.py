#!/usr/bin/python
# coding:utf-8

import flask
import numpy as np 
import pandas as pd 
import json
import warnings
import os
from flask import render_template,request
from gensim.models import Word2Vec 
import random
from azure.storage.blob import BlockBlobService

app = flask.Flask(__name__, template_folder='templates') # 代表目前執行的模組

data=pd.read_csv('./merge_data.csv')

all_titles=[data['ISBN'][i]for i in range (len(data['ISBN']))]

users = data["userID"].unique().tolist()

random.shuffle(users)


users_train = [users[i] for i in range(len(users))]

train_df = data[data['userID'].isin(users_train)]

validation_df = data[~data['userID'].isin(users_train)]

reads_train = []

for i in (users_train):
    temp = train_df[train_df["userID"] == i]["ISBN"].tolist()
    reads_train.append(temp)

reads_val = []
for i in (validation_df['userID'].unique()):
    temp = validation_df[validation_df["userID"] == i]["ISBN"].tolist()
    reads_val.append(temp)





model = Word2Vec(window = 10, sg = 1, hs = 0,
                 negative = 10, 
                 alpha=0.03, min_alpha=0.0007,
                 seed = 14)

model.build_vocab(reads_train, progress_per=200)

model.train(reads_train, total_examples = model.corpus_count, 
            epochs=10, report_delay=1)

X = model[model.wv.vocab]


model.init_sims(replace=True)


books = train_df[["ISBN", "bookTitle"]]

books.drop_duplicates(inplace=True, subset='ISBN', keep="last")

books_dict = books.groupby('ISBN')['bookTitle'].apply(list).to_dict()

def similar_books(v, n = 10):
    
    ms = model.similar_by_vector(v, topn= n+1)[1:]
    
    
    new_ms = []
    for j in ms:
        pair = (books_dict[j[0]][0], j[1])
        new_ms.append(pair)
        
    return new_ms 



@app.route("/",methods=['GET','POST']) # 函數的裝置

def main():
    if flask.request.method == 'GET':
        return(flask.render_template('index.html'))

    if flask.request.method == 'POST':
        m_name = flask.request.form['ISBN']

    if m_name not in all_titles:
            return(flask.render_template('negative.html',name=m_name))
    
    else:
        similar_books(model[m_name])
        recommendation=pd.DataFrame(similar_books(model[m_name]))
        recommendation.columns=['Book_name','percentage']
        name=[]
        for i in range(len(recommendation)):
            name.append(recommendation.iloc[i][0])
            output = recommendation.to_json() 
            #accountName='will'
            #accountKey=''
            #containerName='will'
             

            #blobService = BlockBlobService(account_name=accountName, account_key=accountKey)

            #blobService.create_blob_from_text('will', 'recommendation.json', output)
        
        return flask.render_template('positive.html',book_name=name ,search_name=m_name)

        


if __name__ =="__main__": # 如果以主程式執行
    app.run() #立刻啟動伺服器