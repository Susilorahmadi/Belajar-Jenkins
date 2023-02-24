import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',level=logging.INFO,datefmt='`%Y-%m-%d %H:%M:%S')

def handle(e, c):
    _fullPath   = e.path
    logging.info("=========== START REQUEST ===========")
    logging.info(_fullPath)
    logging.info("=========== Response ============")
    
    if "/inquiry" in _fullPath :
        inquiry = 'Berhasil Inquiry'
        logging.info(inquiry)
        return {"statusCode": 200,"body": inquiry}
    elif "/payment" in _fullPath :
        inquiry = 'Berhasil Payment'
        logging.info(inquiry)
        return {"statusCode": 200,"body": inquiry}
    elif "/status" in _fullPath :
        inquiry = 'Berhasil cek Status'
        logging.info(inquiry)
        return {"statusCode": 200,"body": inquiry}