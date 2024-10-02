from actuator import Actuator


actuator1=Actuator() #instance1
actuator2=Actuator() #instance2

actuator1.name="DC motor"
actuator1.speed_min_rpm=1000
actuator1.speed_max_rpm=100
actuator1.power_consumption_min=5
actuator1.power_consumption_max=500

actuator2.name="Servo motor"
actuator2.speed_min_rpm=60
actuator2.speed_max_rpm=300
actuator2.power_consumption_min=1
actuator1.power_consumption_max=20

print(actuator1.name)
actuator1.display_min_speed()
actuator1.power()

print(actuator2.name)
actuator2.display_min_speed()
actuator2.power()
