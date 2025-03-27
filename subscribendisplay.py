import paho.mqtt.client as mqtt
import json
import time
from datetime import datetime, timedelta
import ssl

AWS_IOT_ENDPOINT = "a25gujpzzv6qk5-ats.iot.us-east-1.amazonaws.com" 
port = 8883
rootCAPath = "certificates/AmazonRootCA1.pem"
certificatePath =  "certificates/2e0a45aa8f8b94cd0e7e44d498ed20b72975b652413bb6a181aca076880fc289-certificate.pem.crt"
privateKeyPath = "certificates/2e0a45aa8f8b94cd0e7e44d498ed20b72975b652413bb6a181aca076880fc289-private.pem.key"
topic = "sensors/IoT"

data_store = []

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        data = json.loads(payload)
        data_store.append(data)
        print("Received:", data)
    except Exception as e:
        print("Error processing message:", e)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.tls_set(ca_certs=rootCAPath,
               certfile=certificatePath,
               keyfile=privateKeyPath,
               cert_reqs=ssl.CERT_REQUIRED,
               tls_version=ssl.PROTOCOL_TLSv1_2)

client.connect(AWS_IOT_ENDPOINT, port, keepalive=60)
client.loop_start()

print("Accumulating data for 30 seconds...")
time.sleep(30)

def display_latest_data(station_id):
    station_data = [d for d in data_store if d.get("station_id") == station_id]
    if not station_data:
        print(f"No data available for station {station_id}.")
        return
    latest = max(station_data, key=lambda x: x["timestamp"])
    print(f"\nLatest data for station {station_id}:")
    print(f"Temperature: {latest['temperature']} °C")
    print(f"Humidity: {latest['humidity']} %")
    print(f"CO2: {latest['co2']} ppm")
    print("Timestamp:", datetime.fromtimestamp(latest['timestamp']))

def display_last_five_hours(sensor_type):
    now = time.time()
    five_hours_ago = now - 5 * 3600
    filtered_data = [d for d in data_store if d["timestamp"] >= five_hours_ago and sensor_type in d]
    if not filtered_data:
        print(f"No data for sensor '{sensor_type}' in the last five hours.")
        return
    print(f"\nData for sensor '{sensor_type}' in the last five hours:")
    for entry in filtered_data:
        print(f"Station: {entry['station_id']}, {sensor_type.capitalize()}: {entry[sensor_type]}, "
              f"Time: {datetime.fromtimestamp(entry['timestamp'])}")

display_latest_data("IoT")
display_last_five_hours("temperature")

client.loop_stop()
client.disconnect()
