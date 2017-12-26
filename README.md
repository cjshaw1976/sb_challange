# View Demo
This project can currently be for running at http://cjshaw.pythonanywhere.com/


# Getting Started
Installing on local computer.

To run this project, your local computer requires Python 3 installed. There are plenty of recourses on the internet to describe how to install Python 3 on different operating systems.

These instructions are for a Linux based environment. Download and unzip the project from github.
cd into the folder sb_challenge-master and create a virtual environment in the folder .p3 with the command `python3 -m venv .p3`.
Next, activate the environment source `.p3/bin/activate`. Install the required project files with the command `pip install -r requirements.txt`.

Before starting the server, you need to initialize the database. cd into the folder sb_protect and run the command `python manage.py makemigrations` followed by `python manage.py migrate`. You will need to create a superuser with the command `python manage.py createsuperuser`. You will be prompted for a username, email and password. This will be your first staff user. You can log into the django admin with this combination to add more staff. To run the project, use the command `python manage.py runserver`. You will then be able to open the project frontend in your browser http://127.0.0.1:8000 or django admin http://127.0.0.1:8000/admin.
