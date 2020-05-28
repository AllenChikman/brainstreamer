
## GUI

### Implemenation details:


**Backend**: Flask and jinja templates <br>
**FrondEnd**: JS, Query, ajax, html, css


### Usage:

The GUI consumes the API and reflects it.

Usage as a python module:

``` pycon
>>> from cortex.gui import run_server
>>> run_server(
... host = '127.0.0.1 ',
... port = 8080 ,
... api_host = '127.0.0.1' ,
... api_port = 5000 ,
... )
```

Usage from CLI:

```pycon
$ python -m cortex.gui run-server \
-h/--host '127.0.0.1' \
-p/--port 8080 \
-H/--api-host '127.0.0.1' \
-P/--api-port 5000
```
