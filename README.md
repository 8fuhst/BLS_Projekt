# Projekt Base.Camp21 BLS_Projekt

This project was created in the course of the [Base.Camp-Project](https://www.inf.uni-hamburg.de/inst/basecamp/projects/ba-projekt.html) 2021 Module at University of Hamburg in cooperation with the [Bucerius Law School](https://www.law-school.de/).

The main topic of this project is legal tech. The goal was to create an application that processes and visualizes court judgments by using existig verdicts of the german high courts startig from 2010 onwards.  
The used data can be found on:  
https://www.rechtsprechung-im-internet.de

The demo of the application can be found on:  
http://basecamp-demos.informatik.uni-hamburg.de:8080/BLS_Tool/  
or  
https://basecamp-demos.informatik.uni-hamburg.de/BLS_Tool/
![GitHub Logo](listenansicht.png)

## Scraping
### Creating new ES Index from scratch
1. Ensure the ES Configuration of the variable "es" in [scraper/database_update.py](https://github.com/8fuhst/BLS_Projekt/blob/master/scraper/database_update.py) is set up correctly. Default is localhost:9200 with timeout set to 60.
2. Ensure that the Watson API Key and Link are present in your credentials.txt.
3. Call initialize_database() in __name__ == '__main__' instead of update_database().
4. Run the database_update.py. You can use the console with  
`python3 database_update.py`

### Updating ES Index
1. Ensure that the links.txt and present_documents.txt exsists in the current directory, they are containing the URLs/Filenumbers of all files already in the DB. If it is, you have to reinitialize the DB to update.
2. Ensure that the Watson API Key and Link are present in your credentials.txt.
3. Run the database_update.py in the [bls_backend/scraper](https://github.com/8fuhst/BLS_Projekt/tree/master/scraper) module.

### Reinitializing
1. Just do "Creating new ES Index from scratch". You will be asked ist you want to overwrite existig indeces.

You can set up regular updates with the database_update.py file using automation tools like Cron!

## Backend
### Elasticsearch
First make sure that the Elasticsearch Database is setup properly in BLS_Projekt/bls_backend/src/main/java/com/bls_tool/repositories/Config.java, default is localhost:9200.

Usefull console commands are:

`curl -XGET basecamp-bigdata:9200/_cat/indices?v`  
if you want to check out the "verdict" index

`curl -XDELETE basecamp-bigdata:9200/verdicts`  
if you want to delete the "verdict" index

`curl -X GET "basecamp-bigdata:9200/verdicts/_search?pretty" -H 'Content-Type: application/json' -d' {   "query": {     "match_all": { }   } } '`  
and  
`curl -X GET "basecamp-bigdata:9200/verdict_nodes/_search?pretty" -H 'Content-Type: application/json' -d' {   "query": {     "match_all": { }   } } '`  
if you want to check if there are existing entries in the indices "verdicts" and "verdict_nodes".

### Building
Build the bls_backend Java project using Maven with the following commands
```
mvn clean
mvn install
mvn package
```

Now there should be a .war file containing the project within the bls_backend target folder called bls_backend-0.0.1-SNAPSHOT.war.

### Deployment on Tomcat
1. Go to the Tomcat Manager of the basecamp or your own server
2. Log in
3. Undeploy currently active version of bls_backend-0.0.1-SNAPSHOT
4. Upload and deploy new version of bls_backend-0.0.1-SNAPSHOT
Now there should be a .war file containing the project within the bls_backend target folder. This .war file can be used to deploy on any Tomcat or Apache server.
There is also a deployed version running on http://basecamp-demos.informatik.uni-hamburg.de:8080/bls_backend-0.0.1-SNAPSHOT.

### Apache Version 
The Apache version of the backend runs on https://basecamp-demos.informatik.uni-hamburg.de/bls_backend.

## Frontend
The frontend is a seperate Vue-app. For further details on deployment and local development see README in the ['bls_frontend'](https://github.com/8fuhst/BLS_Projekt/tree/master/bls_frontend) folder.
