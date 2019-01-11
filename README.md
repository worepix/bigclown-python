# bigclown-python
BigClown libary for Python

## Example

### MQTT

```
from bigclown import mqtt

bc_mqtt = mqtt.Client()
bc_mqtt.connect("localhost")
bc_mqtt.publish_device(bc_mqtt.Devices().relay(0), bc_mqtt.States().false)
```

This example will connect you to the mqtt broker and send MQTT message to turn off [BigClown Relay Module](https://shop.bigclown.com/relay-module/).

### IFTTT
```
from bigclown import ifttt

bc_ifttt = ifttt.key("your_key")
print(bc_ifttt.send("name_event"))
```

With ifttt module you are able to invoke event via WebHooks same as in [Node-RED](https://www.bigclown.com/doc/projects/radio-push-button/). This example will print status code of ifttt request.

## Install

```
git clone https://github.com/worepix/bigclown-python.git
cd bigclown-python
sudo pip3 install .
```