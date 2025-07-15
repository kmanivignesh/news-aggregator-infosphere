# 📰 news-aggregator-infosphere

**InfoSphere** is a Django-based personalized news aggregator platform that solves the problem of digital information overload by providing customized, real-time news feeds based on user preferences. The platform is designed to be accessible, feature-rich, and user-friendly.

---

## 📌 Table of Contents

- [🚀 Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [🔧 Modules](#-modules)
- [🏗️ System Architecture](#️-system-architecture)
- [📥 Installation](#-installation)
- [🔐 Usage](#-usage)
- [🔑 NewsAPI Setup](#-newsapi-setup)
- [🔍 Research Gaps Addressed](#-research-gaps-addressed)
- [📚 References](#-references)

---

## 🚀 Features

- Secure user registration and authentication
- Real-time news feed using NewsAPI
- Personalized categories based on user preferences
- Article bookmarking system
- PDF download for offline reading
- Text-to-speech (TTS) for accessible news consumption
- QR code generation for easy sharing
- Lightweight and responsive UI

---

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript (Django templates)
- **Database**: SQLite
- **APIs**: NewsAPI
- **Libraries**:
  - `requests` – API integration
  - `fpdf` – PDF generation
  - `gTTS` – Text-to-Speech
  - `qrcode` and `Pillow` – QR code generation

---

## 🔧 Modules

- `accounts/` — Handles user registration and login
- `bookmarks/` — Manages saved articles
- `news/` — News fetching logic, categorization, PDF & TTS
- `profile/` — Stores user preferences and profiles
- `qr/` — Generates QR codes for articles
- `templates/` — HTML files
- `static/` — CSS and JS assets

---

## 🏗️ System Architecture

Frontend ↔ Django Views ↔ Models ↔ SQLite  
⬆ NewsAPI integration for real-time news fetching

---

## 📥 Installation

```bash
# Clone the repo
git clone https://github.com/your-username/news-aggregator-infosphere.git
cd news-aggregator-infosphere

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # Use `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations and run the server
python manage.py migrate
python manage.py runserver
