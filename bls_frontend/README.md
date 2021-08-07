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
1. 'env.production' Anpassen für http, also in API_URL Port ':8080' hinzufügen und vorne zu http ändern
2. Auf den [Tomcat manager](http://basecamp-demos.informatik.uni-hamburg.de:8080/manager/html/) des basecamp gehen 
3. Einloggen 
4. Aktive Instanz von BLS_Tool undeployen
5. Neue Version von BLS_Tool.war hochladen

### Deployment über Apache
1. 'env.production' Anpassen für https, also in API_URL Port entfernen und vorne zu https ändern
2. Dist Ordner, der über build erstellt wurde auf basecamp-demos Server verschieben
   (Am einfachsten mit Tools wie win-scp
   Dist Ordner erst auf eigenes Konto auf Informatik Server legen und dann unteren Befehl von Informatik Server aus)
```
scp -r dist/* ba-proj-bls2021@basecamp-demos:/var/www/html/BLS_Tool
```
3. Rechte der Dateien lesbar für www-data machen
```
ssh ba-proj-bls2021@basecamp-demos
cd /var/www/html/BLS_Tool
chmod -R 755 *
```