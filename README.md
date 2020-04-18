
# Milestone 4 : Project - Full Stack using Django Framework

## PartyZone Costume supplies
The project is a commercial site that sells party costumes. The user can select costumes they wish to buy which are placed in a cart.
To purchase costumes the user enters the cart and enters credit card number for payment. 

# UX
### Site Owner
The site aims to sell for adult Stag, Hen, Halloween and other fun occasions. The site promotes the costumes by emphasizing their sense of fun through use of font, colours and text description. Product warnings on stock levels and guarantees of delivery also prompts the user to place an order. The site uses option selection rather than text entry where possible to avoid user error.

### Site User
The user can easily access products in the home page and can add products to his cart using a button click. If the user wishes to remove an item from the cart this is enabled through a button click. The cart is available to review througout the application and the user can amend orders in their cart before checking out. 

The user must be logged in to complete the purchase and is automatically redirected to the login screen if logged out. They are also redirected to the checkout page once login is complete. 

The NavBar has simple (Registration, Login) or (Profile, Logout) options displayed depending on the login status. It also contains a search costumes by category function. For a larger costume database a text search would be added. 

### Wireframes
The design philosophy was to let the products speak for themselves and the products feature prominently with easy access. The text style and description yield a fun and cartoonish sensation. The Navbar is purple to attract attention but does not detract from the products or text. The Navbar and footer formats are consistent across all applications which makes navigation simpler.
  * [Products_Page](Readme/wireframes/Products.jpeg)
  * [Cart_Page](Readme/wireframes/Cart.jpeg)
  * [CheckOut_Page](Readme/wireframes/CheckOut.jpeg)

# Features
The site is broken into various components using Django create application.

## Applications
### /accounts, /templates/registration
This contains functionality for user login, logout, user authenication and registration. The /templates/registration contains html pages to complete password reset.

### cart
Cart feature is a temporary store for the user's selected products. The cart information is visible throughout the site by creating a `contexts.py` which is declared in the middleware section of `settings.py`.

### checkout
Functionality to take payment to purchase products. Once payment is successful product stock levels are updated.

### search
Product search functionality by category. The selected category is retained throughout the site using a session variable.

### products
Display product in html using Bootstrap styling. Products are not displayed once their stock levels reach zero.

### media/images
Contains product images


# Database

## Users
User are created using Django ModelForm which uses a relational database. The fields for each user are: username, email, password1 (password), 
password2 (password verification)

## Products
Each products contains the following information:
name, description, price, stock (number in stock), stock_alert (alert user), image, 
category (foreign Key to Theme)

## Theme
Category of product, currently (Halloween, Pirate)


# Testing
Travis Integration testing was attempted but was abandoned after it rejected version 7.0 of pillow in requirements.txt file. Manual Testing employed under the following scenarios: 

1. Register a new User. Verified through the admin page that a new user was created.
2. Login existing User. Login of existing user was permitted.
3. Logout existing User. Logout operated.
4. Search Products. Search for 'Pirate' or 'Halloween' categories yielded the appropriate products. 

   The following tested for the operation of Stock level alert.
  * [Stock_with_No_Alert](Readme/Tests/StockNoAlert.png)
  * [Sold_3_Stock_items](Readme/Tests/Sale_3_items.png)
  * [Updated_Alert](Readme/Tests/Stock_alert_Post_Sale.png)

5. Select product for Cart. For each product once 'Cart' is selected it is placed in 'Cart'. Minimum quantity is set to '1'.
6. Remove product from Cart. Each product can be deselected from 'Cart' but this is only permitted if product already exists in 'Cart'. The main issue here was indicating to 'Cart' that 'Remove' was selected and to remove the item form Cart.
7. Amend Cart. Edit the product quantity in Cart. 
8. Complete purchase. Purchase was completed using 'Stripe' API with '4242 4242 4242 4242' credit card number. If invalid credit card was used the purchase did not process. Credit card default expiry year was set one year from current year to avoid mistaken entry. 

9. Product record updated. Once purchase is complete the product stock record was updated.
  * [Product_Stock_Pre_Sale](Readme/Tests/StockPreSale.png)
  * [Sold_one_Pirate_First_Mate](Readme/Tests/SaleOnePirateFirstMate)
  * [Post_Sale_Stock](Readme/Tests/StockPostSale.png)


10. Product display updated. New product levels reflected in display.


# Technologies used
1. HTML, CSS.
2. Django. This enabled the admin function and product databases. It also enabled the compartilisation of code through various apps.
3. Javascript. Used for Stripe verification.


# Deployment

## Hosting
The project is hosted (partysupplies.herokuapp.com) on Heroku with media (images and css) files sitting in AWS S3 buckets because static files have limited supported in Heroku.

To host the program in Heroku the following keys had to be entered in the CONFIG page since this information is not uploaded to Github.
1. Postgres SQL URL: This is the URL link to the Postgres database. The URL is created by Heroku CONFIG VARS section and entered into `settings.py` file of the application to enable data to be accessed by Heroku.
2. STRIPE PUBLISHABLE & STRIPE SECRET: Keys used by STRIPE to process payments.
3. AWS_ACCESS_KEY_ID & AWS_SECRET_ACCESS_KEY: Keys to access AWS S3 buckets.
4. SECRET_KEY: Found in the root `settings.py` file. Enables the file to be run in production.

Create requirements.txt in the workspace root directory by entering the following in the command line: pip3 freeze > requirements.txt (This gives Heroku the list of supporting libraries it needs to run the application)

Enter `python3 manage.py collectstatic` in the commmand line to upload static files to AWS.

Create Procfile in the root directory containing the following: "web: gunicorn partyzone.wsgi:application". This will enable Django to run the application.


## Deploy locally
The code is repositied at the following location in Github: https://petergalvin-cyber.github.io/Milestone4-PartyZone/. Download the zip file on Github and unzip to your local Django workspace.

Copy the application directories across and copy the root `url.py and the root settings.py` file to your local directory. 
The `settings.py files contains the linkages to AWS and the urls.py` contain url links to the applications. If AWS is not desired then use your own default `settings.py` file but update it to include the imported applications.


**Install the following libraries in your workspace:**
1. pip3 install django == 1.11.29
2. pip3 install pillow (enable images to be uploaded)
3. pip3 install django-forms-bootstrap (Enable bootstrap form styling in python)
4. pip3 install stripe
5. pip3 install boto3
5. Create AWS S3 and Stripe account and create keys. 
6. Enter "python3 `manage.py` collectstatic" in the commmand line to upload static files to AWS.

Run locally in Gitpod by entering: "python3 `manage.py` runserver".

# Responsive
Application uses Bootstrap functionality which is automatically responsive to mobile applications. The product display and the Navbar respond to various screen sizes. The attachment illustrates how the application adjusts to iPhones.
[Responsive Test](Readme/Tests/Responsive.png)

# Features to add / Issues

In future versions I would expand the User model to include the users address. This information can then be imported into the checkout page to avoid registered users having to re-enter this information.

The password reset sends a passowrd reset email from my personal Google mail to the user but despite assistance from Tutor support Google mail would not permit the application access.  

# Acknowledgement

The code for the application was based on Code Institute tutorials. The concept was developed from an exising costume site www.fancydressball.co.uk
