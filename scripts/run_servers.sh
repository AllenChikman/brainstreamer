#!/bin/bash
python -m bci.server run-server &
python -m bci.parsers run-parsers &
python -m bci.saver run-saver &


