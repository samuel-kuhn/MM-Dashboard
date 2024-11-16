#!/bin/bash

if [ ! -f .first_run ]; then
  /bin/bash ./setup.sh
  touch .first_run
fi

/bin/bash ./run.sh

