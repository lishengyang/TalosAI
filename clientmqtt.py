import paho.mqtt.subscribe as subscribe

def on_message_received(client, userdata, message):
    print("Received message: " + message.payload.decode())

MQTT_HOST = "localhost"  # change to the IP address of the ARM Linux system
MQTT_PORT = 1883
MQTT_TOPIC = "test/topic"

subscribe.callback(on_message_received, MQTT_TOPIC, hostname=MQTT_HOST, port=MQTT_PORT)
