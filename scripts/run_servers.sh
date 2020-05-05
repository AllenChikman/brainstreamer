#!/bin/bash
python -m brainstreamer.server run-server &
python -m brainstreamer.parsers run-parsers &
python -m brainstreamer.saver run-saver &


