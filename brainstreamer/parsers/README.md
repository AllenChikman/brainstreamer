
## Parsers

### Usage

The parsers are available as brainstreamer.parsers and exposes the following API:

```pycon
>>> from cortex.parsers import run_parser
>>> data = …
>>> result = run_parser( 'pose' , data)
```

Which accepts a parser name and some raw data, as consumed from the message queue, and returns the result, as published to the message queue.

It also provides the following CLI:

``` python -m cortex.parsers parse 'pose' 'snapshot.raw' > 'pose.result' ```

Which accepts a parser name and a path to some raw data, as consumed from the message
queue, and prints the result, as published to the message queue (optionally redirecting it
to a file).

The CLI should also support running the parsers as a service, which works with a message queue indefinitely.

```$ python -m cortex.parsers run-parser 'pose' 'rabbitmq://127.0.0.1:5672/' ```

### Default available parsers

The default implemented parsers in the project are:
* [pose parser](parsing_drivers/pose.py)
* [feeling parser](parsing_drivers/feelings.py)
* [color-image parser](parsing_drivers/color_image.py)
* [depth-image parser](parsing_drivers/depth_image.py)

### Package implementation

The parsers package structure is the same as any other [platform](../platforms/README.md).
It consists of a ```parsing_manager.py``` file, that gathers all the common logic for the parsers and manages the communication with the message queue. <br>
It also consists of a drivers folder called ``` parsing_drivers ``` which contains all the available parsers.  


### Adding a new parser

Adding a new parser would be quite simple: just add a new .py file under the  ``` parsing_drivers ``` folder,
and implement a function that accepts as an argument a snapshot, uses json to load it, process it and then returns a dictionary of the results. <br>
You will also required to add a function attribue named ```scheme``` with the name of the parser so the ```parsing_manager``` would know to collect the parsing function, with a proper name.

#### Example of a new_parser.py driver that can be added

```pycon
>>> import json
...
...
>>> def parse_something(snapshot):
...     snapshot = json.loads(snapshot)
...     result = ... # do something to proccess snapshot data
... 
...     return dict(some_key=result)
...
...
>>> parse_something.scheme = 'some_name'
```
