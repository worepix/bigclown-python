from bigclown import mqtt
import time

bc_mqtt = mqtt.Client()
bc_mqtt.connect("localhost")
#bc_mqtt.publish("test_topic", "test_payload")
#bc_mqtt.publish("test", "neco")
#bc_mqtt.publish_device("helo")

#bc_mqtt.publish_device(bc_mqtt.Devices().relay(0), bc_mqtt.States().false)

bc_mqtt.publish_device(bc_mqtt.Device().Relay("power-controller:0").States().false)
time.sleep(2)
bc_mqtt.publish_device(bc_mqtt.Device().Relay("power-controller:0").States().true)
time.sleep(2)
bc_mqtt.publish_device(bc_mqtt.Device().Led_strip("power-controller:0").Colors().blue)
time.sleep(2)
bc_mqtt.publish_device(bc_mqtt.Device().Led_strip("power-controller:0").Effects().rainbow)

#bc_ifttt = ifttt.key("your_key")
#print(bc_ifttt.send("name_request"))