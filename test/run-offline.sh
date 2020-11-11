#!/bin/bash

tmux \
  new-session  "python python_ibft/server.py 0 --offline --input-value 'decide this'; read" \; \
  split-window "python python_ibft/server.py 1 --input-value 'decide this'; read" \; \
  split-window "python python_ibft/server.py 2 --input-value 'decide this'; read" \; \
  split-window "python python_ibft/server.py 3 --input-value 'decide this'; read" \; \
  split-window "bash test/wait.sh; read" \; \
  select-layout tiled