# 1. Uzmi zvaničnu Python sliku kao podlogu
FROM python:3.10-slim

# 2. Postavi radni folder unutar kontejnera
WORKDIR /app

# 3. Kopiraj naš kod sa laptopa u kontejner
COPY app.py .

# 4. Instaliraj potrebne biblioteke unutar kontejnera
RUN pip install flask requests

# 5. Otvori port 5000 na kontejneru da mu možemo pristupiti
EXPOSE 5000

# 6. Komanda koja pokreće aplikaciju kada se kontejner upali
CMD ["python", "app.py"]
