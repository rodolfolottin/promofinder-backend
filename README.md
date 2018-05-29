# promofinder-backend

The backend for the promofinder app.

## Installing and running

1. Clone this repo:

    ```
    $ git clone https://github.com/rodolfolottin/promofinder-backend
    ```

2. Make sure that you have docker installed.

3. Get your own Twitter developers keys.

    In order to be able to use the Twitter API one must get some keys from this site: https://apps.twitter.com/. You need to have a file called .env in the root directory of the project and provide them as it follows:

    ```
    TWITTER_CONSUMER_KEY=''
    TWITTER_CONSUMER_SECRET=''
    TWITTER_ACCESS_TOKEN_KEY=''
    TWITTER_ACCESS_TOKEN_SECRET=''
    ```

    You can copy the file called env.example, rename it to .env and fill in the keys values to their respective names.

4. Build and launch the app.

    ```
    $ docker-compose build up -d
    ```

5. Check it out accessing: http://localhost:8000/

## Running the tests:

1. Make sure that you have python3.6, pip and pipenv installed.

2. Install the project requirements.

    ```
    $ pipenv install
    ```

3. Activate your environment.

    ```
    $ pipenv shell
    ```

3. Run the tests

    ```
    $ pytest
    ```
