
## Server

The server is available as cortex.server and exposes the following API:

```pycon
>>> from cortex.server import run_server
>>> def print_message (message):
... print (message)
>>> run_server(host= '127.0.0.1' , port= 8000 , publish=print_message)
… # listen on host : port and pass received messages to publish
```

And in the following CLI:
```
$ python -m cortex.server run-server \
-h/--host '127.0.0.1' \
-p/--port 8000 \
'rabbitmq://127.0.0.1:5672/'
```
