#!/bin/bash

if [ ! -f /.first_run ]; then
  /bin/bash /app/setup.sh
  touch /.first_run
fi

/bin/bash /app/run.sh

