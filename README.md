![Logo Text](https://user-images.githubusercontent.com/64138643/108905833-17788880-7618-11eb-85e6-b6c7e066fe7c.PNG)

### [Heroku App](https://wrottesley-golf-club.herokuapp.com/)
### [GitHub](https://github.com/CarterStefan/wrottesley_golf_club)

Wrottesley Golf Club is a golf course located in the west midlands. There are a number of users that the website will target and each of these user types will have a different need when using the website. This is my fourth milestone project as part of my Full Stack Web Development Course with [Code Institute](https://codeinstitute.net/). This project focuses on "Full stack Frameworks With Django" and will put into practice what I have learned over the last year on the course.

## Table of Contents
1. [**Project overview**](#project-overview)
2. [**UX**](#ux)
  - [**User Stories**](#user-stories)
3. [**UI**](#ui)
  - [**Color Scheme**](#color-scheme)
  - [**Typography**](#typography)
  - [**Wireframes**](#wireframes)
4. [**Features**](#features)
  - [**Existing Features**](#existing-features)
  - [**Features Left to Implement**](#features-left-to-implemement)
5. [**Databases**](#databases)
6. [**Technologies Used**](#technologies-used)
7. [**Deployment**](#Deployment)
8. [**Testing**](#Testing)
9. [**Acknowledgments**](#Acknowledgments)
---

## Project overview
The project was built using [Django](https://www.djangoproject.com/) - web framework. 

For the testing of the store and subscriptions, a test credit card can be used by inputting the following details:
- Card Number: 4242 4242 4242 4242
- Exp date: 04/24
- CVC: 424
- ZIP: 42424
 
## UX
### User Stories

The three targetted users of the site will be:
- Existing members of the club
- Potential Members of the club
- Casual golfers wishing to play a round or purchase products from the store

Using the website, all users will be able to:

#### Viewing & Navigation
- View informatiion about the club
- View contact information about the club
- Easily navigate to the Tournaments page
- Easily navigate to the Blog page
- Easily navigate to the Store page
- Easily navigate to the Memberships page
- Alwys be able to see the total count of the basket

#### Registration & User Accounts
- Register for an account
- Login and Logout of the account
- Recover my password easily
- Recieve email confirmations once I have registered for an account
- Have an area of the user profile dedicated to my purchase history
- Have an area of the user profile dedicated to my personal information

#### The Store
- View and sort all products in the store
- Sort within a chosen category
- Search for an item
- See what the search criteria was
- Select the quantity of an item to purchase
- Select the size of an item (if applicable)
- View my items that I have added to my bag
- Delete an item and reduce the size selected
- Easily fill out delivery and payment information
- View an order summary once a purchase is made
- Recieve an email confirmation

#### Subscribtions
- See the benefits of a pro membership
- Be able to purchase a pro membership
- Be able to downgrade to beginner membership at any time

#### Blog
- Read the latest news about the course through individual blog posts
- Comment on a blog post
- Upload new blog posts (Admin Only)
- Edit blog posts (Admin Only)
- Delete blog posts (Admin Only)
- Approve comments which have been posted on a blog
- Only allow approved comments to be visible to members

#### Tournaments
- See a list of all the upcoming tournaments
- See the dates and times of the tournaments
- See the location of the tournaments
- See the prices of the tournaments

#### Administration
- Upload new products to the store (Admin Only)
- Upload new tournaments to the Tournaments page (Admin Only)
- Edit tournaments on the Tournaments page (Admin Only)
- Delete tournaments
- Edit the existing products in the store (Admin Only)
- Delete a product from the store (Admin Only)
- Approve comments which have been made on blog posts (Admin Only)

## UI
#### Color Scheme
[uiuxcenter](https://www.instagram.com/uiuxcenter/?hl=en) - Used for inspiration on my color scheme, to create a bold web experience.
![ColorScheme](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/color_scheme.PNG)

#### Typography
[GoogleFonts](https://fonts.google.com/)
- [Libre Baskerville](https://fonts.google.com/specimen/Libre+Baskerville?query=Libre+Baskerville) - Used for the logo and headings around the site
- [Roboto](https://fonts.google.com/specimen/Roboto?query=Roboto) - Used for the main body text

#### Desktop Wireframes
<details><summary>Homepage</summary>
<p>

![Homepage](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Desktop/homepage.png)

</p>
</details>

<details><summary>Products</summary>
<p>

![Products](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Desktop/products.png)

</p>
</details>

<details><summary>Product Details</summary>
<p>

![Product Details](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Desktop/product_details.png)

</p>
</details>

<details><summary>Basket</summary>
<p>

![Basket](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Desktop/Basket.png)

</p>
</details>

<details><summary>Checkout</summary>
<p>

![Checkout](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Desktop/checkout.png)

</p>
</details>

<details><summary>Blog</summary>
<p>

![Blog](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Desktop/blog.png)

</p>
</details>

<details><summary>Blog Post</summary>
<p>

![Blog Post](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Desktop/blog_post.png)

</p>
</details>

<details><summary>Tournaments</summary>
<p>

![Tournaments](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static//UX/Wireframes/Desktop/tournaments.png)

</p>
</details>

<details><summary>Memberships</summary>
<p>

![Memberships](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Desktop/memberships.png)

</p>
</details>

<details><summary>Profile</summary>
<p>

![Profile](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Desktop/profile.png)

</p>
</details>

#### Tablet Wireframes
<details><summary>Homepage</summary>
<p>

![Homepage](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Tablet/tablet_homepage.png)

</p>
</details>

<details><summary>Products</summary>
<p>

![Products](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Tablet/tablet_store.png)

</p>
</details>

<details><summary>Product Details</summary>
<p>

![Product Details](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Tablet/tablet_store_product.png)

</p>
</details>

<details><summary>Basket</summary>
<p>

![Basket](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Tablet/tablet_basket.png)

</p>
</details>

<details><summary>Checkout</summary>
<p>

![Checkout](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Tablet/tablet_checkout.png)

</p>
</details>

<details><summary>Blog</summary>
<p>

![Blog](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Tablet/tablet_blog.png)

</p>
</details>

<details><summary>Blog Post</summary>
<p>

![Blog Post](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Tablet/tablet_blog_post.png)

</p>
</details>

<details><summary>Tournaments</summary>
<p>

![Tournaments](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static//UX/Wireframes/Tablet/tablet_tournaments.png)

</p>
</details>

<details><summary>Memberships</summary>
<p>

![Memberships](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Tablet/tablet_memberships.png)

</p>
</details>

<details><summary>Profile</summary>
<p>

![Profile](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Tablet/tablet_profile.png)

</p>
</details>

#### Mobile Wireframes
<details><summary>Homepage</summary>
<p>

![Homepage](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Mobile/mobile_homepage.png)

</p>
</details>

<details><summary>Products</summary>
<p>

![Products](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Mobile/mobile_store.png)

</p>
</details>

<details><summary>Product Details</summary>
<p>

![Product Details](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Mobile/mobile_store_item.png)

</p>
</details>

<details><summary>Basket</summary>
<p>

![Basket](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Mobile/mobile_basket.png)

</p>
</details>

<details><summary>Checkout</summary>
<p>

![Checkout](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Mobile/mobile_checkout.png)

</p>
</details>

<details><summary>Blog</summary>
<p>

![Blog](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Mobile/mobile_blog.png)

</p>
</details>

<details><summary>Blog Post</summary>
<p>

![Blog Post](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Mobile/mobile_blog_post.png)

</p>
</details>

<details><summary>Tournaments</summary>
<p>

![Tournaments](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static//UX/Wireframes/Mobile/mobile_tournaments.png)

</p>
</details>

<details><summary>Memberships</summary>
<p>

![Memberships](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Mobile/mobile_memberships.png)

</p>
</details>

<details><summary>Profile</summary>
<p>

![Profile](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Mobile/mobile_profile.png)

</p>
</details>


## Features
#### Existing Features
The Wrottesley Golf Club website has 9 apps:
- Basket
- Blog
- Checkout
- Home
- Memberships
- Products
- Profiles
- Tournaments
- Account

#### Future Features

## Databases
For my development environment, I was using SQLite, as this is the default with Django. Once my code was deployed to Heroku, I switched to a PostgreSQL database.

### models and apps
My site consists of 9 apps, and a total of 'xxxxx' models:

#### Home App
- The home app is used to display index.html, which serves as the root page of the site. This app contains no models.

#### Basket App
- The basket app is used for basic CRUD operations for managing products in the shopping basket. This app contains no models.

#### Blog App
- The blog app is used to show blog posts which have been added by an admin. Users can read and also comment on blog.

##### Blog model
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='blog_posts'
    slug = models.SlugField(max_length=200, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    main_image = models.ImageField(null=False, blank=False)
    title = models.CharField(max_length=300, unique=True, null=False, blank=False,)
    sub_title_one = models.CharField(max_length=300, unique=True, null=False, blank=False,)
    blog_content_one = models.TextField(null=False, blank=False,)
    sub_title_two = models.CharField(max_length=300, null=True, blank=True,)
    blog_content_two = models.TextField(null=True, blank=True,)
    last_updated = models.DateTimeField(auto_now=True)

##### Comment model
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    body = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

#### Checkout App
- The checkout app is used to handle the chekout process of the store and enabled users purchase their products through the Stripe payments system.

##### Order model
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    street_address = models.CharField(max_length=80, null=False, blank=False)
    county = models.CharField(max_length=30, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    discount = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

##### OrderLineItem model
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True)  # S, M, L, XL
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models. DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

#### Memberships App
- The memberships app is used to allow users to upgrade their membership to 'pro' or downgrade to 'beginner' if they have signed up but no longer which to be a 'pro'memnber.

##### StripeCustomer model
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    stripeCustomerId = models.CharField(max_length=255)
    stripeSubscriptionId = models.CharField(max_length=255)

#### Products App
- The products app is used to store the details of an individual product and associate it with a particular category.

##### Category model
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

##### Product model
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    material = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

#### Profiles App
- The profiles app is used to store information about the registered users of the site, this can be used for faster checkout and handles the membership level for discounts and access around the site.

##### UserProfile model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_type = models.CharField(max_length=20, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=30, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country *', null=True, blank=True)

#### Tournaments App
- The tournaments app is used to store information about upcoming tournaments at the golf club.

##### Tournament model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_type = models.CharField(max_length=20, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=30, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country *', null=True, blank=True)


## Technologies Used
1. [HTML 5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
- HTML is the standard markup language for Web pages.

2. [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- Cascading Style Sheets (CSS) is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.

3. [JAVASCRIPT](https://www.javascript.com/)
- JavaScript, often abbreviated as JS, is a programming language that conforms to the ECMAScript specification. The vast majority of websites use it for client-side page behavior,[11] and all major web browsers have a dedicated JavaScript engine to execute it.

5. [PYTHON](https://www.python.org/)
- Python is a programming language that lets you work quickly and integrate systems more effectively.

4. [JQUERY](https://jquery.com/)
- jQuery is a fast, small, and feature-rich JavaScript library.

5. [BOOTSTRAP](https://getbootstrap.com/)
- A modern responsive front-end framework based on Material Design.

6. [FONTAWESOME](https://fontawesome.com/)
- Font Awesome is a font and icon toolkit based on CSS and Less.

7. [GOOGLE FONTS](https://fonts.google.com/)
- Google Fonts is a library of more than a thousand free and open source font families, an interactive web directory for browsing the library, and APIs for using the fonts via CSS and Android.

8. [DJANGO](https://www.djangoproject.com/)
- Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

9. [BOTO3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)
- You use the AWS SDK for Python (Boto3) to create, configure, and manage AWS services, such as Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Simple Storage Service (Amazon S3).

10. [GUNICORN](https://gunicorn.org/)
- Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX.

11. [PILLOW](https://pillow.readthedocs.io/en/stable/)
- Python Imaging Library is a free and open-source additional library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats.

12. [POSTGRES](https://www.postgresql.org/)
- PostgreSQL, also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and SQL compliance. 

13. [PSYCOPG2](https://pypi.org/project/psycopg2/)
- Psycopg is the most popular PostgreSQL database adapter for the Python programming language.

14. [STRIPE](https://stripe.com/en-gb)
- Stripe is an Irish-American financial services and software as a service company. The company primarily offers payment processing software and application programming interfaces for e-commerce websites and mobile applications.

15. [SQLITE3](https://www.sqlite.org/index.html)
- SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.

16. [GITPOD](https://www.gitpod.io/)
- Gitpod streamlines developer workflows by providing prebuilt, collaborative development environments in your browser - powered by VS Code.

17. [GITHUB](https://github.com/)
- Hosting for software development and version control using Git.

18. [HEROKU](https://www.heroku.com/home)
- Heroku is a cloud platform as a service supporting several programming languages.

19. [ADOBEXD](https://www.adobe.com/products/xd.html)
- Adobe XD is a vector-based user experience design tool for web apps and mobile apps, developed and published by Adobe Inc.

20. [Imgur](https://imgur.com/)
- Free image hosting website used for embedding links to images into websites.

## Deployment
All code on this project was created in [Gitpod](https://www.gitpod.io/) for development. When development was nearing completion it was deployed to Heroku for hosting the webpage and AWS S3 for hosting the static files and all images.

If someone wishes to run this project locally, they should install the Gitpod chrome browser extension. Then:
- Go to https://github.com/CarterStefan/wrottesley_golf_club and click the green button titled 'Gitpod'

- In the gitpod settings click 'variables' and then 'add new variable' and add the following variables
    - STRIPE_SECRET_KEY = {Your stripe secret key}
    - DEVELOPMENT = {True}
    - STRIPE_BEGINNER_PRICE_ID = {Your stripe beginner price ID}
    - DOMAIN_URL = {Your domain url}
    - STRIPE_PRO_PRICE_ID = {Your stripe pro price ID}
    - STRIPE_WH_SECRET = {Your stripe webhook secret key}
    - STRIPE_PUBLIC_KEY = {Your stripe public key}
    - SECRET_KEY = {Your stripe secret key}
    - STRIPE_MEMBERSHIP_WH_SECRET = {your stripe membership webhook secret key}

    - Any stripe secret keys will need to be set up in the stripe interface once registered for an account

- In the command line type 'pip install -r requirements.txt'

- Migrate the models to the database by going to the command line and typing:
    - python3 manage.py makemigrations
    - python3 manage.py migrate

- Create a super user by going to the command line and typing:
    - python3 manage.py createsuperuser
    
    - Enter a email, username and password

- Load the data for the categories and the products by going to the command line and typing:
    - python3 manage.py loaddata categories
    - python3 manage.py loaddata Products

- Start the web app by going to the command line and typing:
    - python3 manage.py runserver
    
- Go to the admin page, by tacking /admin to the end of the url
    - Login with the credentials of the superuser you just created
    - Go to the blog option, and add a new blog using the form
    - Go to the Tournaments option, and add a new tournament using the form


## Testing


## Acknowledgments
#### Code
- The store section of the website was largely created by following the tutorials from the Boutique Ado project from [CodeInstitute](https://codeinstitute.net/). The code was adapted to suit the needs of my store and fit with the branding of my project. This code included the bag, store products and checkout process.

- The blog application was created by following along with the [DjangoCentral](https://djangocentral.com/building-a-blog-application-with-django/) post 'Building a blog application with django'. I then adapted the code to fit with my project.

- The memberships subscription logic was built with help from the [TestDriven](https://testdriven.io/blog/django-stripe-subscriptions/) tutorial on integrating stripe subscription services.

- I took the code for the dropdowns in the wireframes section of the readme from [Joyrexus](https://gist.github.com/joyrexus/16041f2426450e73f5df9391f7f7ae5f).

#### Media
[ClubHouse](https://www.clubhousegolf.co.uk/)
- Used for all product images, details and descriptions

[StAndrews](https://www.standrews.com/play/the-home-of-golf/blog)
- Used for all blog Contents

[AllSquareGolf](https://www.allsquaregolf.com/golf-courses/england/wrottesley-golf-club)
- Used for hero image on site

[Unsplash](https://unsplash.com/s/photos/golf)
- Used for stock images of golf courses used on blogs, memberships and homepage

#### Thanks
- I would like to thank [CodeInstitute](https://codeinstitute.net/) for providing the lessons on full stack frameworks and the tutorials on how to set up a store. Also, a big thankyou to the tutor support team, who not only helped with this project, but also throughout the last year.

- A big thank you also to my mentor Gbenga, whose encouragement and support has helped me through this project and throughtout my time on the course.
