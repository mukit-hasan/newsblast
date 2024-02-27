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

```
{  
    "name": "yourname",
    "email": "you@mail.com",
    "password": "yourpassword",
    "host": "smtp.gmail.com",
    "port": "587"
}
```

change yourname with your name<br>
change you@mail.com with your Email<br>
change yourpassword with your password<br>
change smtp.gmail.com wiht your email service addresses<br>
change port number with the port you like to change with,<br>

**3. Build and run the Docker containers:**<br>
``docker build -t appname . # for windows``<br>
``docker-compose up -d --build # for linux``<br>
``    #Create a superuser (optional)``<br>
``docker-compose exec web python manage.py createsuperuser``<br>

**4. APis:** <br>
In this app you can find only one api point
``http://localhost:8000/api/newsletter/ ``
using this endpoin you can subscribe and Unsubscribe to the newsletter <br> 
we can use 4 parameter to subscribe <br>
we can see an example down there where we set email=your@mail.com, name=JhoneDoe, <br> 
state=True it mean you want to subscribe if its False then you will Unsubscribe if you already subscribe for that you have to provide id for the email like id=3, and the last one is<br>
frequency=weekly you can set it to weekly or monthly for how frequently you want to receive<br> emails <br>
`` http://localhost:8000/api/newsletter/?email=your@mail.com&name=JhonDoe&state=True&frequency=weekly``

if you want to see if email is sending to users you can go to log/logfile.log from root folder<br> 
to see how many email was send and when email was sent <br>


##Contributing
If you want to Contribute, Please feel free to submit issues or pull requests.