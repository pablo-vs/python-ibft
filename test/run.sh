#!/bin/bash

tmux \
  new-session  "python run.py 0 --input-value 'decide this'; read" \; \
  split-window "python run.py 1 --input-value 'decide this'; read" \; \
  split-window "python run.py 2 --input-value 'decide this'; read" \; \
  split-window "python run.py 3 --input-value 'decide this'; read" \; \
  split-window "bash test/wait.sh" \; \
  select-layout tiled

