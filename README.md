# Django

A Django starter template as per the docs: https://docs.djangoproject.com/en/5.0/intro/tutorial01/


1. Activate the Virtual Environment
For Windows:
venv\Scripts\activate.bat

For Unix/Linux/Mac:
source source/bin/activate


2. Install Dependencies
pip install -r mysite/requirements.txt


3. Navigate to the Project Directory
cd mysite


4. Apply Database Migrations
python manage.py migrate


5. Create a Superuser (Only on first setup)
python manage.py createsuperuser


6. Run the Development Server
python manage.py runserver


7. Access the Application
Open your browser and navigate to:
Main site: http://127.0.0.1:8000/
Admin panel: http://127.0.0.1:8000/admin/ (after creating superuser)