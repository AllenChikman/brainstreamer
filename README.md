[![Build Status](https://travis-ci.org/AllenChikman/brainstreamer.svg?branch=master)](https://travis-ci.org/AllenChikman/brainstreamer)
[![codecov](https://codecov.io/gh/AllenChikman/brainstreamer/branch/master/graph/badge.svg)](https://codecov.io/gh/AllenChikman/brainstreamer)

# brainstreamer
Imaginary hardware , that can read minds, and upload snapshots of cognitions. <br>
This is the final project in the awesome course: _Advanced-System-design_ of [Dan Gittik](https://github.com/dan-gittik).


## Prerequisites

- [Python 3.8](https://www.python.org/downloads/release/python-382/)
- [Docker](https://docs.docker.com/engine/install/ubuntu/)
- [docker-compose](https://docs.docker.com/compose/install/)

## Installation

1. Clone the repository and enter it:

    ```sh
    $ git clone https://github.com/AllenChikman/brainstreamer.git
    ...
    $ cd brainstreamer
    ```

2. Run the installation script and activate the virtual environment:

    ```sh
    $ ./scripts/install.sh
    ...
    $ source .env/bin/activate
    [brainstreamer] $ # you're good to go!
    ```

3. To check that everything is working as expected, run the tests:

    ```sh
    [brainstreamer] $ pytest tests/
    ...
    ```

## Quickstart
After finishing the [installation](#installation) step, run the `run-pipeline` script to set up all the
necessary services:

```sh
[brainstreamer] $ ./scripts/run-pipeline.sh
...
Everything is ready!
[brainstreamer] $
```

Please note that the first time set up may take some time.

Copy the desired binary sample you woul'd like to read from to the ```/data``` folder.
(if you'd like to use the full sample, you can download it from [here](https://storage.googleapis.com/advanced-system-design/sample.mind.gz)). <br>
For your convenience, a mini-sample is already available at the ```/data``` folder .

After that, upload some snapshots from the [client](/brainstreamer/client/README.md). <br>
For usage of the mini-sample provided:

```sh
[brainstreamer] $ python -m brainstreamer.client upload-sample ./brainstreamer/data/mini_sample.gz"
...
Brain Streaming succeeded. All the 1 snapshots were uploaded!
[brainstreamer] $ 
```    
For usage of the a full sample (after it is copied to the ```/data``` folder:

```sh
[brainstreamer] $ python -m brainstreamer.client upload-sample --num-snaps 20 "./brainstreamer/data/sample.mind.gz"
...
Brain Streaming succeeded. All the 20 snapshots were uploaded!
[brainstreamer] $ 
```    

#### Note:
If not necessary, try to use small values for the  ```--num-snaps``` parameter to ensure a smooth and fast flow.

Now you can use the [`cli`](/brainstreamer/cli/README.md) to consume the the data, or use the [`gui`](/brainstreamer/gui/README.md) to see an nice visualization of the data, in a website (default address will be: [http://localhost:8080](http://localhost:8080))

## Project's Pipeline
![brainstreamer_pipeline](https://user-images.githubusercontent.com/37861691/82965333-79945680-9fd0-11ea-8e41-bbfb7f2e891b.png)

## Usage

The project contains one main package, `brainstreamer`, which contains several sub-packages.<br>
Each sub-package represents a micoservice of the project, which contains its own README file.<br>
For examples and further read:

* [`client`](/brainstreamer/client/README.md) - uploads snapshots to the server.
* [`server`](/brainstreamer/server/README.md) - receives the snapshots from the client, processes and publishes them to the [`MQ`](/brainstreamer/platforms/message_queue).
* [`parsers`](/brainstreamer/parsers/README.md) - consumes and parses the snapshots published by the server,and then publishing it back to the saver.
* [`saver`](/brainstreamer/saver/README.md) - consumes and saves the parsed data to the database.
* [`api`](/brainstreamer/server/README.md) - a REST API exposed to consume the data.
* [`cli`](/brainstreamer/cli/README.md) - a CLI that consumes the API.
* [`gui`](/brainstreamer/gui/README.md) - visualization of the data.
* [`platforms`](/brainstreamer/platforms/README.md) - several platforms that provide services to all the components

## Support

For contact please feel free to reach me on:
* Email - allenchikman@gmail.com 
