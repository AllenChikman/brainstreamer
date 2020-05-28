
## Platforms
This package provides platforms of different types: database, message queue, readers etc.

Each sub-package corresponds to a type of a platform. It consists of:
* A wrapper module that wrapps the shared api all the other drivers has to follow.
* A folder containing one or more driver implementation (.py files) that all follow the defined API by the wrapper class.

You can see an example for the message_queue platform folder hierarchy [here](message_queue)

Adding a new driver would be quite simple:
just add a new driver that implements the API defined by the wrapper class, and add a class attribute ```scheme``` with the name of the driver. <br>
All the rest is taken care of, and your new driver will be available for usage with the given name.


#### Example for of the `message_queue` platform:


MqWrapper implementation would look like:

```pycon
>>> class MqWrapper:
... 
...   def __init__(self, url):
...      url = furl(url)
...      scheme, host, port = url.scheme, url.host, url.port
...  
...      if scheme not in mq_drivers:
...          raise ValueError(f"Unsupported MQ driver: {scheme}")
...      try:
...          self.mq = mq_drivers[scheme](host, port)
...      except ConnectionError:
...          raise ConnectionError(f"Couldn't connect to MQ driver: {scheme}")
... 
...   def publish(self, topic, message):
...      self.mq.publish(topic, message)
... 
...   def consume(self, topic, handler):
...      self.mq.consume(topic, handler)
```

Now, every driver would have to follow the ```publish```,```consume``` API.<br>
For example, rabbit_mq driver would look like:

```pycon
>>> class RabbitMq:
...     scheme = 'rabbitmq'
...    
...     def __init__(self, host, port):
...         self.host = host
...         self.port = port
...         ...
...    
...     def publish(self, topic, message):
...         ...
...    
...     def consume(self, topic, handler):
...         ...
```

And to use a message queue of type rabbitMQ:
```pycon
>>> from brainstreamer.platforms import MqWrapper
>>> url = 'rabbitmq://127.0.0.1:5672/'
>>> mq = MqWrapper(url)
>>> mq.publish(topic, message) # publish a given message on a given topic
``` 
