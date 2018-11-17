# SendIt API

[![Build Status](https://travis-ci.org/Mark9Mbugua/SendIT2.svg?branch=ch-add-travisci-%23161952570)](https://travis-ci.org/Mark9Mbugua/SendIT2)

[![Coverage Status](https://coveralls.io/repos/github/Mark9Mbugua/SendIT2/badge.svg?branch=ch-implement-feedback-#162030600)](https://coveralls.io/github/Mark9Mbugua/SendIT2?branch=ch-integrate-coveralls-#161991046)

SendIT is a courier service that helps users deliver parcels to different destinations. SendIT provides courier quotes based on weight categories.


## Getting Started
Clone the repo from GitHub:
    
    `git clone :https://github.com/Mark9Mbugua/SendIT2.git`

Navigate to root folder
    `cd SendIT2`

Create a folder for the virtual environment for example 'env' and navigate to the folder
    `cd env`

Create a virtual environment
    `virtualenv env`

Activate the virtual environment from the root folder
    `source .\env\Scripts\activate`

Install the required packages
    `pip install -r requirements.txt`

## Starting the API

On the terminal type `export FLASK_APP=run.py` and type enter. Run `flask run`

## Use the following endpoints to perform the specified tasks
		 
| 	Endpoint                              | Functionality                                                  
| ----------------------------------------| -----------------------------------------------|
| POST api/v1/signup                      | Create a user account                          |          
| POST /api/v1/signin                     | Sign in a user                                 |
| POST /api/v1/parcels                    | Create a parcel delivery                       |
| GET /api/v1/parcels                     | Retrieve all parcel delivery                   | 
| GET /api/v1/parcels/<int:id>            | Retrieve a specific parcel delivery            |
|PUT /api/v1/parcels/<int:id>/cancel	  | Cancel a specific delivery                     |
|GET /api/v1/users/<int:id>/parcels       | Retrieve a specific user's deliveries          |


## Application Features

1. Users can create an account and log in.
2. Users can request a delivery.
3. Users can cancel a delivery request.
4. Users can see the details of a delivery order.
5. Users can view all the deliveries they have requested
6. Users can view a specific delivery.

