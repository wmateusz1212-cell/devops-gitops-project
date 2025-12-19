# Startujemy od lekkiego obrazu Linuxa z Pythonem (wersja slim waży mało)
FROM python:3.9-slim

# Ustawiamy katalog roboczy wewnątrz kontenera
WORKDIR /app

# Najpierw kopiujemy TYLKO listę bibliotek
COPY requirements.txt .

# Instalujemy biblioteki. Robimy to PRZED skopiowaniem kodu aplikacji.
# Dzięki temu, jak zmienisz tylko kod w app.py, Docker nie będzie musiał
# od nowa instalować bibliotek (użyje cache). To oszczędza minuty przy budowaniu!
RUN pip install --no-cache-dir -r requirements.txt

# Teraz kopiujemy resztę plików (app.py)
COPY . .

# Informacja, że apka działa na porcie 5000
EXPOSE 5000

# Komenda startowa
CMD ["python", "app.py"]
