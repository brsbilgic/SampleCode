from visa.helpers.visa_api_client import VisaAPIClient
import json
import datetime
import unittest
'''
@author: visa
'''

class TestFundsTransfer(unittest.TestCase):

    def setUp(self):
        date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        self.visa_api_client = VisaAPIClient()
        self.push_funds_request = {
            "acquirerCountryCode": "840",
            "acquiringBin": "408999",
            "amount": "124.05",
            "businessApplicationId": "AA",
            "cardAcceptor": {
            "address": {
            "country": "USA",
            "county": "San Mateo",
            "state": "CA",
            "zipCode": "94404"
            },
            "idCode": "CA-IDCode-77765",
            "name": "Visa Inc. USA-Foster City",
            "terminalId": "TID-9999"
            },
            "localTransactionDateTime": date,
            "merchantCategoryCode": "6012",
            "pointOfServiceData": {
            "motoECIIndicator": "0",
            "panEntryMode": "90",
            "posConditionCode": "00"
            },
            "recipientName": "rohan",
            "recipientPrimaryAccountNumber": "4957030420210462",
            "retrievalReferenceNumber": "412770451018",
            "senderAccountNumber": "4957030420210454",
            "senderAddress": "901 Metro Center Blvd",
            "senderCity": "Foster City",
            "senderCountryCode": "124",
            "senderName": "Mohammed Qasim",
            "senderReference": "",
            "senderStateCode": "CA",
            "sourceOfFundsCode": "05",
            "systemsTraceAuditNumber": "451018",
            "transactionCurrencyCode": "USD",
            "transactionIdentifier": "381228649430015"
        }
    
    def test_push_funds_transactions(self):
        base_uri = 'visadirect/'
        resource_path = 'fundstransfer/v1/pushfundstransactions'
        response = self.visa_api_client.do_mutual_auth_request(base_uri + resource_path, self.push_funds_request, 'Push Funds Transaction Test','post')
        self.assertEqual(str(response.status_code) ,"200" ,"Push Funds Transaction test failed")
        pass
