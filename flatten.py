import sys
import json

from typing import Dict, List


def _flatten(data: Dict, prefix: List[str]) -> Dict:
    flattened = {}

    for (key, value) in data.items():
        prefixes = prefix + [key]

        if isinstance(value, dict):
            x = _flatten(value, prefixes)
            flattened.update(x)
        else:
            prefix_key = ".".join(prefixes)
            flattened[prefix_key] = value

    return flattened


def flatten(data: Dict) -> Dict:
    """Flattens a key-value object.

    Nested keys are represented by a dot-separated prefix.
    """

    return _flatten(data, [])


if __name__ == "__main__":
    data = json.loads(sys.stdin.read())
    flattened = flatten(data)

    print(json.dumps(flattened))
