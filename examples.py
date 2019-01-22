from bigclown import mqtt, ifttt

@mqtt.Subscribe.Climate_Monitor.temperature("climate-monitor:0")
def callback_climate_monitor(msg):
    print("Climate: %s" % str(msg.payload, "utf-8"))
    request = ifttt.send("Your ID", "Event")

    if (request == 200):
        print("Sended via IFTTTT")

    else:
        print("Something went wrong")

@mqtt.Subscribe("#")
def callback_all(msg):
    print("Vsechno: %s" % str(msg.payload, "utf-8"))

mqtt.loop()