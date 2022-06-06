import json
from dataclasses import dataclass, asdict


@dataclass
class AlgorithmResponse:
    bins: list[list[int]]
    sums: list[int]

    def convert_to_dict(self):
        return asdict(self)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
