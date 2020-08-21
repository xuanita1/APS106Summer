import math

def horizontal_distance(v, theta, del_h):
    """ (num, num, num) -> (num)
    This function receives initial velocity, launch angle, and altitude change
    in the landing position and returns the horizontal range of a projectile.

    v     is in [m/s]
    theta is in [degrees]
    del_h is in [m]

    >>> range = horizontal_distance(100, 20, 40)
    >>> range
	515.5652309241808
    """
    gravitational_acceleration = 9.81
    theta_converted = theta * (math.pi/180) #converts theta from given degrees to radians
    #split range equation into four parts so it's cleaner when pieced together
    first_term = v*math.cos(theta_converted)
    second_term= (v*math.sin(theta_converted))/gravitational_acceleration
    third_term = (pow(v, 2)*pow(math.sin(theta_converted), 2))/ pow(gravitational_acceleration, 2)
    fourth_term = (2*del_h)/gravitational_acceleration
    
    range = first_term*(second_term + math.sqrt(third_term - fourth_term))
    return range

# test code

velocity = 100
angle = 20
delta_h = 40

range = horizontal_distance(velocity, angle, delta_h)
print("\nThe range is: " + str(range))
