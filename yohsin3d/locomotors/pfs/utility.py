import math
import numpy as np
from ...core.common.constants import *



class Utility:

    def __init__(self) -> None:
        pass

    @staticmethod
    def round_tuple(values, precision=2):
        rounded = []
        for i in range(len(values)):
            rounded.append(round(values[i], precision))
        return tuple(rounded)

    @staticmethod
    def spherical_to_cartesian(r, theta, phi):
        x = r * math.sin(phi) * math.cos(theta)
        y = r * math.sin(phi) * math.sin(theta)
        z = r * math.cos(phi)
        return Utility.round_tuple(values=(x, y, z))

    @staticmethod
    def cartesion_to_spherical(x, y, z):
        r = math.sqrt((x**2) + (y**2) + (z**2))
        theta = math.atan(y / x)
        phi = math.acos(z / r)
        return Utility.round_tuple(values=(r, theta, phi))

    @staticmethod
    def normalize_angle(angle):
        angle = angle % 360
        angle = (angle + 360) % 360
        if (angle > 180):
            angle -= 360
        return angle

    @staticmethod
    def get_angle(point1, point2): 
        angle = math.atan2(point1[1] - point2[1], point1[0] - point2[0])
        angle = math.degrees(angle)
        return angle
    
    @staticmethod
    def get_dribble_angle(point1, point2): 
        point3 = GOAL_MID_POSITION
        angle1 = math.atan2(point1[1] - point3[1], point1[0] - point3[0])
        angle2 = math.atan2(point2[1] - point3[1], point2[0] - point3[0])
        angle = math.degrees(angle1 - angle2)
        return angle


    @staticmethod
    def get_point_on_goal_line(point1, point2, distance):
        point_a = point1
        angle = math.atan2(point2[1] - point1[1], point2[0] - point1[0])
        point_b = (point_a[0] + distance * math.cos(angle),
                   point_a[1] + distance * math.sin(angle))
        return point_b

    @staticmethod
    def get_perpendicular_distance_to_line(p1, p2, p3):
        x1, y1 = p1
        x2, y2 = p2
        perpendicular_distance = abs((y2 - y1) * p3[0] - (
            x2 - x1) * p3[1] + x2 * y1 - y2 * x1) / math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
        return perpendicular_distance

    @staticmethod
    def getAngle2(
            p1, p2):  # These can also be four parameters instead of two arrays
        xDiff = p2[0] - p1[0]
        yDiff = p2[1] - p1[1]
        return math.atan2(yDiff, xDiff)
    

    @staticmethod
    def generate_linespace(point1, point2, num_points, offset_vector=(0, 0.25, 0)):
        start_point = np.subtract(point1, offset_vector)
        end_point = np.add(point2, offset_vector)
        return np.linspace(start_point, end_point, num_points)