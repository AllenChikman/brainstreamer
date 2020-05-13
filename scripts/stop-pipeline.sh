#!/bin/bash

cd "$(dirname "${BASH_SOURCE[0]}")" || exit

function main() {
  docker-compose stop
  echo "All dockers are stopped."
}

main "$@"
