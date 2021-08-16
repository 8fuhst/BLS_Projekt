# Frontend Vue App
## Local development
### Initialize project
```
npm install
```

### Compile and execute with hot-reload
```
npm run serve
```

Note, that the backend has to be started seperately to
display verdicts (additionally there has to be a running
SSH-connection to the rzssh1 server, so the backend can
communicate with the database).


## Deployment

### Compile and create data for deployment
```
npm run build
```
Creates a 'dist'-folder and 'BLS_Tool.war' file

### Deployment on Tomcat server
1. Adapt 'env.production' for deployment on tomcat
2. Build the app
   ```
   npm run build
   ```
3. Go to the basecamp [Tomcat manager](http://basecamp-demos.informatik.uni-hamburg.de:8080/manager/html/) 
4. Log in 
5. Undeploy active instance of BLS_Tool
6. Upload new version of 'BLS_Tool.war'

### Deployment through Apache
1. Adapt 'env.production' for deployment through apache
2. Build the app
   ```
   npm run build
   ```
3. Move the dist folder, that got created after build, onto the basecamp-demos server.
   (You can use a tool like 'win-scp' to move folder onto own account on computer-science server, then use below command from there)
   ```
   scp -r dist/* ba-proj-bls2021@basecamp-demos:/var/www/html/BLS_Tool
   ```
4. Change permissions of the file, so it's readable for 'www-data'
   ```
   ssh ba-proj-bls2021@basecamp-demos
   cd /var/www/html/BLS_Tool
   chmod -R 755 *
   ```