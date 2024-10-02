from sensor import Sensor

sensor1=Sensor() #instance1
sensor2=Sensor() #instance2

sensor1.name="GY53"
sensor1.type="distance"
sensor1.min_measure_range_mm=100
sensor1.max_measure_range_mm=1200
sensor1.consumption_mA=5
sensor1.output="digital"

sensor2.name="QR1113"
sensor2.type="reflexion"
sensor2.min_measure_range_mm=2
sensor2.max_measure_range_mm=1
sensor2.consumption_mA=1
sensor2.output="analog"

print(sensor1.name)
sensor1.display_sensor_type()
sensor1.type_output()

print(sensor2.name)
sensor2.display_sensor_type()
sensor2.type_output()