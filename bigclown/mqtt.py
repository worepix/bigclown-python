import paho.mqtt.client as paho_mqtt
import webcolors

connection = paho_mqtt.Client()
connection.connect("localhost")
connection.subscribe("node/#")

class Sub(object):

   def __init__(self, topic = None):
      self.__topic = topic

   def __call__(self, func):
      
      def recieved(client, userdata, msg):
         func(msg)
         
      connection.message_callback_add(self.__topic, recieved)


   class Climate_Monitor(object):
      def __init__(self):
         pass

      @staticmethod
      def temperature(alias):
         def inner(func):
            @Sub("node/{0}/thermometer/0:0/temperature".format(alias))
            def respond(msg):
               func(msg)
            return respond
         return inner

      @staticmethod
      def illuminance(alias):
         def inner(func):
            @Sub("node/{0}/lux-meter/0:0/illuminance".format(alias))
            def respond(msg):
               func(msg)
            return respond
         return inner

      @staticmethod
      def relative_humidity(alias):
         def inner(func):
            @Sub("node/{0}/hygrometer/0:4/relative-humidity".format(alias))
            def respond(msg):
               func(msg)
            return respond
         return inner
      
   

def loop():
   while True:
      connection.loop()
   

class Colors(object):
   
   def __init__(self, color):
      self.__color = color

   def __repr__(self):
      if self.__color[0] != "#":
         return webcolors.name_to_hex(self.__color)

      else:
         return webcolors.normalize_hex(self.__color)