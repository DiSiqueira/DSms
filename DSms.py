#!/usr/bin/env python

"""
Diego Martins de Siqueira
MIT License
DSms - Send an SMS to a friend
"""

import argparse
import logging
import sys

import requests


def main():
    description = "Send an SMS to a friend"
    parser = argparse.ArgumentParser(
        description=description)
    parser.add_argument("--version", action="version", version='0.0.0.1',
                        help="Version Info")
    parser.add_argument("--number", type=int, default=5,
                        help="Number of SMSs to be sent. The default is 5.")
    parser.add_argument('friendNumber', type=int,
                        help='Your friend number')
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="increase output verbosity")

    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    logging.debug('Verbose increased')
    logging.debug('Params received START')
    logging.debug('Number: ' + str(args.number))
    logging.debug('FriendNumber: ' + str(args.friendNumber))
    logging.debug('Params received END')

    """
    curl 'https://meuvivoapp.vivo.com.br/mvapp/service/system/login' 
    -H 'Host: meuvivoapp.vivo.com.br' 
    -H 'Content-Type: application/json' 
    -H 'Connection: keep-alive' 
    -H 'Proxy-Connection: keep-alive' 
    -H 'Accept: */*' 
    -H 'User-Agent: Meu%20Vivo/60 CFNetwork/758.2.8 Darwin/15.0.0' 
    -H 'Accept-Language: en-us' 
    -H 'Accept-Encoding: gzip, deflate' 
    -H 'Content-Length: 219' 
    --data-binary '{"body": { "msisdn": "14996059889" }, "head": { "appType": "1", "appVersion": "3.5",
                    "deviceCode": "3E2A9", "deviceType": "13", "sessionId": "" } }'
    --verbose
    """

    try:

        url = "https://meuvivoapp.vivo.com.br/mvapp/service/system/login"
        data = '{"body": { "msisdn": "' + str(args.friendNumber)
        data += '" }, "head": { "appType": "1", "appVersion": "3.5", "deviceCode": "3E2A9",'
        data += ' "deviceType": "13", "sessionId": "" } }'

        headers = {
            'Host': 'meuvivoapp.vivo.com.br',
            'Content-Type': 'application/json',
            'Connection': 'keep-alive',
            'Proxy-Connection': 'keep-alive',
            'Accept': '*/*',
            'User-Agent': 'Meu%20Vivo/60 CFNetwork/758.2.8 Darwin/15.0.0',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Length': '219'
        }

        logging.debug('Params Request START')
        logging.debug('Url: ' + url)
        logging.debug('Data: ' + data)
        logging.debug('Headers: ' + str(headers))
        logging.debug('Params Request END')

        for sms in range(args.number):
            logging.debug('Starting Request')
            requests.post(url, data=data, headers=headers)
            logging.debug('Request finished')
            logging.debug('SMS sent')
            print("SMS Sent")

    except KeyboardInterrupt:
        print('Interrupt received, stopping SMSs')

    sys.exit()


if __name__ == "__main__":
    main()
