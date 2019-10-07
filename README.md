## Django Ice Cream Shop
In this assignment you will focus on learning how to use Django's models and function based views.

## Objectives

### Learning Objectives
After completing this assignment, you should…
* Know how to create a django model
* Know about various django model fields
* Know how to use a function based views to get data from the database

### Performance Objectives
After completing this assignment, you be able to effectively use
* Be able to create a Django Model
* Be able to create and use various field types on your Django model
* Be able to use function based views to get model instances (objects) from the database

## Details

### Deliverables
* A repo containing your Django project and one Django app
* The repo should also contain a sql lite database with your test data

### Requirements
* pep8 and pep20 compliant code

## I'm a Web Developer Mode
Buster's is a local ice cream creamery that specializes in making fresh ice cream daily. They rotate out their flavors and have certain flavors that are available for just a day, a week, or seasonal flavors that you can get for a few months.

Using the tools you've learned in class, create an ice cream menu for Busters. The menu should have the following headings:
* Featured
* Daily Flavor
* Our Weekly Flavors
* Seasonal Flavors

Under each heading display a listing of the flavors that fit that category.
Details
* Setup a new Django project
* Add an ice_cream app to your project
* Create an IceCream model in your app
* Add the following fields to your model:
```
flavor: CharField
base: CharField with choices (chocolate, vanilla)
available = CharField with choices (daily, weekly, seasonal)
featured = BoolField
date_churned = DateField
```

* Create a view that will display the menu
* Update the menu to display all, daily, weekly, or seasonal flavors based on user input