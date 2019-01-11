import paho.mqtt.client as mqtt
import json
 
class Client(mqtt.Client):

   class Devices(object):
      def relay(self, id_number):
         return "node/{0}/relay/-/state/set".format(id_number)

      def ledstrip_color(self, id_number):
         return "node/{0}/led-strip/-/color/set".format(id_number)

   class Colors(object):

      @property
      def red(self):
         return '{color: "#ff0000"}'

      @property
      def blue(self):
         return '{color: "#0000ff"}'

      @property
      def green(self):
         return '{color: "#00ff00"}'

   class States(object):
      
      @property
      def true(self):
         return '{state: "true"}'
   
      @property
      def false(self):
         return '{state: "false"}'
   
   def publish_device(self, device, payload):
         self.publish(device, payload)
