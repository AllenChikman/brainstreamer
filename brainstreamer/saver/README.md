
## Saver

The saver is available as brainstreamer.saver and expose the following API:

```
>>> from cortex.saver import Saver
>>> saver = Saver(database_url)
>>> data = …
>>> saver.save( 'pose' , data)
```

Which connects to a database, accepts a topic name and some data, as consumed from the
message queue, and saves it to the database.

It is also provides the following CLI:

```
$ python -m cortex.saver save \
-d/--database 'postgresql://127.0.0.1:5432' \
'pose' \
'pose.result'
```

Which accepts a topic name and a path to some raw data, as consumed from the message
queue, and saves it to a database.

The CLI also supports running the saver as a service, which works with a message queue
indefinitely.

```
$ python -m cortex.saver run-saver \
'postgresql://127.0.0.1:5432' \
'rabbitmq://127.0.0.1:5672/'
```
