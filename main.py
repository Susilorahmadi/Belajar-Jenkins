from ast import literal_eval
import logging
import requests,json
from visa_MLE import date,systemsTraceAuditNumber,retrievalReferenceNumber
import defusedxml.ElementTree as ET

def visaDirectcall(req_sending, url):
    from visa_MLE import myKey_ID,server_cert,cert,key,user_id,password,private_key,headers,encrypt,decrypt
    
    print("==================connnect to "+ url +"============")
    print("************Request Visa************")
    print(req_sending)
    timeout = 60
    encryptedPayload = encrypt(req_sending, server_cert, myKey_ID)
    try:
        r = requests.post(url,
                    cert = (cert, key),
                    headers = headers,
                    auth = (user_id, password),
                    json = encryptedPayload,
                    timeout=timeout
                    # proxies={'http': https_proxy, 'https': https_proxy}
    )
    except Exception as e:
        print (e)

    decryptedPayload_Query_API = decrypt(r.json(), private_key)
    data_Query_API = literal_eval(decryptedPayload_Query_API.decode('utf8'))

    response_Visa = json.dumps(data_Query_API)
    print("************Response Visa************")
    print(data_Query_API)
    print("************Response Visa************/n")

    return data_Query_API

url_card = 'https://sandbox.api.visa.com/pav/v1/cardvalidation'
payload_card = json.loads('''
{
  "cardCvv2Value": "022",
  "primaryAccountNumber": "760360289402716",
  "cardExpiryDate": "2040-10",
  "systemsTraceAuditNumber": "''' + systemsTraceAuditNumber +'''",
  "retrievalReferenceNumber": "''' + retrievalReferenceNumber +'''"
}
''')
card_valid = visaDirectcall(payload_card,url_card)

if('errorMessage' in card_valid):
    print('error')
else:
    url_fx = 'https://sandbox.api.visa.com/forexrates/v2/foreignexchangerates'
    payload_fx = json.loads('''
    {
    "rateProductCode": "A",
    "markupRate": "0.07",
    "destinationCurrencyCode": "360",
    "sourceAmount": "100",
    "sourceCurrencyCode": "840"
    }
    ''')
    card_fx = visaDirectcall(payload_fx,url_fx)

    if('errorResponse' in card_fx):
        print('error')
    else:    
        CORESERVICE_URL  = 'http://192.168.151.220:57004/CoreService'
        HEADER_XML       = {'Content-Type': 'text/xml'}
        request_balance = '''<soapenv:Envelope xmlns:q0="http://service.bni.co.id/core" xmlns:bo="http://service.bni.co.id/core/bo" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <soapenv:Body>
        <q0:transaction>
            <request>
                <systemId>IBANK</systemId>
                <systemJournal/>
                <content xsi:type="bo:BalanceInfoReq">
                    <accountNum>9891231000291398</accountNum>
                </content>
            </request>
        </q0:transaction>
        </soapenv:Body>
        </soapenv:Envelope>'''

        resp_balance        = requests.post(CORESERVICE_URL, data=request_balance, headers=HEADER_XML)
        logging.info('>>>>>>>>>>>> connect to ' + CORESERVICE_URL +' >>>>>>>>>>>>>>>')
        logging.info('>>>>>>>>>>>> request >>>>>>>>>>>>>>>')
        logging.info(request_balance)
        logging.info('>>>>>>>>>>>> response >>>>>>>>>>>>>>>')
        resp_balance        = requests.post(CORESERVICE_URL, data=request_balance, headers=HEADER_XML)
        logging.info(resp_balance.text)

        xml_resp                    = ET.fromstring(resp_balance.text)
        Balance	                    = xml_resp.findtext('.//balance')
        error_desc                  = xml_resp.findtext('.//errorDescription')
        reques                      = 4000000000000000000
        if(error_desc is not None):
                print('errorMessage :' +error_desc)
        else:
            reduction_result            = int(Balance) - reques
            if(reduction_result <= 5000):
                print('DANA kurang !!')
            else:
                print(reduction_result)
                print('send payout')
                import send_visa