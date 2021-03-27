import sys
import json

from typing import Dict, List


def flatten(data: Dict) -> Dict:
    return data


if __name__ == "__main__":
    data = json.loads(sys.stdin.read())

    print(flatten(data))
