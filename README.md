# QRCoder application

Application for generating and saving QR Codes with login system based on the Django framework

__________________


## Screenshots

![Login and Signup forms](https://raw.githubusercontent.com/CosmoSt4r/qrcoder-app/assets/account.png)

You can *register* or *login* if you already have an account.

_________

![Homepage](https://raw.githubusercontent.com/CosmoSt4r/qrcoder-app/assets/home.png)

Press *Edit* button on the upper right to add new or edit existing QR code

_________

![QR Code](https://raw.githubusercontent.com/CosmoSt4r/qrcoder-app/assets/qrcode.png)

Press *Show* to get the QR Code. You can also download it if you want to

## How to install?

### Clone

Clone this repo to your local machine using `https://github.com/CosmoSt4r/qrcoder-app`

### Required packages

To start the server you need the following packages: 

 - Django
 - requests

> go to project folder and type

```py
pip install -r requirements.txt
```

### Starting the server

Before starting the server you have to specify environment variables

| Parameter    | Description                |
| :----------- | :------------------------- |
| `IS_DEBUG`   | set `False` if running in production |
| `SECRET_KEY` | large random value |
| `HOST`       | your hostname, ex.: `appname.heroku.com` |

Open terminal in project folder and type:

```py
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Opening app in browser

Open your browser and go to the `127.0.0.1:8000` (or your host specified in env variables) address. You will see the main page.

## Credits

 - Frontend made using [Bootstrap](https://getbootstrap.com/)
 - QR Codes generated with [imagecharts](https://documentation.image-charts.com/qr-codes/) API 
