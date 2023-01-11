import json, requests
import logging
from wsgiref import headers
from ast import literal_eval
from visa_MLE import myKey_ID,server_cert,cert,key,user_id,password,private_key,headers,encrypt,decrypt,date,systemsTraceAuditNumber,retrievalReferenceNumber,senderReferenceNumber

payload = json.loads('''
{
  "recipientDetail": {
    "name": "bank BNI",
	  "payoutMethod": "C",
	  "card": {
		  "accountNumber": "4957030420210462"
	  }
  },
  "senderDetail": {
    "senderReferenceNumber": "'''+ senderReferenceNumber+'''",
	  "name": "bank BNI",
    "address": {
      "country": "360",
      "city": "indonesia",
	    "addressLine1": "Menara BNI pejompongan"
    },
    "sourceOfFunds": "05"
  },
  "originatorDetail": {
    "originatorName": "Bank Negara Indonesia",
    "bankId": "408999",
	  "bankCountryCode": "360",
	  "address": {
		  "country": "360"
	  },
    "merchantCategoryCode": "6012",
    "originatorId": "77765",
	  "terminalId": "123456"
  },
  "transactionDetail": {
    "systemTraceAuditNumber": "'''+ systemsTraceAuditNumber +'''",
    "localTransactionDateTime": "''' + date + '''",
    "businessApplicationId": "PP",
    "transactionAmount": "100",
    "transactionCurrencyCode": "840",
    "retrievalReferenceNumber": "''' + retrievalReferenceNumber + '''"
  }
}
''')

url     = 'https://sandbox.api.visa.com/visapayouts/v2/payouts'
# headers = { "content-type": "application/json",
#             'accept': 'application/json',
#             'keyId': myKey_ID
#             }

timeout = 10

encryptedPayload = encrypt(payload, server_cert, myKey_ID)
try:
    response = requests.post(url,
                    cert = (cert, key),
                    headers = headers,
                    auth = (user_id, password),
                    json = encryptedPayload,
                    # json = payload,
                    timeout=timeout
 )
except Exception as e:
    print (e)

decryptedPayload_Query_API = decrypt(response.json(), private_key)

data_Query_API = literal_eval(decryptedPayload_Query_API.decode('utf8'))

def responseSendPayout() :
  core = json.dumps(data_Query_API)
  print(data_Query_API)
  return core

def error():
  res = data_Query_API['errorResponse']['message']
  return res
  
def valid():
  res = data_Query_API['originatorDetail']['bankId']
  return res

def statusCode():
  data = json.dumps(data_Query_API)
  if('errorResponse' in data):
    print("500")
    print("Error Response : " + error())
  elif('originatorDetail' in data):
    print("200")
    print("BankID : " + valid())

print("*****************************")
print(payload)
print("*****************************")
responseSendPayout()
statusCode()
print("*****************************")

