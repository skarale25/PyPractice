"""
@author: Snehal
@goal: To compute gravitational force
"""

def ComputeGravitationalForce(m1: float, m2: float, d: float)-> float:
    """
     To compute gravitational force
    :param m1: Magnitude of mass of object 1
    :param m2: magnitude of mass of object 2
    :param d: distance between masses
    :return: gravitational force F
    """
    G = 6.67 * (10 ** -11)
    F = (G * m1 * m2) / (d**2)
    return F


F = ComputeGravitationalForce(111.11, 23211.3, 12.2)
print(F)