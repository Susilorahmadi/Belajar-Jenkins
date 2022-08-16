import json,requests
from ast import literal_eval
from visa_MLE import myKey_ID,server_cert,cert,key,user_id,password,private_key,encrypt,decrypt


payload = json.loads('''
{
  "rateProductCode": "A",
  "markupRate": "0.07",
  "destinationCurrencyCode": "360",
  "sourceAmount": "100",
  "sourceCurrencyCode": "840"
}
''')

url     = 'https://sandbox.api.visa.com/forexrates/v2/foreignexchangerates'
headers = { "content-type": "application/json",
            'accept': 'application/json',
            'keyId': myKey_ID
            }
        
encryptedPayload = encrypt(payload, server_cert, myKey_ID)

timeout = 10
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

def responseForeign() :
  core = json.dumps(data_Query_API)
  print(data_Query_API)
  return core

def error():
  res = data_Query_API['errorResponse']['message']
  return res

print("========")
responseForeign()
print("========")