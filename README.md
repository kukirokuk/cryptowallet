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