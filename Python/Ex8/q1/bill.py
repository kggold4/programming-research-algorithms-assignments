from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Bill:
    BillID: int
    Name: str
    KnessetNum: int
    StatusID: int
    PrivateNumber: int
    LastUpdatedDate: datetime

    def __repr__(self):
        """
        Take help from: https://stackoverflow.com/questions/11637293/iterate-over-object-attributes-in-python
        :return:
        """
        result = ''
        for attribute in [a for a in dir(self) if not a.startswith('__')]:
            result += f'{attribute}: {self.__getattribute__(attribute)}\n'
        return result

    def convert_to_dict(self):
        return asdict(self)
