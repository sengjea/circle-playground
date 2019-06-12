import json
import os
import socket

import boto3
import requests
import sys
import time
from fabric.api import *
from time import sleep

event = {
    what: "Circle CI",
    tags: ["test"],
    data: "Data sent from CircleCI"


}

req = requests.post(url="{base}/events/".format(base=os.environ['URL']), json=event, auth=(os.environ['USER'], os.environ['PASS'])) 
print(req.text)
