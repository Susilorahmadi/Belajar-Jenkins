import json, requests
import logging
from jwcrypto import jwk, jwe
import time
import datetime
import random

def daydate (stddate):
    fmt='%Y-%m-%d'
    sdtdate = datetime.datetime.strptime(stddate, fmt)
    sdtdate = sdtdate.timetuple()
    jdate = str(sdtdate.tm_yday)
    if len (jdate) == 1:
        jdate = "00" + jdate
    if len (jdate) == 2:
        jdate = "0" + jdate        
    return(jdate)

date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
systemsTraceAuditNumber = str(random.randint(100000,999999))

def generateRetrievalReferenceNumber (date, systemsTraceAuditNumber):
    
    stddate = date.split('T')[0]
    #print(stddate)
    lastYearDigit = stddate.split('-')[0][-1]
    #print(lastYearDigit)
    daysCount = daydate(stddate)
    #print(jdate)
    hour = date.split('T')[1].split(':')[0]
    #print(hour)
    
    retrievalReferenceNumber = lastYearDigit + daysCount + hour + systemsTraceAuditNumber
    return(retrievalReferenceNumber)

retrievalReferenceNumber = generateRetrievalReferenceNumber (date, systemsTraceAuditNumber)

def loadPem(filePath):
    with open(filePath, "rb") as pemfile:
        return jwk.JWK.from_pem(pemfile.read())

# Enkripdi dan deskripsi req
def encrypt(payload, server_cert, myKey_ID):
    payload = json.dumps(payload)
    protected_header = {
            "alg": "RSA-OAEP-256",
            "enc": "A128GCM",
            "kid": myKey_ID,
            "iat": int(round(time.time() * 1000))
        }
    jwetoken = jwe.JWE(payload.encode('utf-8'),
                            recipient=loadPem(server_cert),
                            protected=protected_header)
    encryptedPayload = jwetoken.serialize(compact=True)
    return {"encData": encryptedPayload} 
 
def decrypt(encPayload, private_key):
    # print(encPayload)
    # if type(encPayload) is str:
    #     payload = json.loads(encPayload)
    if encPayload.get('encData', True):
        jwetoken = jwe.JWE()
        jwetoken.deserialize(encPayload["encData"], key=loadPem(private_key))
        return jwetoken.payload
    return encPayload  

senderReferenceNumber = str(random.randint(1000000000,9999999999))

cert         = 'D:/Development/G20/G20-virtual-account/topup-refund/app/key/project_susilo_G20coba/cert.pem'
key          = 'D:/Development/G20/G20-virtual-account/topup-refund/app/key/project_susilo_G20coba/private_key.pem'

user_id      = '0I31X4XF9LFQUSC8FGE621vvUCRLOe_dsLGRyrOl0vqhyV8S4'
password     = 'ljDd9vhOJA4yOHKCBD68mu3iivLL0hp4k'

myKey_ID    = 'ac61b4ae-aa3d-47d8-ab9c-1e18f94e63c8'
server_cert = 'D:/Development/G20/G20-virtual-account/topup-refund/app/key/project_susilo_G20coba/server_cert_ac61b4ae-aa3d-47d8-ab9c-1e18f94e63c8.pem'
private_key = 'D:/Development/G20/G20-virtual-account/topup-refund/app/key/project_susilo_G20coba/client_private_key.pem'

headers = { "content-type": "application/json",
            'accept': 'application/json',
            'keyId': myKey_ID
            }
