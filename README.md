# bigclown-python
BigClown libary for Python

## Example

### MQTT

#### Subscibe

```
import bigclown.mqtt

bc_mqtt = bigclown.mqtt.Client()

@bc_mqtt.subscribe("#")
def callback(msg):
    print(msg.topic)
    print(str(msg.payload, "utf-8"))
```

This example will connect you to the mqtt broker and subscribe all topics. Everytime when message come, it will call callback. When callback takes some time and in the same time new message come, queu is made and callback are processed one by one. You can process callback in paralal and no queu is made. So then for every callback is made another threading. You can do it by setting queu to False:

```
import bigclown.mqtt

bc_mqtt = bigclown.mqtt.Client()
bc_mqtt.queu = False

@bc_mqtt.subscribe("#")
def callback(msg):
    print(msg.topic)
    print(str(msg.payload, "utf-8"))
```

#### Publish

```
import bigclown.mqtt

bc_mqtt = bigclown.mqtt.Client()

bc_mqtt.publish("topic", "payload")
```

This example will publish topic "topic" and payload "payload".

### IFTTT
```
import bigclown.ifttt

bc_ifttt = bigclown.ifttt.Client("key")

print(bc_ifttt.send("event_name"))

```

With ifttt module you are able to invoke event via WebHooks same as in [Node-RED](https://www.bigclown.com/doc/projects/radio-push-button/). This example will print [status code](https://www.restapitutorial.com/httpstatuscodes.html) of ifttt request. So 200 is succeed for example.

## Install

```
git clone https://github.com/worepix/bigclown-python.git
cd bigclown-python
sudo pip3 install .
```
