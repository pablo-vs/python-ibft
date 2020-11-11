#!/bin/bash

tmux \
  new-session  "python python_ibft/server.py 0 --input-value 'decaide this' --test-validity 'decide_this'; read" \; \
  split-window "python python_ibft/server.py 1 --input-value 'decaide this' --test-validity 'decide_this'; read" \; \
  split-window "python python_ibft/server.py 2 --input-value 'decaide this' --test-validity 'decide_this'; read" \; \
  split-window "python python_ibft/server.py 3 --input-value 'decide this' --test-validity 'decide_this'; read" \; \
  split-window "bash test/wait.sh" \; \
  select-layout tiled

