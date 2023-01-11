import json, requests
from wsgiref import headers
from ast import literal_eval
from visa_MLE  import myKey_ID,server_cert,cert,key,user_id,password,private_key,encrypt,decrypt,systemsTraceAuditNumber,retrievalReferenceNumber

payload = json.loads('''
{
  "cardCvv2Value": "022",
  "primaryAccountNumber": "4957030420210462",
  "cardExpiryDate": "2040-10",
  "systemsTraceAuditNumber": "''' + systemsTraceAuditNumber +'''",
  "retrievalReferenceNumber": "''' + retrievalReferenceNumber +'''"
}
''')


url     = 'https://sandbox.api.visa.com/pav/v1/cardvalidation'
headers = { "content-type": "application/json",
            'accept': 'application/json',
            'keyId': myKey_ID
            }

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

def responseValidation() :
  core = json.dumps(data_Query_API)
  print(data_Query_API)
  return core

print("*****************************")
responseValidation()
# statusCode()
print("*****************************")

