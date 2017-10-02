import math

class Point(object):


	first_pt = Point()
	second_pt = Point()

	first_pt.x = 2.0
	first_pt.y = 4.0

	second_pt.x = 10.0
	second_pt.y = 15.0

def distance_between_points(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

print distance_between_points(first_pt, second_pt)
