import time
import network
import db


my_db = db.Database('aps.json')

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

authmodes = ['Open', 'WEP', 'WPA-PSK', 'WPA2-PSK4', 'WPA/WPA2-PSK']

while True:
    for (ssid, bssid, channel, RSSI, authmode, hidden) in sta_if.scan():
        try:
            try:
                bssid = "{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}".format(*bssid)
            except:
                bssid = str(bssid)
            auth = f"{authmodes[authmode]} (hidden)" if hidden else f"{authmodes[authmode]}"
            record_value = my_db.get_record_by_bssid(bssid)
            if not record_value:
                found = {"ssid": "{:s}".format(ssid),
                         "auth": auth,
                         "channel": "{}".format(channel),
                         "rssi": "{}".format(RSSI),
                         "bssid": bssid
                         }
                last_record_key = my_db.get_last_record_key()

                if last_record_key:
                    record_key = str(int(last_record_key) + 1)
                else:
                    record_key = "1"
                my_db.add_record(record_key, found)
        except:
            pass
    time.sleep(1)
