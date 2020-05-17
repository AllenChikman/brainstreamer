#!/bin/bash
python -m brainstreamer.server run-server "rabbitmq://127.0.0.1:5672" &
python -m brainstreamer.parsers run-parsers &
python -m brainstreamer.saver run-saver &



