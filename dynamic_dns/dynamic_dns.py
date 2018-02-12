import os
import os.path
import sys
import json
import logging
import argparse
import traceback

from aliyunsdkcore import client
from aliyunsdkcore.request import RpcRequest

PARSER = argparse.ArgumentParser(description="dynamic_dns")

PARSER.add_argument("-n", "--hostname", action="store",
                    dest="hostname",  required=True)

FORMAT = "%(asctime)s %(thread)d %(levelname)s %(filename)s:%(lineno)d:%(funcName)s %(message)s"

LOG_FILE = "/var/log/dynamic_dns/dynamic_dns.log"

LOG_DIR = os.path.dirname(LOG_FILE)
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[logging.FileHandler(LOG_FILE,  mode="a")],
    format=FORMAT
)

logger = logging.getLogger(__name__)


def error_handler(etype, value, tb):
    err_str = '{} {} {}'.format(etype, value, traceback.format_tb(tb))
    logger.error(err_str)

    # make sure exit
    exit(-1)


ACCESS_KEY_ID = "/etc/dynamic_dns/access_key_id"
ACCESS_KEY_SECRET = "/etc/dynamic_dns/access_key_secret"


def get_access():
    """
    return (access_key_id, access_key_secret)
    """
    access_key_id = open(ACCESS_KEY_ID).readline().rstrip()
    if not access_key_id:
        logger.error("{} error".format(ACCESS_KEY_ID))
        exit(-1)

    access_key_secret = open(ACCESS_KEY_SECRET).readline().rstrip()
    if not access_key_secret:
        logger.error("{} error".format(ACCESS_KEY_SECRET))
        exit(-1)

    return access_key_id, access_key_secret


def getip():
    return os.popen("curl http://members.3322.org/dyndns/getip -s").read(). \
        replace("\n", "").replace("\r\n", "")


def set_dns_records(record, ip, oldip):
    """
    UpdateDomainRecord
    """
    access_key_id, access_key_secret = get_access()
    clt = client.AcsClient(access_key_id, access_key_secret, "cn-hangzhou")
    request = RpcRequest("Alidns", "2015-01-09", "UpdateDomainRecord")
    request.add_query_param("RecordId", record["RecordId"])
    request.add_query_param("RR", record["RR"])
    request.add_query_param("Type", record["Type"])
    request.add_query_param("Value", ip)
    response = clt.do_action_with_exception(request)
    logger.info("{} old:{} new:{}".format(response.decode(), oldip, ip))


def get_dns_records(domain):
    """
    DescribeDomainRecords
    """
    access_key_id, access_key_secret = get_access()
    clt = client.AcsClient(access_key_id, access_key_secret, "cn-hangzhou")
    request = RpcRequest("Alidns", "2015-01-09", "DescribeDomainRecords")
    request.add_query_param("DomainName", domain)
    request.set_accept_format("json")
    response = clt.do_action_with_exception(request)
    response_json = json.loads(response.decode())
    return response_json


def main():
    option = PARSER.parse_args()

    sys.excepthook = error_handler

    ip = getip()
    recordlist = get_dns_records(option.hostname)["DomainRecords"]["Record"]

    for record in recordlist:
        if record["Value"] == ip:
            logger.info("ip {} have no change".format(ip))
        else:
            set_dns_records(record, ip, oldip=record["Value"])


if __name__ == "__main__":
    main()
