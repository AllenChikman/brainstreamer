
## Server

The server is available as brainstreamer.server and exposes the following API:

```pycon
>>> from brainstreamer.server import run_server
>>> run_server(host= '127.0.0.1' , port= 8000 , mq_url='rabbitmq://127.0.0.1:5672/')
```

And in the following CLI:
```
$ python -m brainstreamer.server run-server \
-h/--host '127.0.0.1' \
-p/--port 8000 \
'rabbitmq://127.0.0.1:5672/'
```
