class Sensor:

    def __init__(self):

        self.name="sens"                  #attribut1
        self.type = "dist"                #attribut2
        self.min_measure_range_mm =1      #attribut3
        self.max_measure_range_mm = 2     #attribut4
        self.cunsumption_mA = 3           #attribut5
        self.output = "ana"               #attribut6

    def display_sensor_type(self):        #method1
        print(f" is a {self.type} sensor")

    def type_output(self):                #method2
        if self.output == "analog":
            print("The sensor has analog output")
        else:
            print("The sensor has digital output")





