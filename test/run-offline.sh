#!/bin/bash

tmux \
  new-session  "python ibft.py 0 --offline --input-value 'decide this'; read" \; \
  split-window "python ibft.py 1 --input-value 'decide this'; read" \; \
  split-window "python ibft.py 2 --input-value 'decide this'; read" \; \
  split-window "python ibft.py 3 --input-value 'decide this'; read" \; \
  split-window "bash wait.sh; read" \; \
  select-layout tiled