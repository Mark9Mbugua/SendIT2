# SendIt API

[![Build Status](https://travis-ci.org/Mark9Mbugua/SendIT2.svg?branch=ch-add-travisci-%23161952570)](https://travis-ci.org/Mark9Mbugua/SendIT2)

[![Coverage Status](https://coveralls.io/repos/github/Mark9Mbugua/SendIT2/badge.svg?branch=master)](https://coveralls.io/github/Mark9Mbugua/SendIT2?branch=ch-integrate-coveralls-#161991046)

SendIT is a courier service that helps users deliver parcels to different destinations. SendIT provides courier quotes based on weight categories.


## Getting Started
Clone or download the project from git either via terminal using the commands 
* git clone :https://github.com/Mark9Mbugua/SendIT2.git
* Download zip file from the right hand corner


## Use the following endpoints to perform the specified tasks
		 
| 	Endpoint                              | Functionality                                                  
| ----------------------------------------| -----------------------------------------------|
| POST api/v1/registration                | Create a user account                          |          
| POST /api/v1/login                      | Login a user                                   |
| POST /api/v1/parcels                    | Create a parcel delivery                       |
| GET /api/v1/parcels                     | Retrieve all parcel delivery                   |
| POST /api/v1/parcels/<int:id>/          | Update a specific parcel delivery              |
| GET /api/v1/parcels/<int:id>            | Retrieve a specific parcel delivery            |
		 

## Application Features

1. Create a parcel delivery order.
2. Admin account for managing deliveries by users.

<br>

**Users can do the following**

* Users can create an account and log in.
* Users can request a parcel delivery.
* Users can cancel a delivery request.
* Users can view all deliveries that they have requested.
* Users can view a specific delivery. 


### Prerequisites

Please make sure you have a browser installed on your computer if you want to be able to check all files and see how the user interface looks like.

### Installing

Make sure you download postman to be able to test the specific endpoints on this project.

## Running 

* git clone https://github.com/Mark9Mbugua/SendIT2.git
* cd into folder
* create a virtual enviroment using virtualenv env
* activate env
* run command "python run.py"

