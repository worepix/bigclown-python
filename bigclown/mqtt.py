import paho.mqtt.client as paho_mqtt
import threading
import webcolors
import time

def getcolor(color):
   if color != "#":
      return webcolors.name_to_hex(color)

   else:
      return webcolors.normalize_hex(color)


class Client:

   def __init__(self, host="localhost", port=1883, keepalive=60, client_id="", 
               clean_session=True, userdata=None, protocol=4, transport="tcp"):
      self._lock = threading.RLock()
      self._client = paho_mqtt.Client(client_id, clean_session, 
                     userdata, protocol, transport)
      self._client.connect(host, port=1883, keepalive=60, bind_address="")
      self._subscribed_topics = []
      self.callback_queu = True

   def subscribe(self, topic):
      def inner(func):
         def respond(client, userdata, msg):
            self._lock.acquire()
            message = msg
            self._lock.release()

            if self.callback_queu == False:
               callback_thread = threading.Thread(target=func, args=(message,), name="Subsribe respond thread: {0}"
                              .format(threading.active_count()))
               callback_thread.start()

            else:
               func(message)
         
         def make_thread():
            if not topic in self._subscribed_topics:
               self._client.subscribe(topic)
               self._subscribed_topics.append(topic)

            self._client.message_callback_add(topic, respond)
            self._client.loop_start()
            while True:
               time.sleep(1)

         t = threading.Thread(target=make_thread, name="Subsribe topic {0}"
                              .format(topic))
         t.start()

      return inner

   def publish(self, topic, payload, qos = 0):
      self._client.publish(topic, payload, qos)