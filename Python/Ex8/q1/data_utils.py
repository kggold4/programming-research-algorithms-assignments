from datetime import datetime
from bill import Bill

DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S'


def build_bill_objects(data) -> list[Bill]:
    """
    get data in OrderedDict and return a list with Bill objects
    :param data:
    :return:
    """
    bills = []
    for bill_data in data:
        bill_data_content = bill_data.get('content').get('m:properties')
        bills.append(
            Bill(
                BillID=int(bill_data_content['d:BillID']['#text']),
                Name=str(bill_data_content['d:Name']),
                KnessetNum=int(bill_data_content['d:KnessetNum']['#text']),
                StatusID=int(bill_data_content['d:StatusID']['#text']),
                PrivateNumber=int(bill_data_content['d:PrivateNumber']['#text']),
                LastUpdatedDate=datetime.strptime(bill_data_content['d:LastUpdatedDate']['#text'].split('.')[0],
                                                  DATETIME_FORMAT)
            )
        )
    return bills


def print_bills(bills_data: list[Bill]):
    for bill in bills_data:
        print(bill)
