# Amazon_copy
**version 1.0.0**
#### Video Demo:  <https://youtu.be/QMjsjlV8cOc> 
## License & copyright :
© Amde , Amin Nazari
## Contributors : 
- Mohammad Amin Nazari Moghadam
#### Description :  
This project is a Webapplication python project. Its backend is desigend with flask and the frontend is basicly some html pages with styles . You can Register with E-mail and You will recieve an E-mail and You can continue Your registeration with a link in Your E-mail . You have the ability to Login and Logout and change Your password or recover it. The main function of this site is that You can get Amazon.com 's products and you can add or remove them from your shoppingcart.
## function of each file :
### 1. application.py :
this python file organizes the main flask works and each path is provided there . 
### 2. search_engine.py :
This file does the data_collecting job. It goes to amazons website and scrapes the data using selenium , chromedriver and soup libraries.
### 3. helpers.py :
this file contains the hash functions and  used for checking and saving passwords of customers.
### 4. app.js :
js codes and making the website static and ajax used for transforming datas in some parts.
### 5. vendor.js : 
designing swiper and shaping it .
### 6. main.sql :
creating the database using queries .
### 7. info.db :
Database file including 2 tables. One for Users and the Other for shoppingcart data.

*first an api was used for data* Then i decided that I extract data myself. and the small delay for loading some pages is related to this.
for transforming data in 2 functions i used javascript and ajax . Later there can be a new ability be enabled that purchase something for real but this at first step needs a real shop and something further than just a simple web developing and designing.
the delay time for loading pages is related to data-collection from amazon . an api could decrease the loading time.


## experience:
A front-end framework could be used instead of simple css & html layouts but I didnt have enough knoweldge to use that . This was actually my fisrt real web-application using flask . I really enjoyed it and I have became intrested in it
to add all libraries You can use pip in your terminal using this command :

`pip install -r requirements.txt `

if you faced this error : 

Error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory.

try these codes in your termianl :

`set FLASK_APP=application.py`

`$env:FLASK_APP = "application.py"`

To run the application :

`flask run`
#### Swiper
the swiper is used from https://swiperjs.com
You can go visit diffrent Swipers and  use them.



