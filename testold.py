from bigclown import mqttold
import time
import datetime

bc = mqttold.Client()

def recieved(msg):
    print("recieved")

bc.subscribe("neco")
bc.on_message = recieved(msg)

bc.send("test_topic", "test_payload")