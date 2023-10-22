# Description
<p>In this project, it is aimed to create an application where staff users can create personnel, update, delete or read personnel they have created. Users without staff feature will be able to read all staff. We also used class-based views to create custom functions and override some methods.👷🏻</p>

# Models

- Personnel
- Department
- User

![Model](https://github.com/sultankeles/personnel_app/blob/master/personnal_app_erd.jpeg)

# Department

    - Client_User
        - view department only

    - Staff_User
        - CRUD department

# Personnel

    - Client_User
        - view personnel only

    - Staff_User
        - CRUD personnel (their own personnel)

<!-- # Live Project -->

<!-- - <a href="https://pakize.pythonanywhere.com/">Live of the project</a>
- <a href="https://pakize.pythonanywhere.com/swagger/">For the swagger of the project</a> -->

# Personnal App Installation

<p>Here's an example of how you can instruct your audience to download and install your app. This template is not based on any external dependencies or services.</p>

1- python venv installation
python -m venv <venv_name>

2- env activation
Powershell => .\<venv_name>\Scripts\activate
bash => source <venv_name>/Scripts/Activate

3- Install packages
pip install -r requirements.txt

4- For database,
python manage.py migrate

5- .env file
    SECRET_KEY=

6- Create user for Admin Panel
python manage.py createsuperuser

7- The project is ready, you can start using it now
python manage.py runserver

Runs the application in development mode. To view in the browser http://127.0.0.1:8000/
open.