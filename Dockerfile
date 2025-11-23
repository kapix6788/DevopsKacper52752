# --- Etap 1: Budowanie (Builder) ---
FROM python:3.9-slim as builder

WORKDIR /app

# Kopiujemy pliki zależności i instalujemy je
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# --- Etap 2: Obraz końcowy (Final) ---
FROM python:3.9-slim

WORKDIR /app

# Kopiujemy zainstalowane pakiety z etapu buildera
COPY --from=builder /root/.local /root/.local
COPY . .

# Ustawiamy zmienną środowiskową PATH, aby widzieć pakiety zainstalowane przez --user
ENV PATH=/root/.local/bin:$PATH

# Otwieramy port
EXPOSE 5000

# Uruchamiamy aplikację
CMD ["python", "app.py"]