from bill import Bill
from get_data_from_api import get_kns_bill_data
from data_utils import build_bill_objects, print_bills
from db_utils import DBUtils


def main():
    # bill_data = get_kns_bill_data()
    # bill_objects: list[Bill] = build_bill_objects(bill_data)
    # print_bills(bill_objects)

    db_utils = DBUtils()

    # db_utils.create_table()

    # for bill_object in bill_objects:
    #     db_utils.insert(bill=bill_object)

    db_utils.print_table(num_of_rows=10)
    db_utils.close()


if __name__ == '__main__':
    main()
