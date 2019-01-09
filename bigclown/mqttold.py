import paho.mqtt.client as paho_mqtt
 
class Client:

    def __init__(self, host="localhost", port=1883, keep_alive=60, client_id="", clean_session=True, userdata=None, protocol="MQTTv311", transport="tcp", bind_adress=""):
        
        if protocol is "MQTTv311":
            protocol = 4

        else:
            protocol = 3

        self.__paho_client = paho_mqtt.Client(client_id, clean_session, userdata, protocol, transport)
        self.__paho_client.connect(host, port, keep_alive, bind_adress)
        self.on_connect = paho_mqtt.Client.on_connect
        self.on_message = paho_mqtt.Client.on_message

    def send(self, topic, message):
        self.__paho_client.publish(topic, message)

    def subscribe(self, topic, qos=0):
        self.__paho_client.subscribe(topic, qos)