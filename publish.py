import paho.mqtt.client as mqtt
import random
import time
import json
import ssl

AWS_IOT_ENDPOINT = "a25gujpzzv6qk5-ats.iot.us-east-1.amazonaws.com" 
port = 8883
rootCAPath = "certificates/AmazonRootCA1.pem"
certificatePath =  "certificates/2e0a45aa8f8b94cd0e7e44d498ed20b72975b652413bb6a181aca076880fc289-certificate.pem.crt"
privateKeyPath = "certificates/2e0a45aa8f8b94cd0e7e44d498ed20b72975b652413bb6a181aca076880fc289-private.pem.key"
topic = "sensors/IoT"

station_id = "IoT"

def generate_sensor_data():
    data = {
        "station_id": station_id,
        "timestamp": time.time(),
        "temperature": round(random.uniform(-50, 50), 2),
        "humidity": round(random.uniform(0, 100), 2),
        "co2": random.randint(300, 2000)
    }
    return data

client = mqtt.Client()

client.tls_set(ca_certs=rootCAPath,
               certfile=certificatePath,
               keyfile=privateKeyPath,
               cert_reqs=ssl.CERT_REQUIRED,
               tls_version=ssl.PROTOCOL_TLSv1_2)

client.connect(AWS_IOT_ENDPOINT, port, keepalive=60)

try:
    while True:
        sensor_data = generate_sensor_data()
        payload = json.dumps(sensor_data)
        client.publish(topic, payload)
        print(f"Published: {payload}")
        time.sleep(5)
except KeyboardInterrupt:
    print("Publisher stopped.")
    client.disconnect()