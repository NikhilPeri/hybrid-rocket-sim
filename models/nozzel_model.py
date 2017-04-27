class NozzelModel:
    def __init__(simulation):
        self.combustion_model = simulation.combustion_models

    # Newtons
    def thrust_force(t):
        return mass_flow(t)*exit_velocity(t) + (exit_pressure(t)-atmospheric_pressure(prev_position))*exit_area
