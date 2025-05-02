# 🐾 Animal Shelter "House of Hope" 🏠

Welcome to the official repository of the **Animal Shelter "House of Hope"**! This project is a website built with Django to help manage and promote the shelter's activities. Visitors can:
- 📰 Stay updated with the latest shelter news
- 🐕 Browse the list of animals available for adoption
- 🤝 Learn how to volunteer and support the shelter

---

## 📂 Project Structure

```
.
├── .gitignore
├── docker-compose.yml
├── animal_shelter
│   ├── Dockerfile
│   ├── manage.py
│   ├── db.sqlite3
│   ├── requirements.txt
│   ├── animal_photos
│   │   ├── (Animal images)
│   ├── animal_shelter
│   │   ├── (Django core files)
│   ├── images
│   │   ├── (Additional images)
│   └── page
│       ├── (App files: models, views, templates, static assets)
```

---

## 🚀 Installation and Running

### 🖥️ Running Locally (Without Docker)

1. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # for Linux/macOS
   venv\Scripts\activate     # for Windows
   ```

2. **Install dependencies:**
   ```sh
   pip install --upgrade pip
   pip install -r animal_shelter/requirements.txt
   ```

3. **Apply migrations:**
   ```sh
   python animal_shelter/manage.py migrate
   ```

4. **Run the server:**
   ```sh
   python animal_shelter/manage.py runserver
   ```
   The site will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### 🐳 Running with Docker

1. **Ensure Docker and Docker Compose are installed.**

2. **Build and start the container:**
   ```sh
   docker-compose up --build
   ```

3. The site will be available at [http://localhost](http://localhost).

---

## ✨ Features

- **🏠 Home Page** – Information about the shelter.
- **📰 News** – The latest updates from the shelter.
- **🐾 Animal List** – Photos and details of the animals. Clicking on an animal opens a detailed page.
- **🤝 Volunteering** – Instructions and contact info for those interested in volunteering.

---

## 🛠️ Technologies Used

- **Backend:** Django 4.2
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Database:** SQLite (can be changed in the settings)
- **Containerization:** Docker

---

## 📝 Notes

- The theme (light/dark) is controlled through JavaScript located at `animal_shelter/page/static/js/switcher.js`.
- Site administration is managed via Django Admin, available at `/admin`.

---

## 📞 Contact

**Developer:** Bulat Gareev  
**Email:** gareevbulich63@gmail.com 
**Phone number** +1 215 252 0286
**Country** United States
**City:** Philadelphia

---

