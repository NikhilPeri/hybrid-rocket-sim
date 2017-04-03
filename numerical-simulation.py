#ALL VALUES IN METRIC
import math
import numpy as np

gravity = 9.81
ambient_temprature = 293 #kelvin
burn_time = 2
coefficent_drag = 0.8
initial_mass = 5
prev_mass = initial_mass
prev_position = 0
prev_velocity = 0
time_step = 0.001

def run():
    initializeModel()

    global prev_velocity
    global prev_position
    global prev_mass
    global prev_chamber_pressure
    prev_chamber_pressure = atmospheric_pressure(0)
    print mass_flow(0)
    for time in np.arange(0, burn_time, time_step):
        #order matters
        prev_velocity = velocity(time)
        prev_position += prev_velocity*time_step
        prev_mass = mass(time)
        prev_chamber_pressure = chamber_pressure(time)

    print "burnout altitude(m): " + str(prev_position)
    print "burnout velocity(m/s) " + str(prev_velocity)

def initializeModel():
    #============================================
    #Aero
    global body_diameter
    body_diameter = 5.5 * 0.0254 #inch * m/inch
    global cross_sectional_area
    cross_sectional_area = math.pi*math.pow(body_diameter/2, 2)
    #============================================
    #Mass
    global nitrous_density
    relative_temp = 1- ambient_temprature/309.57 #ambite_temp / critical_temp
    nitrous_density = math.pow(math.e, (1.72328*math.pow(relative_temp, 1.0/3.0)-0.83950*math.pow(relative_temp, 2.0/3.0) + 0.51060*relative_temp -0.10412*math.pow(relative_temp, 4.0/3.0)))*452
    global parrafin_density
    parrafin_density = 900 #TODO get realistic value

    #============================================
    #Combustion
    global tank_pressure # tank_pressure in PSI
    tank_pressure = math.pow(10, (61.5168 - 2101.6/ambient_temprature - 22.337*math.log(ambient_temprature, 10) + 0.018232*ambient_temprature - 0.00000000011348*math.pow(ambient_temprature, 2)))*0.0193367747
    global valve_cv
    valve_cv = 1.5
    global injector_cv
    injector_cv = 1.5 #TODO actual value
    #============================================
    #Nozzle
    global exit_area
    exit_area = cross_sectional_area/2

# m/s
def velocity(t):
    return prev_velocity + time_step*(net_force(t)/mass(t))

# Netwons
def net_force(t):
    return thrust_force(t) - drag_force(t) - mass(t)*gravity

# Newtons
def drag_force(t):
    return coefficent_drag*((air_density(prev_position)*math.pow(prev_velocity, 2))/2)*cross_sectional_area

# Newtons
def thrust_force(t):
    return mass_flow(t)*exit_velocity(t) + (exit_pressure(t)-atmospheric_pressure(prev_position))*exit_area

# m/s
def exit_velocity(t):
    #TODO non-linear thrust
    return 343

def exit_pressure(t):
    #TODO correct nozzle geometery
    return chamber_pressure(t)

# pascals
def chamber_pressure(t):
    #TODO non-linear thrust
    return 2700000

# kg/s
def mass_flow(t):
    gallon_cubic_meter = 264.172
    chamber_pressure = prev_chamber_pressure / 6894.76
    total_cv = math.sqrt(1.0/((1.0/math.pow(percentage_valve_open(t)*valve_cv,2))+(1.0/math.pow(injector_cv, 2))))
    return total_cv*math.sqrt((nitrous_density/1000.0)/(tank_pressure-chamber_pressure))*nitrous_density/(60*gallon_cubic_meter)

def percentage_valve_open(t):
    return 1

# kg
def mass(t):
    return prev_mass - time_step*mass_flow(t)

# pascals
def atmospheric_pressure(d):
    #TODO better model
    return 101325

# kg/m^3
def air_density(d):
    #TODO better model
    return 1.225

if __name__ == '__main__':
    run()
