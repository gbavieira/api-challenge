# Alura Challenge Back-End 4th Edition


This repository was created to showcase my project for the 4th Edition of Alura Back-End Challenge.

## About the Challenge

This is a challenge to simulate the routine of a backend developer working a company where the UX team requested an application for a family budget control. This budget control needs to be able to register all income and expenses from a family. It needs routers for the income and expenses following the clean REST coding and have some validations according to the businesses rules. It will be stored in a database and have authentications.

### Tools and Development

For this project, Alura creates a Trello Kanban with some steps of a procedure in where the developer must follow to report weekly. The project is divided in 4 weeks, where the first three are for developing and the last week is meant to be a testing one.

The database needs to be able to store 4 fields for income and expense: id; description; value; date.

To deal with that I have created two different classes for Income and Expense, setting the rules for the model:
![image](https://user-images.githubusercontent.com/101214015/183497454-b2b14105-5f99-4e62-978d-bfb83156fe3a.png)

Blank and Null arguments were set to False to make the fields required when receiving a GET, POST, PUT or PATCH method.

The database choice was free, so I chose to work with [PostgreSQL](https://www.postgresql.org/) as it easily integrates with [Django REST framework](https://www.django-rest-framework.org/). For testing porpouses I have used [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/readme.html) to use [Swagger](https://swagger.io/) for making request methods and testing the API.

To create the API, I have settled the serializer with some businesses rules and used the DRF viewsets.ModelViewSet to easily crete the entry fields for the methods.

### Next Steps

Waiting for second week insctructions.
