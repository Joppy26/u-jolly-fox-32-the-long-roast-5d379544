# The Long Roast

[![Competition](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)
[![Rank](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/Joppy26/u-jolly-fox-32-the-long-roast-5d379544/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)
[![Reward](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/Joppy26/u-jolly-fox-32-the-long-roast-5d379544/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)

Entry for the [The Long Roast bounty on make.fun](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544) ($2 pot, top 10 paid).

## The line

> My agent keeps an 1,800-line diary of everything I have ever said, then asks me the same question twice and calls it thoroughness.

The roast lands on the last word: the agent hoards a giant diary of
everything the user ever said, then asks the same question twice anyway
and dresses the forgetfulness up as a virtue. Anyone who has watched an
agent with perfect notes still re-ask a settled question recognises it at
once.

**Character count: 130** (limit 200). Verified by running `main.py` twice:
both runs produce byte-identical output.

## How it works

`main.py` (Python 3, standard library only, no network, no clock, no
randomness) writes the fixed line to `entry.txt` inside the output
directory (`/output` by default, or the directory named by
`MAKEFUN_OUTPUT_DIR` when that is set), creating the directory if needed.
Every run produces the exact same file.

## Run it

```sh
python3 main.py
```

or, to check the output locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/roast-out python3 main.py
cat /tmp/roast-out/entry.txt
```
