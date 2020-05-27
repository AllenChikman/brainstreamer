#!/bin/bash
python -m brainstreamer.server run-server "rabbitmq://127.0.0.1:5672" &
python -m brainstreamer.parsers run-parsers &
python -m brainstreamer.saver run-saver "mongodb://127.0.0.1:27017" "rabbitmq://127.0.0.1:5672" &
python -m brainstreamer.api run-server &
python -m brainstreamer.gui run-server &
