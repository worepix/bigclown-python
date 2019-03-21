import bigclown.mqtt
import bigclown.threading
import time

bc_mqtt = bigclown.mqtt.Client()


@bc_mqtt.subscribe("#")
def callback(message):
    i = 0

    while i < 5:
        i += 1
        print(i)
        time.sleep(1)

    print(str(message.payload, "utf-8"))


@bc_mqtt.subscribe("test")
def callback2(message):
    print("neco")
    print(str(message.payload, "utf-8"))