# Code challenge

Coding challenge as part of an interview process.
The [assignment](./assignment.md) is to flatten a JSON object passed through stdin.

Time spent: Around 1 hour.
Some time was spent thinking about the problem before initializing the git repo.

## Running 

```console
$ python flatten.py < data.json
```

## Tests

```console
$ python tests.py
```

## Comments
Naming was surprisingly difficult (hence `prefixes`, `x` and `prefix_key`) but other
than that the problem was pretty straight forward.

The code was formatted with [Black](https://github.com/psf/black).
Tested with Python 3.9.2.
