# ChatBox

ChatBox este o aplicație web de conversație bazată pe LLM, care oferă atât un plan gratuit, cât și premium. Aplicația permite utilizatorilor să trimită mesaje și să interacționeze cu modele AI avansate:

- **LLM gratuit:** LLaMA 3.2

- **LLM premium:** GPT-OSS:20B

Funcționalități principale:

- Crearea unui cont de utilizator și autentificare.
- Acces la istoricul conversațiilor.
- Gestionarea datelor personale ale utilizatorului.
- Inserarea de documente pentru ca LLM-ul să le folosească în conversații.
- Schimbarea planului/abonamentului între versiunea gratuită și cea premium.”
- Admin panel disponibil atât pe backend (VMC custom), cât și în frontend-ul web pentru gestionarea aplicației.

## Cerințe de sistem

### Cerințe minime

- **Placă video:** NVIDIA RTX 3050 Ti cu 4 GB VRAM
- **Procesor:** AMD Ryzen 7 6800H
- **Memorie RAM:** 16 GB DDR5
- **Sistem de operare:** Arch Linux

### Cerințe recomandate

- **Placă video:** NVIDIA RTX 4070 cu 8 GB VRAM
- **Procesor:** AMD Ryzen 7 7745HX
- **Memorie RAM:** 32 GB DDR5
- **Sistem de operare:** Arch Linux

## Scop

Acest proiect este realizat pentru laboratorul de Paradigme de proiectare a aplicațiilor web, având ca scop implementarea unei aplicații web cu conversație LLM și opțiuni de scalabilitate.

## Tehnologii

- **Backend**: Django
- **Frontend**: React + Vite
- **Database:** MySQL

## Instalare

Urmează pașii de mai jos pentru a instala și configura proiectul.

1. Clonează repository-ul folosind comanda:

```bash
git clone https://github.com/Xhadrines/ChatBox.git
```

2. Pentru a configura backend-ul, accesează [backend/README.md](backend/README.md), unde vei găsi informațiile necesare.

3. Pentru a configura frontend-ul, accesează [frontend/README.md](frontend/README.md), unde vei găsi informațiile necesare.

4. După ce ai pornit backend-ul și frontend-ul, deschide aplicația în browser accesând linkul generat de frontend `http://127.0.0.1:2002/`.
