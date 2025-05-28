# School Prefectorial Elections Portal 🎓🗳️

This is a Django-based web app for managing school elections. Students can vote for prefects online, and admins can view results in real time.

## 🚀 Features

- Student authentication
- Vote submission (one vote per student)
- Live results tally per position
- Admin management via Django admin
- Secure voting (prevents duplicate votes)

## 📦 Requirements

- Python 3.8+
- Django 4.x
- SQLite or PostgreSQL (optional for deployment)
- Git

## ⚙️ Installation

```bash
git clone https://github.com/your-username/school-elections.git
cd school-elections
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # to access admin
python manage.py runserver
