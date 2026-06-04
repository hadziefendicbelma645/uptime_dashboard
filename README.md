# 📊 DevOps Uptime Monitor — Projekt 2

Ovo je jednostavna i efikasna web aplikacija za nadgledanje (monitoring) dostupnosti web stranica, razvijena u Flasku i zapakovana pomoću Dockera. Projekt demonstrira osnove DevOps ciklusa, uključujući dockerizaciju i automatizaciju kroz CI/CD pipeline.

## Tehnologije
* **Python** & **Flask** (Backend i web prikaz)
* **Requests** (Provjera statusa sajtova)
* **Docker** (Kontejnerizacija aplikacije)
* **GitHub Actions** (CI/CD automatizacija build procesa)

##  Kako pokrenuti projekt lokalno preko Dockera

1. **Izgradite Docker sliku:**
   ```bash
   docker build -t moj-uptime-monitor .
