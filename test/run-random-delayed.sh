#!/bin/bash

tmux \
  new-session  "python run.py 0 --random-values --input-value 'decide this'; read" \; \
  split-window "python run.py 1 --online-delayed --input-value 'decide this'; read" \; \
  split-window "python run.py 2 --input-value 'decide this'; read" \; \
  split-window "python run.py 3 --input-value 'decide this'; read" \; \
  split-window "bash test/wait.sh; read" \; \
  select-layout tiled