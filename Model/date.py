import sys,json
import numpy as np
import re, uuid
from datetime import datetime
def realtime():
    now = datetime.now()
    dtime_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dtime_string
def addressmac():
    mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    return mac
resul='static/20173084.jpg'