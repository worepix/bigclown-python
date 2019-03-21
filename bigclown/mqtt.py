import paho.mqtt.client as paho_mqtt
import webcolors
import time
import bigclown.threading


def getcolor(color):
    if color != "#":
        return webcolors.name_to_hex(color)

    else:
        return webcolors.normalize_hex(color)


class Client:
    def __init__(self, host="localhost", port=1883, client_id="", protocol=4,
                 clean_session=True, userdata=None, transport="tcp"):
                self._client = paho_mqtt.Client(client_id, clean_session,
                                                userdata, protocol, transport)
                self._client.connect(host, port=1883,
                                     keepalive=60, bind_address="")
                self._subscribed_topics = []
                self.callback_queu = True
                self._bc_threading = bigclown.threading.Thread()

    def subscribe(self, topic):
        def inner(func):
            def respond(client, userdata, msg):
                @self._bc_threading.synchronize(msg)
                def output_message(message):
                    func(message)
                return output_message

            @self._bc_threading.add("Subscribe")
            def make_thread():
                if topic not in self._subscribed_topics:
                    self._client.subscribe(topic)
                    self._subscribed_topics.append(topic)

                self._client.message_callback_add(topic, respond)
                self._client.loop_start()
                while True:
                    time.sleep(1)
            return make_thread
        return inner

    def publish(self, topic, payload, qos=0):
        self._client.publish(topic, payload, qos)
