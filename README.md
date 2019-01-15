# bigclown-python
BigClown libary for Python

## Example

### MQTT

```
from bigclown import mqtt
import time

bc_mqtt.publish_device(bc_mqtt.Device().Relay("power-controller:0").States().false)
time.sleep(2)
bc_mqtt.publish_device(bc_mqtt.Device().Relay("power-controller:0").States().true)
bc_mqtt.publish_device(bc_mqtt.Device().Led_strip("power-controller:0").Colors().blue)
time.sleep(2)
bc_mqtt.publish_device(bc_mqtt.Device().Led_strip("power-controller:0").Effects().rainbow)
```

This example will connect you to the mqtt broker and send MQTT message to turn off and on [BigClown Relay Module](https://shop.bigclown.com/relay-module/). Then it will change to blue color and turn on rainbow effect on [BigClown Power Module](https://shop.bigclown.com/power-module/)

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
