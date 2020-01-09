# Cinemaspace

## Description
Task 2 project for the Large-Scale and Multi-Structured Databases course of the Master of Science in Computer Engineering, University of Pisa.  

## Install

The project can run either on a MongoDB replica set or on a MongoDB single server.  If you want to run in single server mode, 
please refer to the code inside the `single_server_version` branch.

| :warning: ATTENTION: the dataset is large and the replication process can take a long time. </br> It is suggested to run the application in single server mode. |
|:--- |

 
- Import the Eclipse Maven project
- Set up a MongoDB replica set or a MongoDB single server
- Update `configuration.xml` according to the database configuration (name of the set, addresses and ports of the nodes)
- Unzip the MongoDB dump file and restore the database using `mongorestore`
- Execute from `cinemaspace.controller.CinemaSpaceLauncher`

For more details, please refer to the specification document.
  
## Dataset credits

The population of the database has been done starting from the pre-existing public dataset [The Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset).  
The dataset has been manipulated using Python (Pandas and JSON libraries) in order to reflect the design choiches.  
The final set is characterized by:
- a total dump size of 1.52 GB;
- 46.6K films;
- 270.9K users;
- 11.4M ratings.

## Contributors
[Marie Giannoni](https://github.com/mariegiannoni)  
[Shirley Caillere](https://github.com/shca10766)  
[Francisco Payés Erroa](https://github.com/fxisco) 
