from reportlab.lib.validators import isInstanceOf

from zklib import zklib
import threading


# print current lock user 
def add_record(record):
    print(record)


zk = zklib.ZKLib("192.168.1.103", 4370)  # IP of my device was 192.168.1.103
res = zk.connect()


temp = 0  # flag to disconnect
if res:
    while temp < 4:
        data = zk.zkrecvCurrentAtt()   # (uid, time)
        if data:
            if isinstance(data, bool):
                continue
            t = threading.Thread(target=add_record, args=(data,))
            t.start()
            temp += 1

#zk.disconnect()


