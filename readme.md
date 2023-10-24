# Interview Organizer

**Description**

Interview Organizer is a web application built using Django and Python. It's designed to help journalists manage and organize their interviews, both upcoming and archived.

**Features**

Upcoming Interviews: Add and keep track of all upcoming interviews.
Archived Interviews: Store details of past interviews for future reference.
User Authentication: Secure login system.

**Prerequisites**

Python 3.8 or higher
Django 4.2.4

**Installation**

Clone the Repository

git clone https://github.com/your-username/interview-organizer.git

cd interview-organizer

**Setup Virtual Environment**

python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

**Install Dependencies**

pip install -r requirements.txt

**Database Setup**

The project uses SQLite as a database. If you want to use another database, modify the DATABASES setting in settings.py.

**Note**

Make sure key/filepaths are correct in settings.py

Generate SECRET_KEY:

from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())

**Migration**

python manage.py makemigrations
python manage.py migrate

**Create Superuser**

python manage.py createsuperuser

**Run Server**

python manage.py runserver
Open http://127.0.0.1:8000/ in your web browser.

**Usage**

Login/Signup: Access the application by logging in or signing up.
Upcoming Interviews: Add or edit upcoming interviews.
Archived Interviews: Access or delete archived interviews.

**Built With**

Django - The web framework used
SQLite - Database

**Contributing**
Contributions are more than welcome.

**Author**

Janne Vuorela

**License**

This project is licensed under the MIT License - see the LICENSE.md file for details.


