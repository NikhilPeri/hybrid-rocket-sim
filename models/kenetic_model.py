class KeneticModel:
    def __init__(simulation):
        self.mass_model = simulation.mass_model
        self.nozzle_model = simulation.nozzle_model

    # m/s
    def velocity(t):
        return prev_velocity + time_step*(net_force(t)/mass(t))

    # Netwons
    def net_force(t):
        return thrust_force(t) - drag_force(t) - mass(t)*gravity

    # Newtons
    def drag_force(t):
        return coefficent_drag*((air_density(prev_position)*math.pow(prev_velocity, 2))/2)*cross_sectional_area
