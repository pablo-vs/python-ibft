# python-ibft
Python implementation of Istanbul BFT algorithm using Flask. Experimental

## Requirements

Needs python3, flask, tmux (for `test/run*.sh` scripts)

## Testing

Run
```bash
test/run.sh
```
to try it out; tmux required.
Several scripts to experiment with defective parties are included in `test/run*.sh`.

You can also run it directly (but you'll need to launch all the nodes manually)

```bash
python run.py 0 --lambda "decide this"
```

## More info

Implements the Istanbul BFT algorithm according to this paper: https://arxiv.org/abs/2002.03613
