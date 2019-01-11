from bigclown import mqtt, ifttt
import json

bc_mqtt = mqtt.Client()
bc_mqtt.connect("localhost")
#bc_mqtt.publish("test_topic", "test_payload")
#bc_mqtt.publish("test", "neco")
#bc_mqtt.publish_device("helo")

bc_mqtt.publish_device(bc_mqtt.Devices().relay(0), bc_mqtt.States().false)

#bc_ifttt = ifttt.key("your_key")
#print(bc_ifttt.send("name_request"))