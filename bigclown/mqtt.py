import paho.mqtt.client as paho_mqtt
            
class Devices(object):
      def __init__(self):
        pass
        
      class Relay(object):
         _global_id_number = None
         
         def __init__(self, alias):
            Devices.Relay._global_id_number = alias
            
         class States(object):
            def __init__(self):
                self.__topic = "node/{0}/relay/0:0/state/set".format(Devices.Relay._global_id_number)
            
            @property
            def true(self):
               return [self.__topic, "true"]
                            
            @property
            def false(self):
                return [self.__topic, "false"]

      class Led_strip(object):
         _global_id_number = None
         
         def __init__(self, alias):
            Devices.Led_strip._global_id_number = alias

         class Colors(object):
            def __init__(self):
               self.__topic = "node/{0}/led-strip/-/color/set".format(Devices.Led_strip._global_id_number)

            @property
            def red(self):
               return [self.__topic, '"#ff0000"']

            @property
            def blue(self):
               return [self.__topic, '"#0000ff"']

            @property
            def green(self):
               return [self.__topic, '"#00ff00"']

               

         class Effects(object):
            def __init__(self):
               self.__topic = "node/{0}/led-strip/-/effect/set".format(Devices.Led_strip._global_id_number)

            @property
            def rainbow(self):
               return [self.__topic, '{"type":"rainbow", "wait":50}']

            

class Client(paho_mqtt.Client):
   
   def publish_device(self, device_and_value):
      self.publish(device_and_value[0], device_and_value[1])

   class Device(Devices):
      pass