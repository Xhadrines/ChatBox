# Backend

Aceasta este **partea de backend** a aplicației, construită folosind framework-ul **Django**.

## Cerințe

Pentru a rula aplicația, trebuie să ai instalat:

- **Python** (v3.13.7 sau o versiune mai mare)
- **pip** (v25.2 sau o versiune mai mare)

## Instalare

1. Asigură-te că te afli în directorul `backend`

2. Creează un fișier `.env` și adaugă următoarea linie:

```bash
DB_NAME=[DB_NAME]
DB_USER=[DB_USER]
DB_PASSWORD=[DB_PASSWORD]
DB_HOST=[DB_HOST]
DB_PORT=[DB_PORT]
HOST_USER=[HOST_USER]
HOST_PASSWORD=[HOST_PASSWORD]
```

_Note: Înlocuiește conținutul din parantezele pătrate cu valorile corespunzătoare._

3. Creează mediul virtual folosind comanda:

```bash
python -m venv .venv
```

4. Activează mediul virtual folosind comanda:

```bash
source ./.venv/bin/activate
```

5. Instalează dependențele folosind comanda:

```bash
pip install -r requirements.txt
```

6. Crează migrațiile folosind comanda:

```bash
python manage.py makemigrations
```

7. Aplică migrațiile folosind comanda:

```bash
python manage.py migrate
```

8. Instalează Ollama mergând pe [site-ul oficial Ollama](https://ollama.com/).

9. Instalează modelul gpt-oss:20b și llama 3.2 folosind comanda:

```bash
ollama pull gpt-oss:20b
```

```bash
ollama pull llama3.2
```

10. Rulează proiectul folosind comanda:

```bash
python manage.py runserver
```

11. Proiectul rulează pe `http://127.0.0.1:2307/`.
