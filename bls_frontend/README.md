# Frontend Vue App
## Lokale Entwicklung
### Projekt initialisieren
```
npm install
```

### Compilen und lokal ausführen mit Hot-Reload
```
npm run serve
```

Beachte, dass das Backend seperat gestartet werden muss, damit Urteile angezeigt werden
(Neben dem Backend muss zudem eine SSH-Verbindung zum rzssh1 Server bestehen, damit das Backend mit der Datenbank kommunizieren kann).

## Deployment

### Compilen und Dateien fürs Deployment erstellen
```
npm run build
```
Liefert zum einen 'dist'-Ordner und 'BLS_Tool.war' file

### Deployment auf Tomcat server
1. Auf den [Tomcat manager](http://basecamp-demos.informatik.uni-hamburg.de:8080/manager/html/) des basecamp gehen 
2. Einloggen 
3. Aktive Instanz von BLS_Tool undeployen
4. Neue Version von BLS_Tool.war hochladen

### Deployment über Apache
1. Dist Ordner, der über build erstellt wurde mit
```
scp -r dist/* ba-proj-bls2021@basecamp-demos:/var/www/html/BLS_Tool
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auf basecamp-demos Server verschieben
2. Rechte der Dateien lesbar für www-data machen
```
chmod -R 755 *
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In BLS_Tool Ordner auf basecamp-demos Server ausführen
