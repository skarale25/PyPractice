"""
@author: Snehal
@goal: To compute the distance between 2D points whose coordinates are given
"""
def ComputeDistanceBetween2DPoints(x1: float, y1: float, x2: float, y2: float)-> float:
    """
    Compute Distance between P1(x1,y1), P2(x2,y2)
    :param x1: x coordinate of point 1
    :param y1: y coordinate of point 1
    :param x2: x coordinate of point 2
    :param y2: y coordinate of point 2
    :return: Distance between P1(x1,y1), P2(x2,y2)
    """
    d = ((y2 - y1)**2 + (x2 - x1) ** 2) ** 0.5
    return d