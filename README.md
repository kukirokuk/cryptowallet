# CryptoWallet

This repository contains the source code for the CryptoWallet app.

## Building the App

To build the app, follow these steps:

1. Make sure you have Docker installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the root directory of this repository.
4. Run the following command to build the Docker image:

   ```shell
   docker build -t cryptowallet .

## Running the App

To run the app, use the following steps:

1. After successfully building the Docker image, run the following command:

    ```shell
    docker run -p 8000:8000 cryptowallet python manage.py runserver 0.0.0.0:8000

2. Open a web browser and visit http://localhost:8000/admin to access the running app admin page with login: admin and pass: admin. For test purpose only dummy admin user was restored from db backup in process of build. In production environment db backups pushed into repos should be strongly avoided!

## Running tests

To run unit tests, use the following command:

1. After successfully building the Docker image, run:

    ```shell
     docker run cryptowallet python manage.py test crypto_addresses.tests.tests

## API docs

### Create Address

- Method: POST
- URL: `/api/addresses/`
- Description: Create a new address for a specific cryptocurrency.

**Request Body**

    {
    "cryptocurrency": "BTC"
    }

**Response**


    Status: 201 Created
    Body:

    {
    "address": "newly_generated_address"
    }

### Retrieve Addresses

- Method: GET
- URL: `/api/addresses/`
- Description: Retrieve a list of all addresses.

**Response**


    Status: 200 OK
    Body:
    
    [
    {
    "address": "address_string"
    },
    ...
    ]

### Retrieve Address by id

- Method: GET
- URL: `/api/addresses/<int: id>`
- Description: Retrieve address

**Response**


    Status: 200 OK
    Body:

    {
    "address": "address_string"
    }
