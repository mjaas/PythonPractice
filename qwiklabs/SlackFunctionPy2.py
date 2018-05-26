from __future__ import print_function

import boto3
import json
import logging

from base64 import b64decode
from urllib2 import Request, urlopen, URLError, HTTPError

SLACK_CHANNEL = '#general'

HOOK_URL = "https://hooks.slack.com/services/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"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Event: " + str(event))
    message = event['Records'][0]['Sns']['Message']
    logger.info("Message: " + str(message))

    alarm_name = message['AlarmName']
    #old_state = message['OldStateValue']
    new_state = message['NewStateValue']
    reason = message['NewStateReason']

    slack_message = {
        'channel': SLACK_CHANNEL,
        'text': "%s state is now %s: %s" % (alarm_name, new_state, reason)
    }

    req = Request(HOOK_URL, json.dumps(slack_message))
    try:
        response = urlopen(req)
        response.read()
        logger.info("Message posted to %s", slack_message['channel'])
    except HTTPError as e:
        logger.error("Request failed: %d %s", e.code, e.reason)
    except URLError as e:
        logger.error("Server connection failed: %s", e.reason)
