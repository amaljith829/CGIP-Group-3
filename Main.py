import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Define the original point coordinates
x = 0.5
y = 1.5

# Define the rotation angle in degrees
theta_deg = 45

# Convert the rotation angle to radians
theta_rad = np.radians(theta_deg)

# Define the rotation matrix
c, s = np.cos(theta_rad), np.sin(theta_rad)
R = np.array(((c, -s), (s, c)))

# Define the original polygon
poly = Polygon([[x,y], [x+1,y], [x+1,y+1], [x,y+1]], fill=False, color='b')

# Apply the rotation to the polygon
rotated_poly = Polygon(np.dot(R, np.array(poly.get_xy()).T).T, fill=False, color='r')

# Create a figure and axis object
fig, ax = plt.subplots()

# Add the original and rotated polygons to the plot
ax.add_patch(poly)
ax.add_patch(rotated_poly)

# Set the axis limits
ax.set_xlim([x-2, x+2])
ax.set_ylim([y-2, y+2])

# Add a title and legend
ax.set_title(f"Clockwise rotation of ({x},{y}) by {theta_deg} degrees")
ax.legend([poly, rotated_poly], ["Original", "Rotated"])

# Show the plot
plt.show()

