# Page-Rank-Calculator
[Zur Aufgabenstellung](https://tbseins.sharepoint.com/:w:/s/ITF24c/IQB50JUqfNfUSpXmlseHXHZoATWiFDiqy0Qk-nEhEM8nwmg "Aufgabe in Word öffnen")

## Projekt aufsetzen

Der Page-Rank-Calculator berechnet PageRanks für die Seiten des ITF24c-Wikis
([itf24c.duckdns.org](https://itf24c.duckdns.org/)). Als Datengrundlage dient ein
Datenbank-Dump des Wikis. Die Datenbank und der Dump sind nicht im Repository
enthalten und müssen lokal bereitgestellt werden.

### Voraussetzungen

- Python 3
- MySQL oder MariaDB
- Ein SQL-Dump der Wiki-Datenbank sowie der MySQL/MariaDB-Client

### Python-Umgebung einrichten

Im Projektverzeichnis eine virtuelle Umgebung erstellen und die Abhängigkeiten
installieren:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### Datenbank erstellen und Dump importieren

Erstelle in MySQL/MariaDB eine leere Datenbank, zum Beispiel
`page_rank_calculator`:

```sql
CREATE DATABASE page_rank_calculator
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
```

Den Befehl kannst du in einer MySQL/MariaDB-Sitzung ausführen. Importiere
anschließend den SQL-Dump des Wikis in diese Datenbank.

### Datenbankverbindung konfigurieren

Lege im Projektverzeichnis eine Datei namens `.env` an und trage die Zugangsdaten
der Datenbank ein. Zum Beispiel:

```dotenv
DB_HOST=localhost
DB_USER=DEIN_DB_BENUTZER
DB_PASSWORD=DEIN_DB_PASSWORT
DB_NAME=page_rank_calculator
```

### PageRanks berechnen

Wenn Datenbank und Verbindung eingerichtet sind, starte das Programm im
Projektverzeichnis:

```powershell
python main.py
```

## Entwicklerhinweise

### Tests ausführen

Die Tests werden mit `unittest` ausgeführt:

```powershell
python -m unittest -v classes
```

### Coverage nutzen

Um die Testabdeckung zu messen und zu bewerten, verwendet man `coverage.py`:

```powershell
coverage run -m unittest -v classes
coverage report -m
coverage html
```
