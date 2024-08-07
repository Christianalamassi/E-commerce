# E-commerce [(Getränke)](https://ecommercepp5-a121ad0ae944.herokuapp.com/)

## Overview

This project was designed, developed, and based on the idea of an online shop to create a simple and easy method for customers to buy drinks online. The users are given the possibility to add the order to their basket, update it, and delete it at any time before the payment. All these functionalities can be accessed by any user with an account. The admins have special permissions for controlling the data (CRUD). The website was made for real-life simulation, although the shop and drinks don't exist in real life. The website was developed using HTML, CSS, JS, Python "Django" and data are stored in an Elephant SQL database.

<img src="static/images/repersd.png">

## Features
Some elements appear on all of the pages of the website, like the navbar and the footer.

- Navbar
  - The navigation is fixed at the top of the page and easy to use. It includes three buttons "Home", "Order Here" and either "log out" and "Profile" when the user logs in "login" and " register" when the user logs out, and "Management" if the user is the superuser.
  - The navbar is responsive to different screen sizes.
  - It also contains a search button where the user can search for all the items in the offer list.

    - <img src="static/images/znavzs.png">

- Footer
    - The footer includes the contact of the shop, email, question, and social media links.

    - <img src="static/images/yzf.png">

    - Question link takes the user to leave us message page, where the user can submit their question to receive an answer from the admin.
      
    - <img src="static/images/yquestion.png">

## Home
This is the main page, and just includes background and if the user is authenticated can see the basket at the right top of the page.

<img src="static/images/zzzhom.png">

## Order Here
- This page is available to everyone.
- On this page where customers can find products and see the details of each product.
- When the user clicks on any item, it displays the item individually, where the user can add the order to the cart in the quantity a user needs, provided that it is not more than 1000
- After the user adds the items to the shopping cart, it displays the message at the top right of the page to take the user to the checkout page by clicking on the checkout button, or the user can easily click on the basket instead if they want to edit or delete some items before checkout. 
- There is a sort button where the user can sort the list according to the options.

<img src="static/images/zorderder.png">

## Profile
 For each registered user there is a personal profile page where they can find the information about their order.

<img src="static/images/zprozfizley.png">

# Checkout page
Here where the user completes the order and pays for it after filling out the delivery information.

<img src="static/images/zyyypatyyy.png">

## Authentication
  - This dropdown button includs the singup, login/out and profile buttons.

### Sign Up
On this page the user can click on "Sign Up" if the user wants to create an account.

<img src="static/images/zyzysig.png">

### Login
On this page, the user only has to enter their username and password to log in to the page. It has a link to the Sign Up page if the user has no account. The user will automatically be able to see the basket.

<img src="static/images/zlogin.png">

### Logout
When the user is logged in and clicks on "Logout" up on the navigation bar, the user will automatically be redirected to this page first. The user receives the question if they are sure they want to log out. To log out they click on the button "confirm". 

<img src="static/images/logout.png">

### Email confirmation
 After the user signs up they should receive an email asking for verification

## Other 
- The website gives the user and visitors the opportunity to ask any question they need in order to get an answer from the staff as soon as possible and to submit a request for a newsletter.
- It also allows the logged-in user to submit its opinion and give a rating.

<img src="static/images/zzzzzzzyyyyyy.png">

## UX

### Strategy

#### Project Goal
    This Project was created for an E-shop that is useful for customers and shop staff.

#### User story
-  The purpose of the project is to give the possibility for the cutomers to buy drinks online. In addition, the users have the ability to view, update (edit) and delete thier order before the payment any time they want, as long as they are logged in. The webiste is easy for the user to navigate through.

- Also, any visitor to the website can view what in the shop's list, Although they can't order untill they logged in.

    - As a User I can recover my password whenever I forgot it so that I can be able to access my profile again
    - As anAdmin I can create, edit, read and delete so that manage the E-shop
    - As a User I can have my personal profile so that I view my order and history data
    - As a User I can Add or delete the products from the basket so that I have flexibility to fix my order
    - As a User I can order and pay so that I do complete buying processes
    - As a user I can search for my product so that I don't have to keep scoring up or down to find it
    - As a User I can receive confirmation email so that I manage my order or check it out
    - As a User I can confirm my payment before complete the payment so that I have flexibility of withdrawing my order
    - As a User I can sort the products so that I find the product that I look for easily and quickly
    - As a User, I can register an account, so that I can access benefits of the project.
    - As a User I can see all the items so that I order or buy
    - As a user I can navigation easily and contact so that I can find the content
    - As a User I can see the details of each product so that I know what to order
    - As a User I can see what minimum price of order so that my order can be
    processed
    - As a Visitor I can send questions so that I receive answer for my wondering
    - As an Admin I can ask the user to subscribe so that I can have their data
    - As a User I can have my data saved so that don't have to to refill it each time I need to process

    <img src="static/images/ussseerre.png">

### Structure
The user can access the home page and Order Here page without having a profile, but to be able to order, the user must create an account. Then the user will have their own profile and basket so that they can add any item to their basket. The user will receive a text message confirming the addition with the ability to modify or delete the items from their basket. Also, if the user returns to the home page, they can still come back at any time to edit or delete from their basket. 

<img src="static/images/untitled iagram.drawioss.png">

### Scope
 - Make a clear and easy design for the users
  - Simple and intuitive User Experience.
  - Add information on contact and social media.
  - Create a responsive design for desktop, tablet, and mobile devices.
  - Allow access to the Profile page only for client type of users
  - Create an E-commerce system feature that allows the admin to display, edit, and delete the item from the shop's list.
  - Create an E-commerce system feature that allows the users to display, edit, and delete the item from the basket.
  - Create a Profile page for the user, so the user can order.

### Skeleton
The project uses the ElephentSQL relational database for storing the data. There was just one diagram created for this project.

### Surface
  - Flex-box
  - Hover effects
  - Color palette:

    - <img src='static/images/red.png'>

  - Fonts imported from fonts.googleapis [google.font](https://fonts.google.com/)
    - Lucida Grande,DejaVu Sans,
    - Bitstream Vera Sans
    - Verdana, Geneva, Tahoma, sans-serif
    - Arial 
    - Courier New Courier, monospace
    - Roboto
    
## Technologies Used

### Languages
  - [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) was used as the foundation of the site.
  - [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) was used to add the style and layout of the site.
  - [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) was used for interaction
  - [Python](https://www.python.org/) Used for back end and front end

### Frameworks:
  - [Django](https://www.djangoproject.com/) Used as a framework
  - [Jquery](https://jquery.com/) For adding predefined function between backend anf fronend 
  - [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/) For adding predefined styled elements and creating

### Other tools:
  - [Gitpod](https://www.gitpod.io/) Hosted the workspace.
  - [Heroku](https://id.heroku.com/login) Used for deploying the project.
  - [Favicon.io](https://www.favicon.cc/) Used for generating the website favicon.
  - [responsiveviewer](https://responsiveviewer.org/) used to check responsive view.
  - [Cloudinary](https://cloudinary.com/) For storing static data.
  - [Stripe](https://stripe.com/de?utm_campaign=DE_en_Search_Brand_Stripe_EXA-866170064&utm_medium=cpc&utm_source=google&ad_content=301948784636&utm_term=stripe&utm_matchtype=e&utm_adposition=&utm_device=c&gad_source=1&gclid=Cj0KCQjws560BhCuARIsAHMqE0GJZhP880Wbgg5rHfjuen4ObDsZMnwGIQHTWVUhPpRK-xsHiIacLkAaAry3EALw_wcB) for payment.
  - [privacypolicygenerator](https://www.privacypolicygenerator.info/) for privacy policy.
  - [GitHub](https://github.com/) Used for hosting the source code of the program
  - [Chrome-Del-Tools](https://developer.chrome.com/docs/devtools/) For debugging the project.
  - [Mailchimp](https://us14.admin.mailchimp.com/audience/contacts/) for subscription.
  - [W3C](https://validator.w3.org/#validate_by_input) HTML Validator Used for validating the HTML.
  - [Google-Fonts](https://fonts.google.com/) for typography.
  - [CI Python Linter](https://pep8ci.herokuapp.com/#) Used to validating Python.
  - [Font-Awesome](https://fontawesome.com/) For creating attractive UX with icons responsiveness.
  - [JsHint](https://jshint.com/) used for validating the javascript code.
  - [Jigsaw](https://jigsaw.w3.org/css-validator/) CSS Validator Used for validating the CSS.
  - [paint](https://www.microsoft.com/en-us/windows/paint) Used to design the RED.
  - Lighthouse.
  - [elephantsql](https://www.elephantsql.com/) Where the DB is storing.
  - [XML-sitemaps](https://www.xml-sitemaps.com/) to create sitemap.
  - gunicorn
  - [django-allauth](https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/gunicorn/) Used for the authorization.
  - [amiresponsive](https://ui.dev/amiresponsive) Used to check responsive screen.
  - [kaggle](https://www.kaggle.com/) To collect some data.

## Deployment 

### Deployment to Heroku

#### Install the dependencies:
  - Open the terminal window and type:
    - pip3 install -r requirements.txt.
    - Create a .gitignore file in the root directory of the project where you should - add env.py.
    - Create a .env file. and added the following.
    - Added "DEVELOPMENT" in os.environ to DEBUG in setting.py.
    - Added '.herokuapp.com' in the setting to ALLOWED_HOSTS.

  - import os:
    - os.environ['SECRET_KEY'] = 'Add a secret key'.
    - os.environ['DATABASE_URL'] = 'will be used to connect to the database'.
    - os.environ.setdefault ["CLOUDINARY_URL"] = will be used for static and images upload
    - os.environ.setdefault ['STRIPE_WH_SECRET'] = To inherit stripe webhook 
    - Also add os.environ['DEVELOPMENT'] = "True" in env.py.
    - Push to GitHub.

  - Migrate by Run the following commands in a terminal:
    - python3 manage.py makemigrations.
    - python3 manage.py migrate.

  - Setting up Heroku
    - Go to the Heroku website [Heroku](https://www.heroku.com/).
    - Log in or create a Heroku account.
    - Login to Heroku and choose Create App.
    - Click New and Create a new app.

      - <img src='static/images/okjk.png'>
    - Choose a name and select your location.
      - <img src="static/images/create.png">
    - Go to the Resources tab.
    - From the Resources list select Heroku Postgres.
      - <img src="static/images/werfg.png">
    - Navigate to the Deploy tab
    - Click on Connect to Github and search for your repository.
      - <img src="static/images/ccv33edg.png">
  - Navigate to the Settings tab.
    - Click on the "Settings" tab and then on "Reveal Config Vars".
    - Delete "DISABLE_COLLECTSTATIC = 1" from the list.
    - Add to the list:
      - CLOUDINARY_URL = API,
      - DATABASE_URL = API,
      - SECRET_KEY = API,
      - EMAIL_HOST_PASS = API,
      - EMAIL_HOST_USER = API,
      - SECRET_KEY = API,
      - STRIPE_WH_SECRET = API ,
      - STRIP_SECRET_KEY = API,
    - <img src="static/images/vars.png">
  - Now click on the tab "Deploy"
    - <img src="static/images/capt.jpg">
  - Then on the button "Deploy Branch" at the bottom of the page. - 
    - <img src="static/images/sccre.png">
  - When it's deployed, Click on "Open App" to access the website.
    - <img src="static/images/werdfgh.png">
  - Here is the website [Getränke](https://ecommercepp5-a121ad0ae944.herokuapp.com/).

#### Stripe
  - Register for a Stripe account.
  - in the Developers section, click on the API section and copy the publishable and secret keys.
  - Add STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY to settings.py and to Heroku, using the values found in the API section.
  - Access the webhooks section and create a webhook.
  - Choose all events to be visualised and add endpoint.
  - Add the STRIPE_WH_SECRET variable to the environment and to Heroku.

## keywords (SEO)
  <img src='static/images/keywords.png'>

## Testing
I have tested the project by the following points

  ### Validator Testing
  - Python
    - Passed the code to PEP8.
      - [Preview](TEST_PYTHON.md)
    
  - HTML
    - No errors were returned when passing through the official W3C validator
      - [Preview](TEST_HTML.md)
    
  - CSS
    - No errors were found when passing through the official (Jigsaw) validator

    <img src='static/images/check.png'>

    <img src='static/images/iiidriord.png'>

    <img src='static/images/intt.png'>

  - JavaScript
    - Undefined bootstrap was checked and there are no error Jshint validator.

    <img src='static/images/checkjssw.png'>

  ### The website has been tested and works on different screen sizes and is responsive.
  - [Preview](TEST_SCREEN.md)

### Lighthouse
  - [Preview](TEST_LIGHTHOUSE.md)

### Manually checking
#### General Tests
- It has been tested and works in several web browsers such as Firefox and Opera.
- The user gets alert messages when they log in or log out.
- The users have their own basket that they can fill it and make a checkout.
- All alerts are closed manually.
- Users can update and remove any article from the basket before checking out.
- The navigation stays at the top of the page.
- Back end connected with front end.
- E-commerce system
- It shows a message for the user when they add an article to the basket or update it/delete it.
- After checking out it is done, and the user receives a confirmation letter including all the details.
- Delete and Edit are functioning for users and admins.
- It allows the user to delete, edit, and read their basket.
- Authorization
  - Sign-Up
  - The Sign-Up page works well.
  - The link to the login page works correctly.
  - Log-in
  - The login page works well.
  - The link to the Sign-Up page works correctly.
  - The user has to enter the user details correctly to be able to log in.
  - Log-out
  - The Log-out page works well.
  - The button works well.
  - email verification

## Bugs

### Fixed bugs
  - This error happened when I was trying to check out.
  The error was solved by adding STRIPE_WH_SECRET to env.py, and to vars in Heroku

  <img src="static/images/errors.png"> 

  - I couldn't call Webhook during my work. The bug was fixed by calling WH from the checkout webhook handler

  <img src="static/images/wwhhh.png"> 

  - Unsaved authenticated user information and check out. It was solved by adding an indentation to checkout after the if statement

  <img src="static/images/eeeee.png"> 

  - Unable to migrate. the bug was solved when I did cheange note at the migartion manually from False to True.

  <img src="static/images/null.png">

  - I had a typo error, which I fixed by spelling it correctly

  <img src="static/images/messagessdef.png">  

### Unfixed bugs

  - It was planned to add a minimum price to the order. Due to a lack of time, this plan is overlooked.
  - Users don't receive an alert before they delete the article from the basket.
## ERD
<img src="static/images/erdecommerce.jpg">

## Facebook page
<img src='static/images/facebook.png'>

## Credits
- Icons are from [Font-Awesome](https://fontawesome.com/).
- This website uses [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/).
- inspiration was taken from [Code Institute](https://codeinstitute.net/de/bildungsgutschein/?utm_term=code%20institute&utm_campaign=CI+-+UK+-+Search+-+Brand&utm_source=adwords&utm_medium=ppc&hsa_acc=8983321581&hsa_cam=16493764737&hsa_grp=132915436966&hsa_ad=635790877675&hsa_src=g&hsa_tgt=kwd-319867646331&hsa_kw=code%20institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQjw-ai0BhDPARIsAB6hmP4gs1dWyA8BsBj7BoJi6X9hqEPvTk0_zxcFmabslJ6LrL0nHB6xoikaAnMjEALw_wcB).
- Hosting wrokspace [gitpod](https://www.gitpod.io/).
- This website is powered by [Django](https://www.djangoproject.com/).
- for update for newslater [Mailchimp](https://login.mailchimp.com/?referrer=%2Faudience%2Fcontacts%2F).
- To check representative screen [amiresponsive](https://ui.dev/amiresponsive).
- Images on this website are hosted and managed by [Cloudinary](https://cloudinary.com/).
- Used to create sitemap[XML](https://www.xml-sitemaps.com/).
- For the payment is used[Stripe](https://stripe.com/de?utm_campaign=DE_en_Search_Brand_Stripe_EXA-866170064&utm_medium=cpc&utm_source=google&ad_content=301948784636&utm_term=stripe&utm_matchtype=e&utm_adposition=&utm_device=c&gad_source=1&gclid=Cj0KCQjws560BhCuARIsAHMqE0GJZhP880Wbgg5rHfjuen4ObDsZMnwGIQHTWVUhPpRK-xsHiIacLkAaAry3EALw_wcB).
- Fonts are from [Google-Fonts](https://fonts.google.com/).
- Used for [Favicon](https://www.favicon.cc/).
- Used to test JavaScript [JsHint](https://jshint.com/).
- Used to stor DB [elephantsql](https://www.elephantsql.com/).
- Used to test HTML code W3 W3C [HTML Validator](https://validator.w3.org/#validate_by_input).
- Used to design the RED [paint](https://www.microsoft.com/en-us/windows/paint).
- Used to test CSS Jigsaw [CSS Validator](https://jigsaw.w3.org/css-validator/).
- Used to check resporesponsive screens [responsiveviewer](https://responsiveviewer.org/).
- Used to generate the privacy policy[privacypolicygenerator](https://www.privacypolicygenerator.info/).
- Media
  - Images were taken from [pixabay](https://pixabay.com/).
  - Some images were taken from [kaggle](https://www.kaggle.com/).
  - An images was taken from [specsonline](https://static.specsonline.com/wp-content/themes/cheers/assets/images/default_bar-mixers.png)