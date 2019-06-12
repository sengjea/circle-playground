import json
import os
import socket

import boto3
import requests
import sys
import time
from fabric.api import *
from time import sleep

req = requests.post(url=os.environ['URL'], auth=(os.environ['USER'], os.environ['PASS'])) 
print(req.text)
