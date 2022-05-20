from bill import Bill
from data_data_from_api import get_kns_bill_data
from data_utils import build_bill_objects, print_bills


def main():
    data = get_kns_bill_data()
    bill_data: list[Bill] = build_bill_objects(data)
    print_bills(bill_data)
    


if __name__ == '__main__':
    main()
