
<div id="top" align="center">
  <a href="https://github.com/Kmachappy/Runners-Page">
    <img src="https://i.imgur.com/jdjcdMZ.jpg" alt="Logo" width="250" height="150">
  </a>
  <a href="https://github.com/Kmachappy/Runners-Page">
    <h3 align="center">KmacShop</h3>
  </a>

  <p align="center">
    An Ecommerce Web App based around Keyboards <br/>
    Keyboards are more than just putting parts together.
 <p>A Django Ecommerce Web App</p><br />
    <a href="https://github.com/Kmachappy/Runners-Page"><strong>Live Website - KmacShop </strong></a>
    <br />
 Ecommerce Web Application built on <br/>
    <a href="https://www.djangoproject.com/">Django</a>
    ·
    <a href="https://www.postgresql.org/">PostgreSQL</a>
    ·
    <a href="https://tailwindcss.com/">TailwindCSS</a>
    ·
    <a href="https://oauth.net/2/">OAuth 2.0</a>
  </p>
</div>

# About

Description            |  Screenshot
:---:|:----:
| <p align="left">- A Django ecommerce web application that displays a directory keyboard related products. <br><br> - Users will be able to explore Keyboard products and view all their details about the Product! <br> - Users can leave a reviews on Products they have purchased. <br>- Users are able to browse and filter products by their categories <br> - Users are able to add products to their cart and maintain session with their cart <br> - Users are able to </p> | ![](https://i.imgur.com/bGD2s2z.jpg) |

<p align="right">(<a href="#top">back to top</a>)</p>

# KmacShop WireFrame and ERD

Index/Home             |  Category/Filtered
:-------------------------:|:-------------------------:
![](https://i.imgur.com/I7mtFwB.png)  |  ![](https://i.imgur.com/4BJ71X9.png)

Product Show             |   ERD still missing models
:-------------------------:|:-------------------------:
![](https://i.imgur.com/253u25t.png)  |  ![](https://i.imgur.com/rJpsWhG.png)
Cart             |  Checkout
:-------------------------:|:-------------------------:

<p align="right">(<a href="#top">back to top</a>)</p>

# Functionality

- In this app we will access a database of products and display them on the index page
- User will Be able to view a directory of products and browse any for full information
- User will be able to sign up or log in
- if user is logged in they can

        - can view products 
        - add products to cart 
        - maintain a session with their cart
        - checkout items with their cart
        - add reviews to products 



# Routes

```
path('', views.index, name='index'),
path('about/', views.about, name='about'),
path('products/<slug:slug>/', views.product_detail, name='product_detail'),
path('category/<category:slug>/', views.category_index, name='category_index')
path('account/signup/', views.signup, name='signup')
```

# Models/Schema

### subject to change

Event/Review Schema:

```

```

User Schema:

```

```

# Current State

- User is currently able to visit the site and see a directory of products

- user is able to log in through google strategy OAuth or django authentication

- user is able to click on any of the product displayed to view full information

- if user is logged in they will have access to be able to add item to their cart and checkout

- if user is logged in on the product they are viewing they are able to add a comment

- user will be able to see their comments added to the product they commented on

<p align="right">(<a href="#top">back to top</a>)</p>

# Roadmap and future Implementations

```
```


<p align="right">(<a href="#top">back to top</a>)</p>

# User Story

- As a user, I should be able to see directory of Running Races/Events on Index
- As a user, I should be able to click any of the featured Race for their full description/data on index page
- As a user, I should be able to navigate the navigation links to sort events by race type on index and Results/filtered
- As a user, On the Results/filtered page I should be able to see a directory of event filtered by event type
- As a user, I should be able to click on any Race/Event to see their complete data on the Results/Filtered page
- As a user, On the show page I should be able to see all an Events data
- As a user, On the show page I should be able to update the event data
- As a user, On the show page I should be able add a review for the event
- As a user, I could contribute to the database of events by creating another race event on the database on the head of the page
- As a user, I should be able to log in  on the header and view and edit my reviews

<p align="right">(<a href="#top">back to top</a>)</p>

# Technologies used

- HTML
- CSS
- TailwindCSS
- JavaScript
- Django
- Postgresql
- SQL
- DTL
- OAuth 2.0

<p align="right">(<a href="#top">back to top</a>)</p>

# API's used
 <!-- - **[Strava API](https://developers.strava.com/)**. -->
- **[Leaflet API](https://leafletjs.com/SlavaUkraini/)**.
- **[mapbox API](https://leafletjs.com/SlavaUkraini/)**.


<p align="right">(<a href="#top">back to top</a>)</p>


# KmacShop ScreenShots

Index/Home             |  Category/Filtered
:-------------------------:|:-------------------------:
![](https://i.imgur.com/bGD2s2z.jpg)  |  ![](https://i.imgur.com/haKGQ6J.png)

Product Show             |   Cart Summary
:-------------------------:|:-------------------------:
![](https://i.imgur.com/cpQWQEo.png)  |  ![](https://i.imgur.com/PajTdjV.png)
User Profile           |  Checkout
:-------------------------:|:-------------------------:

<p align="right">(<a href="#top">back to top</a>)</p>


# Resources/Links
```
```
<p align="right">(<a href="#top">back to top</a>)</p>
