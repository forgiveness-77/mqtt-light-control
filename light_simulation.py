import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
TOPIC = "/student_group/light_control"

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    if message == "ON":
        print(" Light is TURNED ON")
    elif message == "OFF":
        print(" Light is TURNED OFF")

client = mqtt.Client()
client.on_message = on_message

client.connect(BROKER, 1883, 60)
client.subscribe(TOPIC)

print("Listening for MQTT messages...")
client.loop_forever()
