# Page-Rank-Calculator
[Zur Aufgabenstellung](https://tbseins.sharepoint.com/:w:/s/ITF24c/IQB50JUqfNfUSpXmlseHXHZoATWiFDiqy0Qk-nEhEM8nwmg "Aufgabe in Word öffnen")

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

### Programm ausführen

```powershell
python main.py
```