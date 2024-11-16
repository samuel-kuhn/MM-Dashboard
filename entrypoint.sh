#!/bin/bash

if [ ! -f .first_run ]; then
  /bin/bash ./setup.sh
  touch .first_run
  echo "initial setup"
fi

/bin/bash ./run.sh

