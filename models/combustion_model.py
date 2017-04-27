class CombustionModel:
    def __init__(simulation):
        self.mass_model = simulation.mass_model

    # pascals
    def chamber_pressure(t):
        #TODO non-linear thrust
        return 2700000

    # Kelvin
    def chamber_temprature(t):
        return 2700

    # kg/s
    def mass_flow(t):
        return fuel_mass_flow(t) + oxidizer_mass_flow(t)

    # kg/s
    def fuel_mass_flow(t):
        gallon_cubic_meter = 264.172
        chamber_pressure = prev_chamber_pressure / 6894.76
        total_cv = math.sqrt(1.0/((1.0/math.pow(percentage_valve_open(t)*valve_cv,2))+(1.0/math.pow(injector_cv, 2))))
        return total_cv*math.sqrt((nitrous_density/1000.0)/(tank_pressure-chamber_pressure))*nitrous_density/(60*gallon_cubic_meter)

    # kg/s
    def oxidizer_mass_flow(t):
        gallon_cubic_meter = 264.172
        chamber_pressure = prev_chamber_pressure / 6894.76
        total_cv = math.sqrt(1.0/((1.0/math.pow(percentage_valve_open(t)*valve_cv,2))+(1.0/math.pow(injector_cv, 2))))
        return total_cv*math.sqrt((nitrous_density/1000.0)/(tank_pressure-chamber_pressure))*nitrous_density/(60*gallon_cubic_meter)

    def percentage_valve_open(t):
        return 1
