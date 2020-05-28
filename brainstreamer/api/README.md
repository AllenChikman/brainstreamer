
## API

The API is available as brainstreamer.api and expose the following API:

```pycon
>>> from cortex.api import run_api_server
>>> run_api_server(
... host = '127.0.0.1' ,
... port = 5000 ,
... database_url = 'postgresql://127.0.0.1:5432' ,
... )
… # listen on host : port and serve data from database_url
```

And the following CLI:

```
python -m cortex.api run-server \
-h/--host '127.0.0.1' \
-p/--port 5000 \
-d/--database 'postgresql://127.0.0.1:5432'
```

The API server supports the following RESTful API endpoints:

- **GET /users** - Returns the list of all the supported users, including their IDs and names only.
- **GET /users/ user-id** - Returns the specified user's details: ID, name, birthday and gender.
- **GET /users/ user-id /snapshots** - Returns the list of the specified user's snapshot IDs and datetimes only.
- **GET /users/ user-id /snapshots/ snapshot-id** - Returns the specified snapshot's details: ID, datetime, and the available results'
names only (e.g. pose ).
- **GET /users/ user-id /snapshots/ snapshot-id / result-name** - Returns the specified snapshot's results.
