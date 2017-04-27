class ModelMass:
    def __init__(simulation):
        self.atmospheric_model = simulation.atmospheric_model
        relative_temp = 1- ambient_temprature/309.57 #ambite_temp / critical_temp
        self.nitrous_density = calculate_nitrous_density

    def calculate_nitrous_density:
        relative_temp = 1- atmospheric_model.surface_temprature/309.57 
        c_1 = 1.72328*math.pow(relative_temp, 1.0/3.0)
        c_2 = -0.83950*math.pow(relative_temp, 2.0/3.0)
        c_3 = 0.51060*relative_temp
        c_4 =  -0.10412*math.pow(relative_temp, 4.0/3.0)
        return 452*math.pow(math.e, c_1 + c_2 + c_3 + c_4)
