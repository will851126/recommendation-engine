
# Book recommendation system 

## Scenario 

part 1:

In this part , we use the **Book-Crossing** datasets to showcase how can use [Azure notebook](https://docs.microsoft.com/en-us/azure/notebooks/azure-notebooks-overview) for built book rcommender System base on **Word2Vec** model , and goal is to **predict What book do users favorite**


Part 2: 

In this part , we can develpomnet web page  using **Flask API** and then recommendation outcome upload to blob , use **Logic APP**  monitor storage when a blob is added or modified , trigger **Send email** function


## Prerequisite

> To have Microsoft Account or a work or school account

> Install [Visual Studio Code](https://code.visualstudio.com/)

> Install Anaconda or [Miniconda](https://docs.conda.io/en/latest/miniconda.html "Miniconda下載頁面")

> Install Git




## Sign in  Azure Notebooks


1. Select Sign in on the top right of Azure notebook (notebooks.azure.com)

<p align="center">
    <img src="main/images/01.png" width="80%" height="80%">

2. Enter the email address of a Microsoft Account or a work or school account and select **Next**.

<p align="center">
    <img src="main/images/02.png" width="50%" height="80%">

3. Enter your password when prompted

<p align="center">
    <img src="main/images/03.png" width="50%" height="80%">

4. Azure Notebooks asks for permission to access your account. Select **Yes** to continue

<p align="center">
    <img src="main/images/04.png" width="30%" height="80%">

5. After successfully signing in, Azure Notebooks navigates to your public profile page

<p align="center">
    <img src="main/images/05.png" width="80%" height="80%">


## Upload local file in Azure Notebooks

1. From your public profile page, select **My Projects** at the top of the page

<p align="center">
    <img src="main/images/06.png" width="80%" height="80%">

2. Enter appropriate values for the notebook in the Project name

<p align="center">
    <img src="main/images/07.png" width="80%" height="80%">
<p align="center">
    <img src="main/images/08.png" width="80%" height="80%">

3. On the project page, select Upload ,then select **From computer** 
<p align="center">
    <img src="main/images/09.png" width="80%" height="80%">

4. Select **Choose Files** 
<p align="center">
    <img src="main/images/010.png" width="80%" height="80%">

5. Select file **book folder**  which is in this repository in your computer folder

<p align="center">
    <img src="main/images/015.png" width="50%" height="80%">

6. click **Upload**, and wait for about 5 minutes.

<p align="center">
    <img src="main/images/056.png" width="50%" height="80%">


## Train processing

*  Detail train processing  information for [book_recommendation](main/README)


## Train Result
    similar_books(model['0446520802'])

<p align="center">
    <img src="main/images/045.png" width="80%" height="80%">


    similar_books(model['034545104X'])
<p align="center">
    <img src="main/images/046.png" width="80%" height="80%">

## Create Storage as Container

1. Sign in to the Azure portal ,and in the upper-left corner of Azure portal, select **Storage Accounts**

<p align="center">
    <img src="flask/images/007.png" width="20%" height="50%">

2. Select your **Storage Account**, if you have not **Storage Account**, create new

<img src="flask/images/011.png" width="80%" height="80%">
<p align="center">
    

3. Click **Container**

<img src="flask/images/008.png" width="80%" height="80%">

4. Click **add Container**

<img src="flask/images/009.png" width="80%" height="80%">



* Name: **your unique name**
* Public access level : **Container**

<img src="flask/images/010.png" width="80%" height="80%">

5. Click **OK**




## Implement Flask API

* **Detail Flask design** information for [Flask documents](Flask/README)

1-1. Open  **Flask** folder in VS code

<p align="center">
    <img src="Flask/images/002.png" width="80%" height="80%">


1-2. Modify code for storage SDK information in line 103 to 110

 * Account Name: `your storage Account name`

 * Account key: `your storage Account Key`

* ContainerName: `yor container name`

<p align="center">
    <img src="Flask/images/012.png" width="80%" height="80%">

<p align="center">
    <img src="Flask/images/013.png" width="80%" height="80%">

* Account key: `your storage Account Key`


<p align="center">
    <img src="Flask/images/014.png" width="80%" height="80%">

* ContainerName: `yor container name`

<p align="center">
    <img src="Flask/images/015.png" width="80%" height="80%">


1-3. Enter `cd Flask` 

<p align="center">
    <img src="Flask/images/050.png" width="80%" height="80%">

1-4. Implement  **Flask API**  on localhost using `python app.py`

<p align="center">
    <img src="Flask/images/003.png" width="80%" height="80%">



1-5. **Click + CTRL** click URL to page

<p align="center">
    <img src="Flask/images/004.png" width="80%" height="80%">


1-6. Enter **ISBN** , and Click **Submit**


<p align="center">
    <img src="Flask/images/005.png" width="80%" height="80%">


* If the input ISBN is misspelled or does not exist in the database ,then show **error page** 

<p align="center">
    <img src="Flask/images/01.png" width="80%" height="80%">


* If a **correct ISBN** is entred & present in the database , then show the recommendations.  

<p align="center">
    <img src="Flask/images/006.png" width="80%" height="80%">


## Check Json file whether upload to Storage

<p align="center">
    <img src="Flask/images/016.png" width="80%" height="80%">


##  Create Logic APP 

1-1.  On the Azure portal ,and in the upper-left corner of Azure portal, select **Create a resource**.

<p align="center">
    <img src="Flask/images/017.png" width="80%" height="80%">

1-2. Use the search bar to find **logic apps**,and click **Select**

<p align="center">
    <img src="Flask/images/018.png" width="80%" height="80%">

1-3. Click **Create logic app**

<p align="center">
    <img src="Flask/images/019.png" width="80%" height="80%">

* For Resource group , Select **your resource group**

* For **Logic App name**,Type a **your name**


* Click **Create**

<p align="center">
    <img src="Flask/images/020.png" width="80%" height="80%">


1-4. The Logic Apps Designer opens and show a page with an introduce video and commonly used triggers. Under Templates, Select **Blank Logic App**

<p align="center">
    <img src="Flask/images/021.png" width="80%" height="80%">

##  Add blob trigger

* In the search box , enter `Blob storage`,From the triggres list , Select the **When a blob is added or modified**

<p align="center">
    <img src="Flask/images/022.png" width="80%" height="80%">

1-1. Enter trigger information

* For **Connect Name**, Type a **your name**

* for **Storage Account** ,Select **your storage**

* Click **Create**

<p align="center">
    <img src="Flask/images/023.png" width="80%" height="80%">

1-2. Select Container

<p align="center">
    <img src="Flask/images/024.png" width="80%" height="80%">

1-3. Under the **When a blob is added or modified**, select **New step**

<p align="center">
    <img src="Flask/images/025.png" width="80%" height="80%">


1-4. In the search box , enter `Blob storage`,From the Action list , Select the **Get Blob content**

<p align="center">
    <img src="Flask/images/026.png" width="80%" height="80%">

* Select json file in your Blob ,and select **New step**


<p align="center">
    <img src="Flask/images/027.png" width="80%" height="80%">

1-5.  In the search box , enter `Data Operations`,
From the Action list , Select the **Parse Json**


<p align="center">
    <img src="Flask/images/028.png" width="80%" height="80%">

* In the **Parse Json**, Click **Add dynamic content** , Select **Expression** , and in the **function box** ,Input `decodeBase64(body(‘Get_blob_content’)[‘$content’])`

<p align="center">
    <img src="Flask/images/029.png" width="50%" height="80%">

* In the **Schema** , input`{}`


* Click **OK**

<p align="center">
    <img src="Flask/images/030.png" width="80%" height="80%">

* Click **Save**

<p align="center">
    <img src="Flask/images/031.png" width="80%" height="80%">


## Test logic app

1-1. In the Flask API web ,Enter **ISBN**

<p align="center">
    <img src="Flask/images/005.png" width="80%" height="80%">


1-2. In the Logic apps , Select **overview**, and Click **Run Trigger**, wait after seconds , check**Run history** ,check whether succeeded

<p align="center">
    <img src="Flask/images/032.png" width="80%" height="80%">

1-3. Click **succeeded Run history** , and then select **Parson JSON**, can see outputs , **Copy all** 

<p align="center">
    <img src="Flask/images/033.png" width="80%" height="80%">

1-4. In the Logic App Designer , Select **Parson JSON**, and click **Use sample payload to generate scheme**

<p align="center">
    <img src="Flask/images/034.png" width="80%" height="80%">

1-5. In the sample JSON payload, **paste content** ,and Click **Done**

<p align="center">
    <img src="Flask/images/035.png" width="80%" height="80%">

## Add send email  trigger

1-1. Click **New step**

1-2. In the search box , enter `Office 365 Outlook`,From the Action list , Select the **Send an email**
<p align="center">
    <img src="Flask/images/036.png" width="80%" height="80%">

1-3. Sign in Office 365 Outlook

<p align="center">
    <img src="Flask/images/037.png" width="80%" height="80%">

1-4. Select Microsoft Office Account 

<p align="center">
    <img src="Flask/images/038.png" width="80%" height="80%">

1-5. Enter email information:

* To: type **your email account**

* subject: type`Rcommendation for you`


* Body design reference this 

<p align="center">
    <img src="Flask/images/039.png" width="80%" height="80%">


1-6. Add dynamic content

* Click **Add dynamic content**

* Select Parse JSON ,and click **see more**

* for each item , Select **Second** object 

<p align="center">
    <img src="Flask/images/040.png" width="80%" height="80%">


## check mail

1-1. 1-1. In the Flask API web ,Enter **ISBN**

<p align="center">
    <img src="Flask/images/005.png" width="80%" height="80%">


1-2. In the Logic apps , Select **overview**, and Click **Run Trigger**, wait after seconds 

<p align="center">
    <img src="Flask/images/032.png" width="80%" height="80%">


1-3. Check email

<p align="center">
    <img src="Flask/images/041.png" width="80%" height="80%">


##  Conclusion

Congratulations! You now have learned how to:

1. Train Recommendation model on Azure notebook

2. Use Flask API coneect model 

3. Recommendation outcome present in html

4. Use Vscode upload file to storage

5. Use logic app to send email 

## Clean up Resource

In the resource group,**Delete resource**

* Storage account

* Logic App

* API connection

