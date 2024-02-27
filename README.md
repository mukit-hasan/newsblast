# Django Newsletter App

This repository contains a Django project for a newsletter application. Users can subscribe to weekly or monthly newsletters by providing their email addresses.

## Requirements

- Docker
- Docker Compose

## Getting Started

To set up the project locally using Docker, follow these steps:

**1. Clone the repository:**<br>
   ``git clone https://github.com/your-username/django-newsletter-app.git``<br>
   ``cd django-newsletter-app``<br>

**2. Setup your smpt mail service:** <br>
on main/host_mail.json folder<br>

```{  
    "name": "yourname",
    "email": "you@mail.com",
    "password": "yourpassword",
    "host": "smtp.gmail.com",
    "port": "587"
}```

change yourname with your name<br>
change you@mail.com with your Email<br>
change yourpassword with your password<br>
change smtp.gmail.com wiht your email service addresses<br>
change port number with the port you like to change with,<br>

**3. Build and run the Docker containers:**<br>
``docker build -t appname . # for windows``
``docker-compose up -d --build # for linux``
``    #Create a superuser (optional)``
``docker-compose exec web python manage.py createsuperuser``
<br>
