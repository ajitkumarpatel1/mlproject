## END TO END MACHINE LEARNING PROJECT
# STUDENT PERFORMANCE INDECATOR 

### Software And Tools Requirements

1. [Github Account](https://github.com)
2. [AWS](https://aws.amazon.com/console/)
3. [VSCodeIDE](https://code.visualstudio.com/)
4. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)
5. [PostMan](https://www.postman.com/downloads/)

Create a new environment

```
conda create -p venv python==3.8 -y
```
### Creating a web app which take input from user and send to the backend through flask api and give to the model.pkl,preprocessor.pkl file and in results its give the out.
activate envionment 
```
conda activate C:\Users\AJIT\jupiter_cvv\mlproject\venv
```

# STEPS TO FOLLOW :
### 1.github repo (mlproject)

### 2.make a folder(mlproject) on local system

### 3.open anaconda promt
#### (command) 
```
1.cd local/folder/path
```
(to open vscode)
```
2.code . 
```

### 4.open a new terminal(cmd)
                        (command) 1.conda create -p venv python==3.8 -y
                                  2.conda activater venv/

### 5.sink localrepo with git & github (cmd)
                        (command) 1.git init (Initialized empty Git repository)
                                  2.git add README.md (or manualy Add a README.md file by Vscode)
                                  3.git commit -m "first commit" (commiting the staging area file with a message)
                                  4.git branch -M main (check in to the main brach of github)
                                  5.git remote add origin https://github.com/ajitkumarpatel1/mlproject.git  (sink the local repo and vartual repo)
                                  6.git remote -v (try check the remote conecction connected)
                                  7.git config --global user.name "ajitkumarpatel1" (adding the github username)
                                  8.git config --global user.email "1ajitkumarpatel@gmail.com" (adding the github gmail)
                                  9.git push -u origin main

### 6.Creating .gitignore file directly on github  (Add file >Create new file >.gitignore(name) > python(choose)> add mcommit message> commit change)

### 7.git pull (pulling the updated directore)

### 8.Creating "setup.py" (it is used to defined the project metadata and dependencies as well as to facilatate the distrubution and installation of the project)

### 9.Creating "requirements.txt"   (pip install -r requirement.txt)

### 10.creating a "src" folder (src-source,implementing everything(module) of this project is comes insude this.It make up the core of the project)
                          ("src" folder often include scripts for data preprocessing, model training, model evaluation, and prediction.)
                                SRC FILE STREACTURE
                               -------------------
                                1. __init__.py
                                2. components ("components" folder in a ml project can be used to organize all the module of a project ex-data injection,preprocessing upto deployment)  
                                      a) __init__.py (component will be created as a package it can be exported or imported to some other file location)
                                      b)data_injection.py (it uses to a)Entered the data ingestion method or component
                                                                      b)Read the dataset as dataframe
                                                                      c)Train test split initiated
                                                                      d)Inmgestion of the data iss completed
                                      c)data_transformation.py (it uses to transform the data into their actual form by the help of two function
                                                                      a)1st function:"get_data_transformer_object" it is the function which do pree processing
                                                                      b)2nd function:"initiate_data_transformation" it call the 1st function and do the pree processing,devide the train
                                                                        dataset into independent and dependent, save the dataset into a memory location "artifacts"///lineno 110  
                                                                        "save_object" is save in the utils file (go to utils file)
                                      d)model_trainer.py (hear all the train code of the model as well as score the accuracy of the model is present which are writen in MODEL TRAIN.ipynb)
                                3. pipeline (it contain 2 files - train pipeline and prediction pipeline)
                                      a)__init__.py
                                      b)train_pipeline.py (it contain all the code for traning pipeline and it call automatically all the file need for training inside "component folder")
                                      c)predict_pipeline.py (creating the app.py files(16) in this using flask 
                                4. logger.py file (this file is for saving the log details which occurs in this project like execution etc so we can track if any errors)
                                5. exception.py file (this is for exception handling purpose)
                                6. utils.py file (all the functonality/evaluation methods of project flow is writen over hear)
                                                 

### 11.Creating "notebook" folder (it contain the data folder, EDA STUDENT PERFORMANCE.ipynb, MODEL TRAINING.ipynb)
                                1.data>stud.csv  (data is the folder which contain the students data as csv format)
                                2.EDA STUDENT PERFORMANCE.ipynb (Hear all the eda are done for this project {jupiter notebook}
                                                                a)
                                3.MODEL TRAINING.ipynb (Hear all the machine learning model is implemented and choose the best model for this dataset {jupiter notebook}
                                (Open all this file in vs code 1.select python enterpreter and run all the code in vs code for model traning we need to import the sklearn in our project    
                                inveronment {pudate "scikit-learn","catboost","xgboost" in requirement.txt and use the command cmd---->pip install -r requirement.txt})====imp

### 12. working with :"src/component/data_injection.py files  
                               (a)import requird lib 7, 
                                b)for saving traning data,testing data,raw data, from multiple sources making a class "DataIngestionConfig" and it give the output as a "artifacts files" -train.csv, test.csv, data.csv ,
                                c)we need to put the artifacts files into .gitignore file #environment".artifacts"
### 13. working with :"src/component/data_injection.py files ----------read the src/component/data_transformation.py 
### 14. working with :"src/component/model_trainer.py files------------ adding all the functonality to it and connect with the utils.py file
### 15. working with :"src/pipeline/predict_pipeline.py-------------READ THAT
### 16. making a file "app.py" (it contain the flask app ---17
### 17. making a file "index.html"  --it contain all the forntend related files
                                1.index.html (it contain the html code for frontend Welcome page)
                                2.Home.html  (it contain the html code for frontend input page )
