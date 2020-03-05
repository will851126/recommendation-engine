# Built  book rcommender System on Azure notebook 

## Scenario 

In this Lab , we use the **Book-Crossing** datasets to showcase how can use [Azure notebook](https://docs.microsoft.com/en-us/azure/notebooks/azure-notebooks-overview) for built book rcommender System base on **Word2Vec** model , and goal is to **predict What book do users favorite**

<p align="center">
    <img src="images/017.png" width="50%" height="80%">

## Prerequisite

* To have Microsoft Account or a work or school account


* Download **book folder**  which is in this repository in your computer folder





## Run notebook in Azure notebook

* Click **book_Recommendation System.ipynb**

<p align="center">
    <img src="images/016.png" width="80%" height="80%">


<p align="center">
    <img src="images/014.png" width="80%" height="80%">


* Load libraries

<p align="center">
    <img src="images/018.png" width="80%" height="80%">


* Load  and view for Book Data 



<p align="center">
    <img src="images/019.png" width="80%" height="80%">

* Define book data columns and check
    
<p align="center">
    <img src="images/020.png" width="80%" height="80%">


* Load User data 

        
* Define User data columns

    <p align="center">
    <img src="images/021.png" width="80%" height="80%">

* Load Book rating data 
        
* Define book rating columns and check

<p align="center">
    <img src="images/022.png" width="80%" height="80%">

* Merge user and ratings data  by `UserID` 

<p align="center">
    <img src="images/023.png" width="80%" height="80%">

* Merge book daya by `ISBN` and check columns

<p align="center">
    <img src="images/024.png" width="80%" height="80%">


* Drop columns

    * define Drop_columns 

    * Drop columns 

    <p align="center">
    <img src="images/025.png" width="80%" height="80%">

* Check data size 

<p align="center">
    <img src="images/026.png" width="80%" height="80%">

## EDA(Exploratory Data Analysis)


* Observe data type and observe data value 
    
<p align="center">
    <img src="images/027.png" width="80%" height="80%">


* Observe data columns is **null value**

<p align="center">
    <img src="images/028.png" width="80%" height="80%">

* Count distinct observations over requested axis

       
<p align="center">
    <img src="images/029.png" width="80%" height="80%">


* Plot columns`[Age]` distributed


<p align="center">
    <img src="images/030.png" width="80%" height="80%">

*   Observe in colums`[Age]` if age over 100

<p align="center">
    <img src="images/031.png" width="80%" height="80%">

*  Replace `0` value in columns`[bookRatings]` if value is **null**

        
<p align="center">
    <img src="images/047.png" width="80%" height="80%">

* plot columns`[bookRating]` distributed

<p align="center">
    <img src="images/032.png" width="80%" height="80%">

* Calculate bookRating mean to the second point

<p align="center">
    <img src="images/048.png" width="80%" height="80%">

* Observe and plot columns`[yearOfpublication]` distributes


<p align="center">
    <img src="images/033.png" width="80%" height="80%">

* Group multiple set by **country** and **bookratings**

<p align="center">
    <img src="images/049.png" width="80%" height="80%">




## Feature Engineering


* Cast to numeric

* Handle outliers

* Impute **unknown** value in Categorical feautes

* Check cat features 

<p align="center">
    <img src="images/034.png" width="80%" height="80%">


* Remain **median plus or minus one unit of standard deviation** in  columns`[age]`

        
    <p align="center">
    <img src="images/035.png" width="80%" height="80%">


## Extract features

* Extract feature in columns`[Location]` is  **USA**

* check data 

<p align="center">
    <img src="images/036.png" width="80%" height="80%">



## Prepeare dataset

* Define data equal df

* Find Relevant score >= 6
        

* Check value  groupby `ISBN` and `User-ID`

        

<p align="center">
    <img src="images/037.png" width="80%" height="80%">

* Filter x > length of 5 

<p align="center">
    <img src="images/050.png" width="80%" height="80%">

## Embedings (word2vec)


* Load package

        

<p align="center">
    <img src="images/039.png" width="80%" height="80%">


* Calculator users count, and set type of **list**

<p align="center">
    <img src="images/40.png" width="80%" height="80%">

* Extract 90% of customer ID

*  Split data of train and validation set 

<p align="center">
    <img src="images/041.png" width="80%" height="80%">

* Append list of  columns userID and ISBN in train to reads_train

<p align="center">
    <img src="images/052.png" width="80%" height="80%">

*  Append list of  columns userID and ISBN in validation to reads_val

<p align="center">
    <img src="images/053.png" width="80%" height="80%">


*  Train word2vec model

 <p align="center">
    <img src="images/042.png" width="80%" height="80%">

* Precompute L2-normalized vectors

* Check text and weight shape in model 

<p align="center">
    <img src="images/054.png" width="80%" height="80%">


*  Extract **ISBN** and **BookTitle** and Remove duplicates 

    <p align="center">
    <img src="images/043.png" width="80%" height="80%">


* Choose Title equal **Lord of the Rings** to sample

<p align="center">
    <img src="images/055.png" width="80%" height="80%">



*  Extract most similar products for the input vector


*  Extract name and similarity score of the similar products


<p align="center">
    <img src="images/044.png" width="80%" height="80%">




* Predict Recommend

        similar_books(model['0446520802'])



<p align="center">
    <img src="images/045.png" width="80%" height="80%">

<p align="center">
    <img src="images/046.png" width="80%" height="80%">
