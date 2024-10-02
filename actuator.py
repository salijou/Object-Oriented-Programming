class Actuator:

    def __init__(self):

        self.name = "act"
        self.speed_min_rpm=10               #attribut1
        self.speed_max_rpm = 100                #attribut2
        self.power_consumption_min =1      #attribut3
        self.power_consumption_max = 2     #attribut4

    def display_min_speed(self):        #method1
        print(f" {self.name} has a minimum speed of  {self.speed_min_rpm} rpm")

    def power(self):                #method2
        if self.power_consumption_max < 30 :
            print("The actuator has maximum power consumption less than 30 watt ")
        else:
            print("The actuator has maximum power consumption more than 30 watt")
