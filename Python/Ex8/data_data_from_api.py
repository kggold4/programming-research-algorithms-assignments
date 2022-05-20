import requests
import xmltodict

URL = "http://knesset.gov.il/Odata/ParliamentInfo.svc/KNS_Bill()?$filter=SubTypeID%20eq%2054&$expand=KNS_BillInitiators"


def get_kns_bill_data():
    """
    Get the KNS Bill data
    Get help from: https://stackoverflow.com/questions/18308529/python-requests-package-handling-xml-response
    :return:
    """
    response = requests.get(URL)
    response.raise_for_status()
    xml_data = xmltodict.parse(response.content)
    xml_data_entries = xml_data.get('feed').get('entry')
    return xml_data_entries
