[![Build Status](https://travis-ci.org/AllenChikman/brainstreamer.svg?branch=master)](https://travis-ci.org/AllenChikman/brainstreamer)
[![codecov](https://codecov.io/gh/AllenChikman/brainstreamer/branch/master/graph/badge.svg)](https://codecov.io/gh/AllenChikman/brainstreamer)

# brainstreamer
Imaginary hardware , that can read minds, and upload snapshots of cognitions.
This is the final project in awesome course: Advanced-System-design of [Dan Gittik](https://github.com/dan-gittik).


## Prerequisites


[Python 3.8](https://www.python.org/downloads/release/python-382/).

[Docker](https://docs.docker.com/engine/install/ubuntu/).

[docker-compose](https://docs.docker.com/compose/install/).

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

After that, upload some snapshots from the [client](/brainstreamer/client/README.md):
```sh
[brainstreamer] $ python -m brainstreamer.client upload-sample sample.mind.gz
...
All the 1024 snapshots were sent successfully!
[brainstreamer] $ 
```    
    
## Project's Pipeline
![brainstreamer_pipeline](https://user-images.githubusercontent.com/37861691/82965333-79945680-9fd0-11ea-8e41-bbfb7f2e891b.png)

