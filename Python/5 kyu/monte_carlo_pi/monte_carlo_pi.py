# In this kata we will see a method, not so accurate but a different one to estimate number Pi.
# You will be given a list of random points contained in a cube of side of length 2l.
# The center of the cube coincides with the center of the coordinates system xyz, the point (0, 0, 0).
# You can see the above image to understand that the radius of the spehere is half of the side of the cube.
# To estimate Pi we should count the amount of points that are contained in the sphere inscribed in the cube.

# The function mCarlo3D_pi(), will receive a list of numeruous points. An estimation of the length side of the cube,
# and of course, the radius of the sphere, has to be deduced from this list.

# The function mCarlo3D_pi() , will output in a list

# [(1), (2), (3), (4), (5), (6)]

# (1) - Total amount of points.

# (2) - Estimated radius of the inscribed sphere.

# (3) - Number of points contained in the sphere(including the ones in its surphace).

# (4) - Estimation of Pi as a float with a maximum of four decimals (rounded result).

# (5) - Relative error, relError= abs(real Val of Pi - estmimated Val of Pi) / (real Val of Pi) * 100 rounded with two decimals
# and expressed as a string with the symbol "%"

# (6) - A boolean variable according to the constraints bellow

import numpy as np
import math
def mCarlo3D_pi(lst):
    total_points = len(lst)
    est_radius = max([max(max(i),abs(min(i))) for i in lst])
    insc_points = len([i for i in lst if np.linalg.norm(i)<=est_radius])
    est_pi_unround = 6*(insc_points/total_points)
    est_pi = round(est_pi_unround,4)
    relError = abs(((math.pi - est_pi_unround)/math.pi))*100
    boolean_val = relError<5
    return [total_points,est_radius,insc_points,est_pi,str(round(relError,2))+'%',boolean_val]