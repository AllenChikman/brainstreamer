#!/bin/bash

cd "$(dirname "${BASH_SOURCE[0]}")" || exit

function main() {
  docker-compose up -d
  echo "All dockers are up."
}

main "$@"
