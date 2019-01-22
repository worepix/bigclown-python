# bigclown-python
BigClown libary for Python

## Example

### MQTT

```
from bigclown import mqtt

@mqtt.Sub.Climate_Monitor.temperature("climate-monitor:0")
def callback_climate_monitor(msg):
    print("Climate: %s" % str(msg.payload, "utf-8"))

mqtt.loop()
```

This example will connect you to the mqtt broker and send MQTT message to turn off [BigClown Relay Module](https://shop.bigclown.com/relay-module/).

### IFTTT
```
from bigclown import ifttt

ifttt.send("your_key", "event_name")

```

With ifttt module you are able to invoke event via WebHooks same as in [Node-RED](https://www.bigclown.com/doc/projects/radio-push-button/). This example will print status code of ifttt request.

## Install

```
git clone https://github.com/worepix/bigclown-python.git
cd bigclown-python
sudo pip3 install .
```