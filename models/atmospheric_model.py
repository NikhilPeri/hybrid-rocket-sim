class AtmosphericModel:
    def __init__(simulation):
        self.kenetic_model = simulation.kenetic_model

        self.surface_temprature = 293 #Kelvin
        
    # pascals
    def atmospheric_pressure(d):
        #TODO better model
        return 101325

    # kg/m^3
    def air_density(d):
        #TODO better model
        return 1.225
