# financial-data-banxico


Financial-data-banxico is a web app that allows clients to get and visualize daily data about UDIS and dollar, this data comes from Banxico service. The backend of the app is built-in Python 3 using Flask to build the API, SQLAlchemy, MySQL to save the data of UDIS and Dolar. The frontend of the app is built using React and Typescript for the UI, Axios for creating requests, and ApexCharts to create the charts.

### Features!
-----------------

  - Range selector (the user can select a date range to search).
  - The [Banxico service] is the source of the data displayed.
  - Display the values of UDIS and Dollar for the range selected.
  - Max, Min and average values in the selected range are displayed for UDIS and Dollar.

### Tech
-----------------

Financial-data-banxico uses a number of open source projects to work properly:

* [Python 3] - algorithms, DB connection and tests!
* [SQLAlchemy] - ORM
* [MySQL] - relational database.
* [Docker] - containers.
* [Typescript] - Components of the UI and interfaces.
* [React] - UI framework.
* [Axios] - HTTP requests.
* [ApexCharts] - Charts.

### Database
-------------------

There are 2 tables on the database. `UDIS` and `dollars` table in the database has 2 columns (`date`, and `value`) and looks like this:

![Alt text](documentation/tables_structure.png?raw=true "Table example")

### Considerations!
-----------------

  - The database is used to store the data about dollars and UDIS, when a user search a date inside of a previous range the response is faster because the results on the databases are user but when the user search for date outside a previous range then the search is requested to the [Banxico service], but when the request in partially in our database then the request made to the [Banxico service] has a fix range in which we only request tthe data missing.

### Installation
-----------------

1) Clone the repository (`.env` file is exposed for demonstration purposes, that said, this doesn't represent security leak)

2) Build the containers

    ```sh
    $ docker-compose up
    ```
    After this step you should see a message from the DB container like this: `database system is ready to accept connections`, other from the backend service: 
    ```
        * Serving Flask app "run.py"
    web_1  |  * Environment: production
    web_1  |    WARNING: This is a development server. Do not use it in a production deployment.
    web_1  |    Use a production WSGI server instead.
    web_1  |  * Debug mode: off
    ```
    And the last one from the frontend service:
    ```
      Compiled successfully!
      frontend_1       | 
      frontend_1       | You can now view frontend in the browser.
      frontend_1       | 
      frontend_1       |   Local:            http://localhost:3000
      frontend_1       |   On Your Network:  http://172.22.0.3:3000
      frontend_1       | 
      frontend_1       | Note that the development build is not optimized.
      frontend_1       | To create a production build, use npm run build.
      frontend_1       | 
    ```
    At this point, all the service are running and ready.

3) Open a browser tab an go to ```http://localhost:3000/```
4) At top of the page you can select a change the range you are interested in.

![Alt text](documentation/select_range.png?raw=true "Select range")

5) Visualize the data, also you can download the data or the plot.

![Alt text](documentation/plot.png?raw=true "Plot")

6) (Optional) You can see the backend response using for example `postman`. You can find some example requests below:


### API Examples
-----------------

The request structure is the same for both resource, then you can change `dollars` by `UDIS`.

1) Getting the dollar daily price from `03-oct-2020` to `03-nov-2020`:

Request:
  ```json
  localhost:5000/dollars?start_date=2020-10-03&end_date=2020-11-03
  ```
Respone:
  ```json
  {
    "avg": 21.2118,
    "data": [
        {
            "date": "Mon, 05 Oct 2020 00:00:00 GMT",
            "value": 21.396
        },
        {
            "date": "Tue, 06 Oct 2020 00:00:00 GMT",
            "value": 21.4507
        },
        {
            "date": "Wed, 07 Oct 2020 00:00:00 GMT",
            "value": 21.493
        },
        {
            "date": "Thu, 08 Oct 2020 00:00:00 GMT",
            "value": 21.4318
        },
        {
            "date": "Fri, 09 Oct 2020 00:00:00 GMT",
            "value": 21.1822
        },
        {
            "date": "Mon, 12 Oct 2020 00:00:00 GMT",
            "value": 21.2183
        },
        {
            "date": "Tue, 13 Oct 2020 00:00:00 GMT",
            "value": 21.3677
        },
        {
            "date": "Wed, 14 Oct 2020 00:00:00 GMT",
            "value": 21.2998
        },
        {
            "date": "Thu, 15 Oct 2020 00:00:00 GMT",
            "value": 21.3832
        },
        {
            "date": "Fri, 16 Oct 2020 00:00:00 GMT",
            "value": 21.1765
        },
        {
            "date": "Mon, 19 Oct 2020 00:00:00 GMT",
            "value": 21.1342
        },
        {
            "date": "Tue, 20 Oct 2020 00:00:00 GMT",
            "value": 21.0902
        },
        {
            "date": "Wed, 21 Oct 2020 00:00:00 GMT",
            "value": 21.064
        },
        {
            "date": "Thu, 22 Oct 2020 00:00:00 GMT",
            "value": 21.03
        },
        {
            "date": "Fri, 23 Oct 2020 00:00:00 GMT",
            "value": 20.9205
        },
        {
            "date": "Mon, 26 Oct 2020 00:00:00 GMT",
            "value": 20.9818
        },
        {
            "date": "Tue, 27 Oct 2020 00:00:00 GMT",
            "value": 20.8798
        },
        {
            "date": "Wed, 28 Oct 2020 00:00:00 GMT",
            "value": 21.1648
        },
        {
            "date": "Thu, 29 Oct 2020 00:00:00 GMT",
            "value": 21.377
        },
        {
            "date": "Fri, 30 Oct 2020 00:00:00 GMT",
            "value": 21.2508
        },
        {
            "date": "Tue, 03 Nov 2020 00:00:00 GMT",
            "value": 21.1555
        }
    ],
    "max": 21.493,
    "min": 20.8798
  }
  ```


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [Python 3]: <https://www.python.org/>
   [SQLAlchemy]: <https://www.sqlalchemy.org/>
   [MySQL]: <https://www.mysql.com/>
   [Docker]: <https://www.docker.com/>
   [Banxico Service]: <https://www.banxico.org.mx/SieAPIRest/service/v1/;jsessionid=5fa4f900baccc38cd60cb4f38981>
   [React]: <https://es.reactjs.org/>
   [Typescript]: <https://www.typescriptlang.org/>
   [ApexCharts]: <https://apexcharts.com/>
   [Axios]: <https://github.com/axios/axios>
