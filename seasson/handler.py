import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',level=logging.INFO,datefmt='`%Y-%m-%d %H:%M:%S')

def handle(e, c):
    _fullPath   = e.path
    logging.info("=========== START REQUEST ===========")
    logging.info(e.path)
    
    if "/inquiry" in _fullPath :
        inquiry = 'Anda sedang melakukan inquery'
        logging.info(inquiry)
        return {"statusCode": 200,"body": inquiry}
    elif "/payment" in _fullPath :
        payment = ''
        return payment
    elif "/status" in _fullPath :
        status = ''
        return status