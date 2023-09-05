# Import necessary modules
import time
import network
import db  # Import the custom database module

# Create an instance of the Database class to manage network data
my_db = db.Database('aps.json')

# Activate the Wi-Fi interface for scanning
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

# List of authentication modes for Wi-Fi networks
authmodes = ['Open', 'WEP', 'WPA-PSK', 'WPA2-PSK4', 'WPA/WPA2-PSK']

# Infinite loop to continuously scan for nearby APs
while True:
    # Iterate through the scanned Wi-Fi networks
    for (ssid, bssid, channel, RSSI, authmode, hidden) in sta_if.scan():
        try:
            try:
                # Format the BSSID (MAC address) as a string
                bssid = "{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}".format(*bssid)
            except:
                bssid = str(bssid)
            
            # Create a formatted authentication mode string
            auth = f"{authmodes[authmode]} (hidden)" if hidden else f"{authmodes[authmode]}"

            # Check if the BSSID is not already in the database
            record_value = my_db.get_record_by_bssid(bssid)
            if not record_value:
                # Create a new record for the scanned network
                found = {
                    "ssid": "{:s}".format(ssid),
                    "auth": auth,
                    "channel": "{}".format(channel),
                    "rssi": "{}".format(RSSI),
                    "bssid": bssid
                }
                # Get the key for the new record (incremental)
                last_record_key = my_db.get_last_record_key()
                if last_record_key:
                    record_key = str(int(last_record_key) + 1)
                else:
                    record_key = "1"
                # Add the new record to the database
                my_db.add_record(record_key, found)
        except:
            pass
    # Sleep for 1 second before scanning again
    time.sleep(1)
