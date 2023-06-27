import paho.mqtt.publish as publish

MQTT_HOST = "localhost"  # change to the IP address of the ARM Linux system
MQTT_PORT = 1883
MQTT_TOPIC = "test/topic"
MESSAGE = "Hello world!"

publish.single(MQTT_TOPIC, payload=MESSAGE, hostname=MQTT_HOST, port=MQTT_PORT)
