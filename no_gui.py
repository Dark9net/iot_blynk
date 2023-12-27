import requests
import time

BLYNK_AUTH_TOKEN = 'nk24hJbhlmcJv9x6n8E49fH-Nx7sMrRb'
BLYNK_URL = f'https://blynk.cloud/external/api/'
def update_sensors():
    response_hum = requests.get(f'https://blynk.cloud/external/api/get?token=nk24hJbhlmcJv9x6n8E49fH-Nx7sMrRb&v5')
    if response_hum.status_code == 200:
        humidity_v5=float(response_hum.json())
        print(f'Humidity : {humidity_v5}')

    response_temp = requests.get(f'https://blynk.cloud/external/api/get?token=nk24hJbhlmcJv9x6n8E49fH-Nx7sMrRb&v6')
    if response_temp.status_code == 200:
        temp_v6=float(response_temp.json())
        print(f'Temperature : {temp_v6}')

def update_cont():
    update_sensors()
    time.sleep(3)
    update_cont()

update_cont()
